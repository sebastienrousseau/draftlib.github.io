#!/usr/bin/env python3
"""Content-integrity gate for draftlib.com.

Fails the build if the generated site contains markers of the obsolete
"Draft Lib" Rust product, a malformed double-scheme image URL, or a leftover
meta-keywords tag. Scans the built output (docs/ by default). See the
remediation plan, task 0.5.
"""
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCAN_DIR = os.path.join(ROOT, sys.argv[1] if len(sys.argv) > 1 else "docs")

# Substrings that must never appear in shipped HTML. Case-insensitive.
# (Note: "draft lib" as a product name is checked via word-boundary regex in
# BANNED_RE so it does not false-positive on "draft library".)
BANNED = [
    "astnode",
    "clausevalidator",
    "schemavalidator",
    "ast compiler",
    "ast synthesizer",
    "zero-copy lexer",
    "draftlib::",
    "rust crate",
    "type-safe ast",
]

# Regex checked against every scanned file (word-boundary so it does not fire
# on "draft library").
BANNED_RE_ALL = [
    (re.compile(r"\bdraft[ -]lib\b", re.I), "obsolete 'Draft Lib' product name"),
]

# Regex checked against HTML only.
BANNED_RE_HTML = [
    (re.compile(r"https?://[^\s\"'<>]*https?://"), "double-scheme URL"),
    (re.compile(r'<meta[^>]+name=["\']keywords["\']', re.I), "meta keywords tag"),
    (re.compile(r"cloudcdn\.pro/stocks/images/[a-z0-9-]+-1280\.webp"), "nonexistent -1280 image size"),
]

def main():
    if not os.path.isdir(SCAN_DIR):
        print(f"content check: no such directory {SCAN_DIR}", file=sys.stderr)
        return 1
    problems = []
    files = glob.glob(os.path.join(SCAN_DIR, "**", "*.html"), recursive=True)
    files += glob.glob(os.path.join(SCAN_DIR, "llms*.txt"))
    # machine-read surfaces: search index and agent/plugin manifests
    files += glob.glob(os.path.join(SCAN_DIR, "search-index.json"))
    files += glob.glob(os.path.join(SCAN_DIR, ".well-known", "*.json"))
    # the double-scheme URL pattern would false-positive on JSON escaping, so
    # only the banned-substring checks run against JSON (handled per-file below).
    for path in files:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        low = text.lower()
        rel = os.path.relpath(path, ROOT)
        for term in BANNED:
            if term in low:
                problems.append(f"{rel}: banned string {term!r}")
        for rx, label in BANNED_RE_ALL:
            if rx.search(text):
                problems.append(f"{rel}: {label}")
        if path.endswith(".json"):
            continue  # URL/meta checks are HTML-only
        for rx, label in BANNED_RE_HTML:
            if rx.search(text):
                problems.append(f"{rel}: {label}")
    if problems:
        print("Content-integrity gate FAILED:", file=sys.stderr)
        for p in sorted(set(problems)):
            print("  " + p, file=sys.stderr)
        print(f"\n{len(set(problems))} problem(s) across {len(files)} files.", file=sys.stderr)
        return 1
    print(f"content check: OK ({len(files)} files scanned, no banned content)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
