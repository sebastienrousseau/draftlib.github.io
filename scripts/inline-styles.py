#!/usr/bin/env python3
"""Inline styles.css into each layout as a plain <style> block.

ssg publishes CSS only when it appears inline in a <style> block: its CSP
plugin extracts the block to /_csp/<hash>.css with Subresource Integrity and
rewrites the link. An external <link href="/styles.css"> is never published,
so the site loads unstyled. This inlines styles.css between HTML-comment
markers so the block is a plain <style> ssg will extract, yet stays
regenerable: edit styles.css, then re-run this script.
"""
import pathlib, re

BEGIN = "<!-- styles.css:begin -->"
END = "<!-- styles.css:end -->"
LINK = '<link rel="stylesheet" href="/styles.css">'
BLOCK_RE = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)


def main() -> None:
    css = pathlib.Path("styles.css").read_text().strip()
    block = BEGIN + "\n<style>\n" + css + "\n</style>\n" + END
    changed = 0
    for f in sorted(pathlib.Path("_layouts").glob("*.html")):
        s = f.read_text()
        if BLOCK_RE.search(s):
            new = BLOCK_RE.sub(lambda _: block, s)
        elif LINK in s:
            new = s.replace(LINK, block)
        else:
            continue
        if new != s:
            f.write_text(new)
            changed += 1
    print(f"inlined styles.css into {changed} layout(s)")


if __name__ == "__main__":
    main()
