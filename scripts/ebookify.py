#!/usr/bin/env python3
"""Transform markdown files into navigable ebook format with TOC and collapsible sections."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PERSIAN_RE = re.compile(r"[\u0600-\u06FF]")
ALREADY_EBOOK_RE = re.compile(r"^<div\s+dir=", re.M)
PHASE_FILE_RE = re.compile(r"phase|pahse", re.I)


def is_persian(text: str) -> bool:
    return bool(PERSIAN_RE.search(text))


def clean_title(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"[*_]", "", text)
    return text.strip()


def slugify(text: str) -> str:
    text = clean_title(text)
    text = text.lower()
    text = re.sub(r"[^\w\s\u0600-\u06FF-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text


def is_phase_file(path: Path) -> bool:
    return bool(PHASE_FILE_RE.search(path.name))


def choose_wrap_level(content: str, path: Path) -> int:
    if is_phase_file(path):
        return 1
    h1 = len(re.findall(r"^# [^#]", content, re.M))
    h2 = len(re.findall(r"^## [^#]", content, re.M))
    if h2 >= max(h1, 3):
        return 2
    if h1 >= 3:
        return 1
    return 2


def split_sections(content: str, level: int) -> tuple[str, list[dict]]:
    pattern = rf"^(#{{{level}}})\s+(.+)$"
    lines = content.split("\n")
    preamble: list[str] = []
    sections: list[dict] = []
    current: dict | None = None
    in_preamble = True

    for line in lines:
        match = re.match(pattern, line)
        if match:
            in_preamble = False
            if current is not None:
                sections.append(current)
            current = {
                "title": match.group(2).strip(),
                "header_line": line,
                "body": [],
            }
        elif in_preamble:
            preamble.append(line)
        elif current is not None:
            current["body"].append(line)
        else:
            preamble.append(line)

    if current is not None:
        sections.append(current)

    return "\n".join(preamble).strip(), sections


def normalize_preamble(preamble: str, doc_title: str) -> str:
    lines = preamble.split("\n")
    title_clean = clean_title(doc_title)
    filtered: list[str] = []
    seen_title = False

    for line in lines:
        if re.match(r"^#\s+", line):
            heading = clean_title(re.sub(r"^#+\s*", "", line))
            if heading == title_clean:
                if seen_title:
                    continue
                seen_title = True
                continue
        filtered.append(line)

    text = "\n".join(filtered).strip()
    text = re.sub(r"\n---\s*$", "", text).strip()
    return text


def nav_labels(persian: bool) -> dict[str, str]:
    if persian:
        return {
            "toc": "📑 فهرست مطالب",
            "toc_hint": "کلیک برای باز / بسته کردن",
            "prev": "← قبلی",
            "next": "بعدی →",
            "top": "↑ بالا",
            "section": "بخش",
            "scenario": "سناریو",
        }
    return {
        "toc": "📑 Table of Contents",
        "toc_hint": "click to expand / collapse",
        "prev": "← Previous",
        "next": "Next →",
        "top": "↑ Top",
        "section": "Section",
        "scenario": "Scenario",
    }


def build_toc(
    sections: list[dict],
    labels: dict[str, str],
    title_slug: str,
    column_header: str | None = None,
) -> str:
    col = column_header or labels["section"]
    rows = []
    for idx, section in enumerate(sections, 1):
        title = clean_title(section["title"])
        anchor = slugify(section["title"])
        rows.append(f"| {idx} | [{title}](#{anchor}) |")

    return "\n".join(
        [
            "<details>",
            f"<summary><strong>{labels['toc']}</strong> — <em>{labels['toc_hint']}</em></summary>",
            "",
            f"| # | {col} |",
            "| ---: | --- |",
            *rows,
            "",
            f"[{labels['top']}](#{title_slug})",
            "",
            "</details>",
        ]
    )


def section_nav(
    idx: int,
    total: int,
    sections: list[dict],
    title_slug: str,
    labels: dict[str, str],
) -> str:
    links = [f"[{labels['top']}](#{title_slug})"]
    if idx > 0:
        prev_anchor = slugify(sections[idx - 1]["title"])
        links.append(f"[{labels['prev']}](#{prev_anchor})")
    if idx < total - 1:
        next_anchor = slugify(sections[idx + 1]["title"])
        links.append(f"[{labels['next']}](#{next_anchor})")
    return f"\n<div align=\"center\">\n\n{' · '.join(links)}\n\n</div>\n"


def wrap_section_body(body: str, title: str, collapsible: bool) -> str:
    body = body.strip()
    if not body:
        return ""
    if not collapsible:
        return f"\n{body}\n"
    summary = clean_title(title)
    return f"\n<details>\n<summary>{summary}</summary>\n\n{body}\n\n</details>\n"


def extract_doc_title(content: str, sections: list[dict]) -> str:
    match = re.search(r"^#\s+(.+)$", content, re.M)
    if match:
        return clean_title(match.group(1))
    if sections:
        return clean_title(sections[0]["title"])
    return "document"


def transform_fresh(content: str, path: Path) -> str:
    persian = is_persian(content)
    labels = nav_labels(persian)
    dir_attr = "rtl" if persian else "ltr"
    align_attr = "right" if persian else "left"

    wrap_level = choose_wrap_level(content, path)
    preamble, sections = split_sections(content, wrap_level)
    if not sections:
        return content

    doc_title = extract_doc_title(content, sections)
    title_slug = slugify(doc_title)
    intro = normalize_preamble(preamble, doc_title)

    work_sections = sections
    if wrap_level == 1 and sections:
        first = clean_title(sections[0]["title"])
        if first == doc_title:
            merged = "\n".join(sections[0]["body"]).strip()
            merged = re.sub(r"\n---\s*$", "", merged).strip()
            intro = (intro + "\n\n" + merged).strip() if merged else intro
            work_sections = sections[1:]

    intro = re.sub(r"\n---\s*$", "", intro).strip()

    collapsible = len(work_sections) >= 2
    toc = build_toc(work_sections, labels, title_slug) if collapsible else ""

    out: list[str] = [
        f'<div dir="{dir_attr}" align="{align_attr}">',
        "",
        f"# {doc_title}",
        "",
    ]

    if intro:
        out.append(intro)
        out.append("")

    if toc:
        if not out or out[-1] != "---":
            out.extend(["---", ""])
        out.extend([toc, "", "---", ""])

    total = len(work_sections)
    for idx, section in enumerate(work_sections):
        out.append(section["header_line"])
        out.append(wrap_section_body("\n".join(section["body"]), section["title"], collapsible))
        if collapsible and total > 1:
            out.append(section_nav(idx, total, work_sections, title_slug, labels))
        out.append("")
        out.append("---")
        out.append("")

    while out and out[-1] in ("", "---"):
        out.pop()

    out.extend(["", "</div>"])
    return "\n".join(out) + "\n"


def enhance_existing(content: str, path: Path) -> str:
    """Enhance pre-formatted ebook files (scenario Q&A)."""
    if "📑 فهرست مطالب" in content and 'align="center"' in content:
        return content

    persian = is_persian(content)
    labels = nav_labels(persian)
    doc_title = extract_doc_title(content, [])
    title_slug = slugify(doc_title)

    toc_block = re.search(
        r"## فهرست[^\n]*\n\n(\| # \|[^\n]+\n\| ---[^\n]+\n(?:\|[^\n]+\n)+)",
        content,
    )
    if toc_block:
        table = toc_block.group(1).strip()
        wrapped_toc = "\n".join(
            [
                "<details>",
                f"<summary><strong>{labels['toc']}</strong> — <em>{labels['toc_hint']}</em></summary>",
                "",
                table,
                "",
                f"[{labels['top']}](#{title_slug})",
                "",
                "</details>",
            ]
        )
        content = content.replace(
            re.search(r"## فهرست[^\n]*\n\n(?:\|[^\n]+\n)+", content).group(0),
            wrapped_toc,
        )

    scenario_pattern = re.compile(
        r"^(## \d+\. سناریو:.+?)\n(<details>.*?</details>)",
        re.S | re.M,
    )
    matches = list(scenario_pattern.finditer(content))
    if not matches:
        return content

    sections = [{"title": m.group(1).lstrip("# ").strip()} for m in matches]
    total = len(sections)

    for idx, match in enumerate(matches):
        nav = section_nav(idx, total, sections, title_slug, labels).strip()
        original = match.group(0)
        if nav in content:
            continue
        content = content.replace(original, f"{original}\n{nav}", 1)

    return content


def transform(content: str, path: Path) -> str:
    if ALREADY_EBOOK_RE.search(content):
        return enhance_existing(content, path)
    return transform_fresh(content, path)


def build_readme_index() -> str:
  labels = nav_labels(True)
  books = [
      ("README.md", "مسیر مطالعه Nginx", "صفحه اصلی و نقشه راه"),
      ("phase1.md", "فاز ۱: پایه عملی Nginx", "۲–۳ هفته — reverse proxy، static، HTTPS"),
      ("pahse2.md", "فاز ۲: Production Operations", "۴–۶ هفته — timeout، cache، rate limit"),
      ("phase3%20-%20Network.md", "فاز ۳: شبکه و سیستم‌عامل", "۲–۳ ماه — TCP، epoll، performance"),
      ("linux.md", "آنچه از لینوکس باید بدانم", "راهنمای فول‌استک دولوپر"),
      ("linux/grep.md", "grep Command Usage", "جستجوی متن در فایل‌ها"),
      ("git/git-rebase-fast-forward.md", "Git Pull و Fast-Forward", "merge، rebase، ff-only"),
      ("git/git-head-guide.md", "HEAD در Git", "HEAD~1، detached HEAD، reset"),
      (
          "git/git-rebase-fast-forward-questions.md",
          "سؤالات سناریومحور Git",
          "۲۰ سناریو با جواب",
      ),
  ]

  rows = []
  for idx, (href, title, desc) in enumerate(books, 1):
      if href == "README.md":
          rows.append(f"| {idx} | **{title}** | {desc} |")
      else:
          rows.append(f"| {idx} | [{title}]({href}) | {desc} |")

  return f"""<div dir="rtl" align="right">

