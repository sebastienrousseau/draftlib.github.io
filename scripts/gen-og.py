#!/usr/bin/env python3
"""Generate a branded Open Graph card (1200x630 PNG) per page and wire it in.

For each _posts/*.md it renders og/<slug>.png from the page's eyebrow, headline
and description, and ensures the page's frontmatter carries `og_card: <slug>`
so base.html can point og:image / twitter:image at it. Run manually (needs
ImageMagick + a system font); og/ is committed as static assets. Not part of
`make build`, which runs in CI without these fonts. See audit item 1.3.
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
POSTS = os.path.join(ROOT, "_posts")
OGDIR = os.path.join(ROOT, "og")
FONT = "/System/Library/Fonts/HelveticaNeue.ttc"
BG = "#0b0e14"
CORAL = "#f56b5e"
FG = "#f8fafc"
MUTED = "#93a1b5"


def parse_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return None, None, None
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r'^([A-Za-z0-9_]+):\s*"?(.*?)"?\s*$', line)
        if mm:
            fm[mm.group(1)] = mm.group(2)
    return fm, m.group(1), m.group(2)


def slug_of(fm, path):
    perm = fm.get("permalink", "")
    s = re.sub(r"^https?://[^/]+/", "", perm).strip("/")
    if not s or s == "":
        return "home"
    return s.replace("/", "-")


def trim(s, n):
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0] + "…"


def render(slug, eyebrow, headline, desc):
    out = os.path.join(OGDIR, slug + ".png")
    eyebrow = (eyebrow or "draft").lower()
    cmd = [
        "magick", "-size", "1200x630", "xc:" + BG,
        "-fill", CORAL, "-draw", "rectangle 0,0 1200,10",
        "(", "-background", "none", "-fill", CORAL, "-font", FONT, "-weight", "800",
        "-pointsize", "34", "label:draft  ·  " + eyebrow, ")",
        "-gravity", "NorthWest", "-geometry", "+80+72", "-composite",
        "(", "-background", "none", "-fill", FG, "-font", FONT, "-weight", "800",
        "-size", "1040x", "-pointsize", "80", "caption:" + trim(headline, 70), ")",
        "-gravity", "NorthWest", "-geometry", "+80+180", "-composite",
        "(", "-background", "none", "-fill", MUTED, "-font", FONT,
        "-size", "1040x", "-pointsize", "33", "caption:" + trim(desc, 150), ")",
        "-gravity", "SouthWest", "-geometry", "+80+120", "-composite",
        "(", "-background", "none", "-fill", MUTED, "-font", FONT,
        "-pointsize", "27", "label:draftlib.com", ")",
        "-gravity", "SouthWest", "-geometry", "+80+56", "-composite",
        out,
    ]
    subprocess.run(cmd, check=True)
    return out


def ensure_og_card(path, raw_fm, slug):
    text = open(path, encoding="utf-8").read()
    if re.search(r"^og_card:", raw_fm, re.M):
        return
    text = re.sub(r"(^layout:.*$)", lambda m: m.group(1) + f'\nog_card: "{slug}"',
                  text, count=1, flags=re.M)
    open(path, "w", encoding="utf-8").write(text)


def main():
    os.makedirs(OGDIR, exist_ok=True)
    n = 0
    for path in sorted(glob.glob(os.path.join(POSTS, "*.md"))):
        fm, raw_fm, _ = parse_fm(open(path, encoding="utf-8").read())
        if not fm or not fm.get("headline"):
            continue
        slug = slug_of(fm, path)
        render(slug, fm.get("eyebrow"), fm["headline"],
               fm.get("lead") or fm.get("description") or "")
        ensure_og_card(path, raw_fm, slug)
        n += 1
        print(f"  og/{slug}.png  <- {os.path.basename(path)}")
    print(f"generated {n} OG cards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
