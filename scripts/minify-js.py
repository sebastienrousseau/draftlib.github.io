#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Sebastien Rousseau <sebastian.rousseau@gmail.com>
# SPDX-License-Identifier: Apache-2.0 OR MIT
"""Strip comments and indentation from the site's own JavaScript.

The sources are heavily commented on purpose — terminal.js opens with thirty
lines explaining why a command types and its output does not — and those
explanations earn their place in the repository. They earn nothing over the
wire. terminal.js is the one script the pages load without `defer`, because
deferring it lets a shell block paint as a plain `<pre>` and then become a
terminal, which measured a layout shift of 0.064. So it sits on the critical
path, and two thirds of what it costs there is prose.

Conservative in the same way minify-css.py is. It removes comments, strips the
whitespace at each end of a line, and drops blank lines. It does not rename
anything, collapse statements onto one line, or remove a semicolon it thinks is
redundant — the transformations that make a minifier impressive and sometimes
wrong. Newlines survive exactly where they were, so automatic semicolon
insertion cannot land anywhere new.

Recognising a regular expression is the part worth being careful about. A `/`
starts one or divides, depending on what came before it, and getting that
backwards turns the rest of the file into a literal. The rule used here is the
usual one: after a value — an identifier, a number, a closing bracket — a slash
divides; anywhere else it opens a pattern. A quote inside a pattern would then
be read as opening a string, so the scanner refuses the file instead of
guessing, and no script in this repository contains one.

Whether the result still parses is checked separately, by `make web`, over
everything the build emits. Keeping that out of here matters: a check that
decides what to write makes the output depend on which tools the machine
happens to have, and the deployed bytes would stop matching a local build.
This script's output depends on its input and nothing else.

    python3 scripts/minify-js.py in.js out.js
"""

from __future__ import annotations

import sys
from pathlib import Path

# After one of these a slash is division, not the start of a pattern. Keywords
# are the exception that makes the "last character" test insufficient on its
# own: `return /x/` and `typeof /x/` both end in a letter.
VALUE_END = set("})]") | set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_$")

KEYWORDS_BEFORE_REGEX = {
    "return", "typeof", "instanceof", "in", "of", "new", "delete", "void",
    "throw", "case", "do", "else", "yield", "await",
}


class Unsupported(Exception):
    """The file uses something this minifier will not guess at."""


def scan(src: str) -> str:
    """Walk the source once, dropping comments and copying everything else.

    One pass, for the reason minify-css.py takes one: at any point the text is
    inside a string, a template, a pattern, a comment, or none of those, and
    only the last case may be rewritten. Deciding that in two passes means each
    pass has to guess what the other did.
    """
    out: list[str] = []
    i, n = 0, len(src)

    def previous_token() -> str:
        """The last thing emitted, ignoring whitespace — enough to tell a
        pattern from a division."""
        j = len(out) - 1
        while j >= 0 and out[j].isspace():
            j -= 1
        if j < 0:
            return ""
        # A bracket or operator is a token in itself. Falling through to the
        # identifier walk below would return nothing for it, and nothing reads
        # as "not after a value", which turns the division in `(a + b) / 2`
        # into the opening of a pattern and swallows the rest of the line.
        if not (out[j].isalnum() or out[j] in "_$"):
            return out[j]
        # Walk back over an identifier so a keyword can be recognised whole.
        end = j
        while j >= 0 and (out[j].isalnum() or out[j] in "_$"):
            j -= 1
        return "".join(out[j + 1:end + 1])

    while i < n:
        c = src[i]

        # Strings and templates are copied verbatim. A template may contain
        # newlines that are part of its value, so nothing inside is touched.
        if c in "\"'`":
            quote = c
            j = i + 1
            while j < n:
                if src[j] == "\\":
                    j += 2
                    continue
                if src[j] == quote:
                    j += 1
                    break
                j += 1
            else:
                raise Unsupported("a string is never closed")
            out.append(src[i:j])
            i = j
            continue

        if src.startswith("//", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
            continue

        if src.startswith("/*", i):
            j = src.find("*/", i + 2)
            if j < 0:
                raise Unsupported("a block comment is never closed")
            i = j + 2
            continue

        if c == "/":
            prev = previous_token()
            divides = bool(prev) and (prev[-1] in VALUE_END and prev not in KEYWORDS_BEFORE_REGEX)
            if not divides:
                j = i + 1
                in_class = False
                while j < n:
                    ch = src[j]
                    if ch == "\\":
                        j += 2
                        continue
                    if ch == "\n":
                        raise Unsupported("a pattern appears to span a line")
                    if ch in "\"'`" and not in_class:
                        raise Unsupported(
                            "a quote inside a pattern: refusing rather than "
                            "reading it as a string")
                    if ch == "[":
                        in_class = True
                    elif ch == "]":
                        in_class = False
                    elif ch == "/" and not in_class:
                        j += 1
                        break
                    j += 1
                else:
                    raise Unsupported("a pattern is never closed")
                while j < n and src[j].isalpha():   # flags
                    j += 1
                out.append(src[i:j])
                i = j
                continue

        out.append(c)
        i += 1

    return "".join(out)


def minify(src: str) -> str:
    body = scan(src)
    lines = [ln.strip() for ln in body.split("\n")]
    return "\n".join(ln for ln in lines if ln) + "\n"


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: minify-js.py in.js out.js", file=sys.stderr)
        return 2

    src_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
    src = src_path.read_text(encoding="utf-8")

    try:
        result = minify(src)
    except Unsupported as exc:
        # Shipping the file unchanged is always correct; shipping a guess is
        # not. A script that silently stopped working would show up as a page
        # that quietly does less, which is the worst way to find out.
        print(f"minify-js: {src_path.name} left as it is — {exc}", file=sys.stderr)
        out_path.write_text(src, encoding="utf-8")
        return 0

    out_path.write_text(result, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
