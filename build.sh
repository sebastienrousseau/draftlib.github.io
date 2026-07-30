#!/usr/bin/env bash
set -euo pipefail

# Build draftlib.com with Shokunin SSG, then publish the result to docs/
# (GitHub Pages serves from docs/ on the default branch).
#
#   1. `ssg build -f ssg.toml` compiles _posts/ + _layouts/ into ./Draftlib
#      (ssg names the final directory after site_name, which also feeds the
#      JSON-LD publisher and llms.txt title — hence "Draftlib", not "docs").
#   2. The CNAME ssg emits is a DNS zone record; GitHub Pages requires the
#      bare apex domain, so it is rewritten.
#   3. static/ is mirrored over the output, then ./Draftlib is synced into
#      ./docs and the staging directories are removed.
#
# Usage: ./build.sh          (build + publish to docs/)
#        ./build.sh --audit  (build, publish, then run the ssg audit gates)

cd "$(git rev-parse --show-toplevel)"

AUDIT=0
[[ "${1:-}" == "--audit" ]] && AUDIT=1

command -v ssg >/dev/null || {
  echo "ssg not found on PATH. Install Shokunin: cargo install ssg" >&2
  exit 1
}

rm -rf output Draftlib

ssg build -f ssg.toml

# GitHub Pages custom-domain file must contain exactly the apex domain.
printf 'draftlib.com\n' > Draftlib/CNAME

# GitHub Pages runs Jekyll by default, and Jekyll drops underscore-prefixed
# paths — which would 404 any asset served from one. Opt out entirely.
touch Draftlib/.nojekyll

# Repair the ssg output: unescape entity-escaped head metas (otherwise every
# page renders its <meta> tags as visible text), drop the duplicate metas ssg
# synthesises, and unwrap the highlighter's inline-styled code blocks that the
# strict CSP would otherwise blank out. See scripts/postbuild_fix.py.
python3 scripts/postbuild_fix.py Draftlib

# Static assets that mirror the site root: self-hosted fonts (no third-party
# requests, so the CSP needs no carve-outs), the brand mark, and the shared
# stylesheet.
rsync -a static/ Draftlib/

# Publish: replace docs/ content with the fresh build (keep the dir itself).
mkdir -p docs
rsync -a --delete --exclude '.ssg-cache' Draftlib/ docs/

rm -rf output Draftlib

if [[ "$AUDIT" == "1" ]]; then
  ssg audit -f ssg.toml -o docs --severity warn
fi

echo "Build published to docs/."
