#!/usr/bin/env python3
"""Repair the ssg output for draftlib.com.

ssg emits several artefacts that a browser cannot render as intended. Each
pass below fixes one of them, and each is a no-op when its artefact is absent,
so the script is idempotent and safe to re-run.

1. Head metas arrive HTML-escaped, so ``<meta …>`` renders as visible text at
   the top of every page instead of being parsed as markup.
2. ssg injects a second ``description`` and ``viewport`` meta synthesised from
   page text. The authored one is kept and the duplicates dropped.
3. The syntax highlighter nests an inline-styled ``<pre>`` inside the markdown
   code block. Those inline styles are blocked by the strict CSP, leaving
   broken boxes around every fenced sample, so the wrapper is unwrapped and
   the layout's own code styling used instead.
4. Presentational ``align`` attributes on table cells fail WCAG H49.
5. The search widget injects a ``<link rel=stylesheet>`` inside ``<body>``,
   which fails WCAG H59; links belong in the head.
6. The taxonomy plugin renders ``tags/`` pages from its own built-in template
   rather than from ``_layouts/``, so they ship with neither the security head
   metas nor the ``og:image`` card the layouts declare — ``ssg audit`` reports
   CSP-MISSING and OG-IMAGE for each. Both sets are copied onto them from a
   layout-rendered page rather than written out again here, so ``_layouts/``
   stays the single source of truth and the copy picks up the policy ssg
   itself rewrites when it externalises inline styles. A ``_headers`` file
   would also silence the CSP warning, but GitHub Pages ignores it, so it
   would silence the audit without delivering the header.

Usage: python3 scripts/postbuild_fix.py <output-dir>
"""

from __future__ import annotations

import html as _html
import re
import sys
from pathlib import Path

_ESCAPED_HEAD_TAG = re.compile(r"&lt;(?:meta|link)\b.*?(?:&gt;|>)", re.DOTALL)

# ssg entity-escapes the whole {{content}} blob, so the rendered markdown
# arrives as literal "&lt;div lang=..." text rather than markup. The close tag
# is searched literally: an escaped blob cannot contain one, so the first match
# ends the container.
_BODY_MARKER = "&lt;div lang="
_CONTAINERS = [
    (('<article class="content-body">', "<article class=content-body>"), "</article>"),
    (('<div class="content-body">', "<div class=content-body>"), "</div>"),
]


def fix_body(html: str) -> str:
    # Every container is scanned, not just the first: a page may hold several
    # content-body blocks (the home page hard-codes one for its code samples,
    # because ssg whitespace-collapses the {{content}} blob on index pages and
    # a fenced block written in markdown would lose its newlines). Stopping at
    # the first would leave the real content escaped.
    for opens, close in _CONTAINERS:
        for open_tag in opens:
            pos = 0
            while True:
                start = html.find(open_tag, pos)
                if start == -1:
                    break
                inner_start = start + len(open_tag)
                inner_end = html.find(close, inner_start)
                if inner_end == -1:
                    break
                inner = html[inner_start:inner_end]
                if _BODY_MARKER in inner:
                    fixed = _html.unescape(inner)
                    html = html[:inner_start] + fixed + html[inner_end:]
                    pos = inner_start + len(fixed)
                else:
                    pos = inner_end
    return html


# fix_body unescapes the whole blob, which strips inline `<code>` spans bare —
# markdown's `<tag>` would become a real element and vanish from the page. Block
# code survives (it was escaped twice); inline code was escaped once, so it is
# re-escaped here. <pre> contents are excluded: their markup is legitimate.
_PRE_BLOCK_RE = re.compile(r"<pre\b.*?</pre>", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"(<code\b[^>]*>)(.*?)(</code>)", re.DOTALL)


