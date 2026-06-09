#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MDBOOK="${ROOT}/.bin/mdbook"

cd "$ROOT"
python3 scripts/prepare-mdbook.py
"$MDBOOK" build
mkdir -p book/theme/fonts
cp -f theme/fonts/*.woff2 book/theme/fonts/

echo ""
echo "Book built → ${ROOT}/book/index.html"
echo "Open: file://${ROOT}/book/index.html"