# مسیر مطالعه Nginx در سطح دکترای کامپیوتر

اگر می‌خواهی Nginx را در سطح بسیار عمیق و نزدیک به نگاه یک دکترای کامپیوتر بخوانی، نباید آن را فقط به‌عنوان یک وب‌سرور یا ابزار reverse proxy ببینی. باید Nginx را به‌عنوان یک نمونه واقعی از سیستم‌های high-performance، event-driven، network server و production infrastructure مطالعه کنی.

<details>
<summary><strong>{labels['toc']}</strong> — <em>{labels['toc_hint']}</em></summary>

| # | کتاب / فصل | توضیح |
| ---: | --- | --- |
{chr(10).join(rows)}

</details>

---

## ساختار مطالعه

مسیر درست مطالعه شامل سه لایه اصلی است:

1. استفاده عملی و Production Configuration
2. معماری داخلی، سورس‌کد و module system
3. مفاهیم علمی پشت آن: سیستم‌عامل، شبکه، concurrency، performance، caching، security و distributed systems

---

## مدت زمان پیشنهادی

| سطح هدف                       | مدت زمان واقع‌بینانه |
| ----------------------------- | -------------------: |
| استفاده حرفه‌ای در پروژه‌ها   |           ۱ تا ۲ ماه |
| سطح Production / DevOps قوی   |           ۳ تا ۶ ماه |
| درک عمیق معماری و Performance |          ۶ تا ۱۲ ماه |
| سطح پژوهشی / PhD-like         |         ۱۲ تا ۱۸ ماه |