def escape_inline_code(html: str) -> str:
    spans: list[str] = []

    def stash(m: re.Match) -> str:
        spans.append(m.group(0))
        return "\x00PRE%d\x00" % (len(spans) - 1)

    body = _PRE_BLOCK_RE.sub(stash, html)

    def fix(m: re.Match) -> str:
        inner = m.group(2)
        if "<" not in inner and ">" not in inner:
            return m.group(0)
        inner = inner.replace("<", "&lt;").replace(">", "&gt;")
        return m.group(1) + inner + m.group(3)

    body = _INLINE_CODE_RE.sub(fix, body)
    return re.sub(r"\x00PRE(\d+)\x00", lambda m: spans[int(m.group(1))], body)


def fix_head(html: str) -> str:
    """Unescape head metas that ssg entity-escaped."""
    end = html.find("</head>")
    if end == -1:
        return html
    head = html[:end]
    if "&lt;meta" not in head and "&lt;link" not in head:
        return html
    head = _ESCAPED_HEAD_TAG.sub(lambda m: _html.unescape(m.group(0)), head)
    return head + html[end:]


# theme-color is left alone: its light/dark pair legitimately repeats with
# different media queries.
_DEDUPE_NAMES = ("description", "viewport")


def dedupe_head_metas(html: str) -> str:
    end = html.find("</head>")
    if end == -1:
        return html
    head = html[:end]
    for name in _DEDUPE_NAMES:
        # ssg re-emits metas with attributes in arbitrary order, so anchor on
        # the name attribute wherever it appears rather than on position.
        pattern = re.compile(
            r'<meta\b(?=[^>]*\bname=["\']?%s["\']?[\s>])[^>]*>\s*' % name)
        matches = list(pattern.finditer(head))
        for m in reversed(matches[1:]):
            head = head[: m.start()] + head[m.end():]
    return head + html[end:]


_CODE_BLOCK_RE = re.compile(r"(<pre><code[^>]*>)(.*?)(</code></pre>)", re.DOTALL)
_INNER_PRE_RE = re.compile(r"</?pre[^>]*>")
_SPAN_RE = re.compile(r"</?span[^>]*>")


def fix_code_blocks(html: str) -> str:
    def unwrap(m: re.Match) -> str:
        inner = _SPAN_RE.sub("", _INNER_PRE_RE.sub("", m.group(2)))
        return m.group(1) + inner.strip("\n") + m.group(3)

    return _CODE_BLOCK_RE.sub(unwrap, html)


_ALIGN_ATTR_RE = re.compile(r"(<t[dhr]\b[^>]*?)\s+align=\"?[a-z]+\"?")


def strip_align_attrs(html: str) -> str:
    return _ALIGN_ATTR_RE.sub(r"\1", html)


_BODY_LINK_RE = re.compile(r"<link rel=\"stylesheet\"[^>]*>")


def relocate_body_stylesheets(html: str) -> str:
    head_end = html.find("</head>")
    if head_end == -1:
        return html
    body = html[head_end:]
    moved = _BODY_LINK_RE.findall(body)
    if not moved:
        return html
    body = _BODY_LINK_RE.sub("", body)
    return html[:head_end] + "".join(moved) + body


PASSES = (
    fix_head,
    dedupe_head_metas,
    fix_body,
    escape_inline_code,
    fix_code_blocks,
    strip_align_attrs,
    relocate_body_stylesheets,
)


# Matched against a whole <meta> tag, so attribute order does not matter, and
# the optional quotes cover both the authored and the minified output.
#
# The og:image set rides along with the security metas because the taxonomy
# template omits both, and the card is site-wide rather than per-page: a tag
# listing shares the same preview image as everything else.
def _meta(attr: str, value: str) -> re.Pattern:
    """Match a whole <meta> tag whose *attr* is exactly *value*.

    The value is anchored: an unquoted `property=og:image` must be followed by
    whitespace or `>`, or the og:image pattern would also match the og:image
    :width tag that shares its prefix.
    """
    v = re.escape(value)
    return re.compile(
        r'<meta\b[^>]*\b%s=(?:"%s"|\'%s\'|%s(?=[\s>]))[^>]*>' % (attr, v, v, v),
        re.I)


def _http_equiv(name: str) -> re.Pattern:
    return _meta("http-equiv", name)


