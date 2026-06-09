#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MDBOOK="${ROOT}/.bin/mdbook"

cd "$ROOT"
python3 scripts/prepare-mdbook.py
"$MDBOOK" build

echo ""
echo "Book built → ${ROOT}/book/index.html"
echo "Open: file://${ROOT}/book/index.html"