---

## فازهای Nginx

<details>
<summary><strong>فاز ۱–۳</strong> — کلیک برای باز / بسته</summary>

| فاز | فایل | مدت |
| ---: | --- | --- |
| ۱ | [فاز ۱: پایه عملی](phase1.md) | ۲–۳ هفته |
| ۲ | [فاز ۲: Production](pahse2.md) | ۴–۶ هفته |
| ۳ | [فاز ۳: شبکه و OS](phase3%20-%20Network.md) | ۲–۳ ماه |

</details>

---

## منابع تکمیلی

<details>
<summary><strong>Linux و Git</strong> — کلیک برای باز / بسته</summary>

| موضوع | فایل |
| --- | --- |
| لینوکس برای فول‌استک | [linux.md](linux.md) |
| دستور grep | [linux/grep.md](linux/grep.md) |
| Git Pull / Rebase | [git/git-rebase-fast-forward.md](git/git-rebase-fast-forward.md) |
| HEAD در Git | [git/git-head-guide.md](git/git-head-guide.md) |
| سؤالات تمرینی Git | [git/git-rebase-fast-forward-questions.md](git/git-rebase-fast-forward-questions.md) |

</details>

---

## روش مطالعه پیشنهادی

```text
Read → Configure → Break → Measure → Debug → Explain → Modify
```

برای هر موضوع این چرخه را اجرا کن:

1. مستندات رسمی را بخوان.
2. یک config کوچک بساز.
3. عمداً خرابش کن.
4. فشار تست بگیر.
5. log و metric ببین.
6. دلیل رفتار را بنویس.
7. config را بهتر کن.
8. سورس‌کد مربوطه را پیدا کن.

---

> [!TIP]
> هر فایل دارای **فهرست مطالب قابل باز/بسته**، **بخش‌های collapsible** و **لینک ناوبری** (قبلی / بعدی) است — مثل یک ebook.

</div>
"""


def main() -> None:
    targets = [
        ROOT / "git" / "git-rebase-fast-forward.md",
        ROOT / "git" / "git-head-guide.md",
        ROOT / "git" / "git-rebase-fast-forward-questions.md",
        ROOT / "linux.md",
        ROOT / "linux" / "grep.md",
        ROOT / "phase1.md",
        ROOT / "pahse2.md",
        ROOT / "phase3 - Network.md",
    ]

    for path in targets:
        if not path.exists():
            print(f"skip missing: {path}")
            continue
        original = path.read_text(encoding="utf-8")
        transformed = transform(original, path)
        if transformed != original:
            path.write_text(transformed, encoding="utf-8")
            print(f"updated: {path.relative_to(ROOT)}")
        else:
            print(f"unchanged: {path.relative_to(ROOT)}")

    readme_path = ROOT / "README.md"
    readme_new = build_readme_index()
    readme_path.write_text(readme_new, encoding="utf-8")
    print("updated: README.md (index)")


if __name__ == "__main__":
    main()
