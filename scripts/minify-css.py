#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Sebastien Rousseau <sebastian.rousseau@gmail.com>
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Concatenate and minify stylesheets for the built site.

The sources are heavily commented, deliberately: half of brand.css is an
explanation of why a rule exists, and those explanations are worth more than the
bytes they cost in the repository. They are worth nothing over the wire, where
the stylesheet is on the critical path and the page cannot paint until it
arrives.

Conservative by design. It removes comments and collapses whitespace, and it
does not attempt to rewrite values, merge rules, or strip units — the kinds of
transformation that make a minifier fast and occasionally wrong. `calc(100% -
2rem)` needs its spaces; `a :hover` and `a:hover` are different selectors. What
is left is the change that is provably safe and recovers most of the bytes.

    python3 scripts/minify-css.py out.css in1.css in2.css
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

def strip_comments_and_hold_strings(css: str) -> tuple[str, list[str]]:
    """Walk the stylesheet once, removing comments and lifting out strings.

    A single pass, because two passes cannot agree on which comes first. Lifting
    strings out before removing comments treats an apostrophe in a comment as
    the start of one, and swallows everything up to the next apostrophe; the
    first version of this did exactly that and silently deleted 61 of the 83
    rules in playground.css. Removing comments first would instead mangle a
    string that happens to contain a comment marker.

    Scanning left to right decides it correctly: at any point the text is either
    inside a comment, inside a string, or neither, and only the third case is
    rewritten.
    """
    out: list[str] = []
    held: list[str] = []
    i, n = 0, len(css)

    while i < n:
        c = css[i]

        if c == "/" and css.startswith("/*", i):
            end = css.find("*/", i + 2)
            i = n if end == -1 else end + 2
            # A comment separates tokens, so it leaves a space behind it.
            out.append(" ")
            continue

        if c in "\"'":
            quote = c
            j = i + 1
            while j < n:
                if css[j] == "\\":
                    j += 2
                    continue
                if css[j] == quote:
                    j += 1
                    break
                j += 1
            held.append(css[i:j])
            out.append(f"\0{len(held) - 1}\0")
            i = j
            continue

        if css.startswith("url(", i):
            end = css.find(")", i)
            j = n if end == -1 else end + 1
            held.append(css[i:j])
            out.append(f"\0{len(held) - 1}\0")
            i = j
            continue

        out.append(c)
        i += 1

    return "".join(out), held


def minify(css: str) -> str:
    css, held = strip_comments_and_hold_strings(css)

    css = re.sub(r"\s+", " ", css)
    # Whitespace either side of these carries no meaning anywhere in CSS.
    css = re.sub(r"\s*([{};,])\s*", r"\1", css)
    # A trailing semicolon before a closing brace is redundant.
    css = css.replace(";}", "}")
    css = css.strip()

    return re.sub(r"\0(\d+)\0", lambda m: held[int(m.group(1))], css)


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: minify-css.py <out.css> <in.css>...", file=sys.stderr)
        return 2

    out = Path(sys.argv[1])
    parts, raw = [], 0
    for name in sys.argv[2:]:
        p = Path(name)
        if not p.is_file():
            print(f"no such stylesheet: {p}", file=sys.stderr)
            return 1
        text = p.read_text(encoding="utf-8")
        raw += len(text)
        small = minify(text)

        # A minifier that quietly drops rules is worse than none, because the
        # result still loads and still looks almost right. Counting blocks
        # either side is a cheap proof that nothing was lost: the first version
        # of this deleted 61 of 83 rules and the only visible symptom was a
        # suspiciously good compression ratio.
        before, after = text.count("{"), small.count("{")
        if before != after:
            print(f"{p}: {before} rule blocks in, {after} out — refusing to write",
                  file=sys.stderr)
            return 1
        if small.count("{") != small.count("}"):
            print(f"{p}: unbalanced braces after minifying", file=sys.stderr)
            return 1

        parts.append(small)

    # Order is preserved, and it matters: brand.css overrides the design system
    # and is unlayered, so it has to follow it.
    result = "\n".join(parts)
    out.write_text(result, encoding="utf-8")

    saved = 100 - round(100 * len(result) / raw) if raw else 0
    print(f"css: {raw} -> {len(result)} bytes ({saved}% smaller) -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