def _prop(name: str) -> re.Pattern:
    return _meta("property", name)


_SHARED_HEAD_METAS = (
    _http_equiv("Content-Security-Policy"),
    _http_equiv("Permissions-Policy"),
    _http_equiv("X-Content-Type-Options"),
    re.compile(r'<meta\b[^>]*name=["\']?referrer["\']?[^>]*>', re.I),
    _prop("og:image"),
    _prop("og:image:type"),
    _prop("og:image:width"),
    _prop("og:image:height"),
    _prop("og:image:alt"),
)

_HEAD_OPEN_RE = re.compile(r"<head\b[^>]*>", re.I)
_HEAD_CLOSE_RE = re.compile(r"</head\s*>", re.I)


def _head_of(html: str) -> str | None:
    open_m = _HEAD_OPEN_RE.search(html)
    close_m = _HEAD_CLOSE_RE.search(html)
    if not open_m or not close_m or close_m.start() < open_m.end():
        return None
    return html[open_m.end():close_m.start()]


def harvest_shared_head_metas(pages: list[str]) -> list[tuple[re.Pattern, str]]:
    """Take the shared head metas off the first page that carries all of them.

    Pages rendered from _layouts/ have the full set; the taxonomy pages have
    none. Requiring the complete set means a partially-built page can never
    become the donor.
    """
    for html in pages:
        head = _head_of(html)
        if head is None:
            continue
        found = []
        for pattern in _SHARED_HEAD_METAS:
            m = pattern.search(head)
            if not m:
                break
            found.append((pattern, m.group(0)))
        if len(found) == len(_SHARED_HEAD_METAS):
            return found
    return []


_CHARSET_RE = re.compile(r"<meta\b[^>]*\bcharset\b[^>]*>", re.I)


def apply_shared_head_metas(html: str, donor: list[tuple[re.Pattern, str]]) -> str:
    """Add any shared meta the page is missing, high in <head>.

    Inserted *after* the charset declaration, never before it: the CSP alone
    runs to ~900 bytes, and HTML requires the encoding to be declared within
    the first 1024 bytes of the document. Going in first would leave charset
    47 bytes short of the limit and one new CSP directive away from breaking
    encoding detection.
    """
    if not donor:
        return html
    head = _head_of(html)
    if head is None:
        return html
    missing = [tag for pattern, tag in donor if not pattern.search(head)]
    if not missing:
        return html

    open_m = _HEAD_OPEN_RE.search(html)
    charset_m = _CHARSET_RE.search(html, open_m.end(), open_m.end() + len(head))
    at = charset_m.end() if charset_m else open_m.end()
    return html[:at] + "\n  " + "\n  ".join(missing) + html[at:]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: postbuild_fix.py <output-dir>", file=sys.stderr)
        return 2
    root = Path(argv[1])
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 1

    paths = sorted(root.rglob("*.html"))

    # Pass 1: the per-page repairs. Results are held in memory because the
    # security-meta pass needs a repaired page to copy from, and fix_head is
    # what makes the donor's metas readable in the first place.
    repaired: dict[Path, str] = {}
    changed = 0
    for path in paths:
        html = original = path.read_text(encoding="utf-8")
        for fn in PASSES:
            html = fn(html)
        repaired[path] = html
        if html != original:
            path.write_text(html, encoding="utf-8")
            changed += 1

    # Pass 2: propagate the shared head metas to pages generated outside
    # _layouts/. Ordered so a layout-rendered page is reached first.
    donor = harvest_shared_head_metas(
        [repaired[p] for p in sorted(paths, key=lambda p: len(p.parts))])
    if not donor:
        print("[postbuild] warning: no page carried the full set of security "
              "metas; none propagated", file=sys.stderr)

    secured = 0
    for path in paths:
        html = apply_shared_head_metas(repaired[path], donor)
        if html != repaired[path]:
            path.write_text(html, encoding="utf-8")
            repaired[path] = html
            secured += 1

    print(f"[postbuild] repaired {changed} of {len(paths)} page(s); "
          f"added shared head metas to {secured}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
