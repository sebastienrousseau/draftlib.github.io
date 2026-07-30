#!/usr/bin/env bash
set -euo pipefail

# Render scripts/og-card.html to static/img/og-card.png at exactly 1200x630.
#
# The PNG is committed, so this is only run when the card is redrawn — it is
# deliberately NOT part of build.sh, which must work on a machine (or a CI
# runner) with no browser installed.
#
# Chrome is the renderer rather than ImageMagick because the mark uses an SVG
# mask and a gradient, and the card uses a self-hosted woff2 face; a browser
# is the only thing here that renders all three faithfully.
#
# Usage: ./scripts/make-og-card.sh

cd "$(git rev-parse --show-toplevel)"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[[ -x "$CHROME" ]] || {
  echo "Google Chrome not found at: $CHROME" >&2
  exit 1
}

OUT="static/img/og-card.png"
TMPDIR_RENDER="$(mktemp -d)"
trap 'rm -rf "$TMPDIR_RENDER"' EXIT

"$CHROME" \
  --headless \
  --disable-gpu \
  --hide-scrollbars \
  --force-device-scale-factor=1 \
  --default-background-color=00000000 \
  --window-size=1200,630 \
  --screenshot="$TMPDIR_RENDER/og-card.png" \
  --user-data-dir="$TMPDIR_RENDER/profile" \
  "file://$(pwd)/scripts/og-card.html" >/dev/null 2>&1

[[ -s "$TMPDIR_RENDER/og-card.png" ]] || {
  echo "Chrome produced no screenshot" >&2
  exit 1
}

mkdir -p "$(dirname "$OUT")"
cp "$TMPDIR_RENDER/og-card.png" "$OUT"

# Fail loudly rather than shipping a card at the wrong size — a mismatch
# between the real pixels and the declared og:image:width/height is exactly
# the bug this card was added to fix.
read -r W H < <(python3 -c "
import struct, sys
d = open('$OUT','rb').read(33)
w, h = struct.unpack('>II', d[16:24])
print(w, h)
")
if [[ "$W" != "1200" || "$H" != "630" ]]; then
  echo "rendered ${W}x${H}, expected 1200x630" >&2
  exit 1
fi

echo "Wrote $OUT (${W}x${H})."
