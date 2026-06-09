#!/usr/bin/env python3
"""Prepare clean markdown sources for mdBook (strip ebook HTML wrappers)."""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SRC = ROOT / "src"

SOURCES = [
    ("introduction.md", "introduction.md", True),
    ("nginx/phase1.md", "nginx/phase1.md", True),
    ("nginx/phase2.md", "nginx/phase2.md", True),
    ("nginx/phase3-network.md", "nginx/phase3-network.md", True),
    ("linux/linux.md", "linux/linux.md", True),
    ("linux/grep.md", "linux/grep.md", False),
    ("git/rebase-fast-forward.md", "git/rebase-fast-forward.md", True),
    ("git/head-guide.md", "git/head-guide.md", True),
    ("git/rebase-questions.md", "git/rebase-questions.md", True),
]

NAV_RE = re.compile(
    r'\n<div align="center">\s*\n(?:\[.+?\]\(.+?\)\s*(?:·\s*)?)+\n\n</div>\s*',
    re.M,
)
BROKEN_NAV_DIV_RE = re.compile(
    r'\n<div align="center">\s*\n.*?(?=\n---\s*\n|\n## |\Z)',
    re.S,
)
ORPHAN_DIV_CLOSE_RE = re.compile(r"\n</div>\s*", re.M)
DETAILS_TOC_RE = re.compile(
    r"<details>\s*\n<summary><strong>📑[^<]*</strong>[^<]*</summary>\s*\n(?:.*?\n)*?</details>\s*\n?",
    re.S,
)
OUTER_DIV_RE = re.compile(
    r'^<div\s+dir="(?:rtl|ltr)"\s+align="(?:right|left)"\s*>\s*\n?',
    re.M,
)
CLOSING_DIV_RE = re.compile(r"\n?</div>\s*$", re.M)
DETAILS_BLOCK_RE = re.compile(
    r"<details>\s*\n<summary>.*?</summary>\s*\n(.*?)\n</details>",
    re.S,
)
SUMMARY_ONLY_RE = re.compile(r"<summary>.*?</summary>\s*\n?", re.S)
GITHUB_TOC_RE = re.compile(
    r"## فهرست[^\n]*\n\n(?:\|[^\n]+\n)+(?:\|[^\n]+\n)+",
    re.M,
)
ORPHAN_TOC_TABLE_RE = re.compile(
    r"\n---\s*\n\n\| # \| (?:بخش|Section|سناریو|کتاب / فصل)[^\n]*\n"
    r"\| ---[^\n]+\n(?:\|[^\n]+\n)+(?:\n\[(?:↑[^\]]+|↑ Top)\]\([^\)]+\))?\s*",
    re.M,
)
TOP_LINK_RE = re.compile(r"\n\[(?:↑[^\]]+|↑ Top)\]\([^\)]+\)\s*", re.M)


def unwrap_details(content: str) -> str:
    while True:
        updated = DETAILS_BLOCK_RE.sub(r"\1", content)
        if updated == content:
            break
        content = updated
    return content


def strip_ebook_html(content: str) -> str:
    content = OUTER_DIV_RE.sub("", content)
    content = CLOSING_DIV_RE.sub("", content)
    content = DETAILS_TOC_RE.sub("", content)
    content = GITHUB_TOC_RE.sub("", content)
    content = ORPHAN_TOC_TABLE_RE.sub("\n---\n\n", content)
    content = TOP_LINK_RE.sub("\n", content)
    content = unwrap_details(content)
    content = SUMMARY_ONLY_RE.sub("", content)
    content = NAV_RE.sub("\n", content)
    content = BROKEN_NAV_DIV_RE.sub("\n---\n\n", content)
    content = ORPHAN_DIV_CLOSE_RE.sub("\n", content)
    content = re.sub(r"\n---\s*\n---\s*\n", "\n---\n\n", content)
    content = re.sub(r"\n{3,}", "\n\n", content)
    return content.strip() + "\n"


def prepare_file(source: Path, dest: Path, rtl: bool) -> None:
    raw = source.read_text(encoding="utf-8")
    clean = strip_ebook_html(raw)
    if not rtl:
        clean = f'<div class="page-ltr">\n\n{clean}\n\n</div>\n'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(clean, encoding="utf-8")


def clean_content_sources() -> None:
    """Remove ebook HTML wrappers and leftover TOC tables from content markdown."""
    for source_rel, _, _ in SOURCES:
        source = CONTENT / source_rel
        if not source.exists():
            continue
        raw = source.read_text(encoding="utf-8")
        clean = strip_ebook_html(raw)
        if clean != raw:
            source.write_text(clean, encoding="utf-8")
            print(f"cleaned: content/{source_rel}")


def copy_assets() -> None:
    assets_src = ROOT / "assets"
    assets_dest = SRC / "assets"
    if assets_src.exists():
        if assets_dest.exists():
            shutil.rmtree(assets_dest)
        shutil.copytree(assets_src, assets_dest)


def write_summary() -> None:
    summary = """# Summary

- [مقدمه](introduction.md)

# Nginx

- [فاز ۱: پایه عملی](nginx/phase1.md)
- [فاز ۲: Production Operations](nginx/phase2.md)
- [فاز ۳: شبکه و سیستم‌عامل](nginx/phase3-network.md)

# Linux

- [Linux برای توسعه‌دهنده](linux/linux.md)
- [grep](linux/grep.md)

# Git

- [Git Pull، Fast-Forward، Merge و Rebase](git/rebase-fast-forward.md)
- [HEAD در Git](git/head-guide.md)
- [سؤالات Git (Pull / Rebase)](git/rebase-questions.md)
"""
    (SRC / "SUMMARY.md").write_text(summary, encoding="utf-8")


def main() -> None:
    clean_content_sources()

    for source_rel, dest_rel, rtl in SOURCES:
        source = CONTENT / source_rel
        dest = SRC / dest_rel
        if not source.exists():
            print(f"skip missing: content/{source_rel}")
            continue
        prepare_file(source, dest, rtl)
        print(f"prepared: {dest_rel}")

    copy_assets()
    write_summary()
    print("wrote: src/SUMMARY.md")


if __name__ == "__main__":
    main()
