#!/usr/bin/env python3
"""Split markdown into small Docusaurus doc pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"


def slugify(text: str) -> str:
    text = re.sub(r"^\d+\.\s*", "", text)
    text = re.sub(r"[«»]", "", text)
    text = re.sub(r"[^\w\s\u0600-\u06FF-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    return text[:72] or "page"


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3 :].lstrip("\n")
    return text


def yaml_quote(s: str) -> str:
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def write_page(out_dir: Path, idx: int, title: str, body: str, description: str = "") -> str:
    slug = slugify(title)
    filename = f"{idx:02d}-{slug}.md"
    desc = description or title[:120]
    content = (
        f"---\ntitle: {yaml_quote(title)}\ndescription: {yaml_quote(desc)}\n---\n\n"
        f"# {title}\n\n{body.strip()}\n"
    )
    (out_dir / filename).write_text(content, encoding="utf-8")
    return filename.replace(".md", "")


def split_on_h1(source: Path, out_dir: Path) -> list[str]:
    text = strip_frontmatter(source.read_text(encoding="utf-8"))
    parts = re.split(r"(?m)^# ", text)
    created: list[str] = []
    out_dir.mkdir(parents=True, exist_ok=True)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        lines = part.splitlines()
        title = lines[0].strip()
        body = "\n".join(lines[1:])
        if "Report" in title and title.startswith("Nginx Phase"):
            continue
        created.append(write_page(out_dir, len(created) + 1, title, body))
    return created


def split_on_h2(source: Path, out_dir: Path, skip_title: str | None = None) -> list[str]:
    text = strip_frontmatter(source.read_text(encoding="utf-8"))
    text = re.sub(r"(?m)^# .+\n+", "", text, count=1)
    parts = re.split(r"(?m)^## ", text)
    created: list[str] = []
    out_dir.mkdir(parents=True, exist_ok=True)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        lines = part.splitlines()
        title = lines[0].strip()
        if skip_title and title == skip_title:
            continue
        # skip intro preamble before first real section
        if not created and not re.match(r"^\d+\.", title) and title not in ("خلاصه", "Summary", "Basic Usage"):
            continue
        body = "\n".join(lines[1:])
        created.append(write_page(out_dir, len(created) + 1, title, body))
    return created


def main() -> None:
    jobs_h1 = [
        (CONTENT / "nginx" / "phase1.md", CONTENT / "nginx" / "01-basics"),
        (CONTENT / "nginx" / "phase2.md", CONTENT / "nginx" / "02-production"),
        (CONTENT / "nginx" / "phase3-network.md", CONTENT / "nginx" / "03-systems"),
    ]
    jobs_h2 = [
        (CONTENT / "linux" / "linux.md", CONTENT / "linux" / "01-shell"),
        (CONTENT / "linux" / "grep.md", CONTENT / "linux" / "02-grep"),
        (CONTENT / "git" / "rebase-fast-forward.md", CONTENT / "git" / "01-pull-merge"),
        (CONTENT / "git" / "head-guide.md", CONTENT / "git" / "02-head"),
        (CONTENT / "git" / "rebase-questions.md", CONTENT / "git" / "03-scenarios", "خلاصه"),
    ]

    for src, dst in jobs_h1:
        if src.exists():
            n = len(split_on_h1(src, dst))
            print(f"H1 {src.name} -> {dst.relative_to(ROOT)} ({n} pages)")

    for item in jobs_h2:
        src, dst = item[0], item[1]
        skip = item[2] if len(item) > 2 else None
        if src.exists():
            n = len(split_on_h2(src, dst, skip))
            print(f"H2 {src.name} -> {dst.relative_to(ROOT)} ({n} pages)")


if __name__ == "__main__":
    main()
