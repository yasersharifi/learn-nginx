<div dir="rtl" align="right">

# مسیر مطالعه Nginx در سطح دکترای کامپیوتر

اگر می‌خواهی Nginx را در سطح بسیار عمیق و نزدیک به نگاه یک دکترای کامپیوتر بخوانی، نباید آن را فقط به‌عنوان یک وب‌سرور یا ابزار reverse proxy ببینی. باید Nginx را به‌عنوان یک نمونه واقعی از سیستم‌های high-performance، event-driven، network server و production infrastructure مطالعه کنی.

<details>
<summary><strong>📑 فهرست مطالب</strong> — <em>کلیک برای باز / بسته کردن</em></summary>

| # | کتاب / فصل | توضیح |
| ---: | --- | --- |
| 1 | **مسیر مطالعه Nginx** | صفحه اصلی و نقشه راه |
| 2 | [فاز ۱: پایه عملی Nginx](phase1.md) | ۲–۳ هفته — reverse proxy، static، HTTPS |
| 3 | [فاز ۲: Production Operations](pahse2.md) | ۴–۶ هفته — timeout، cache، rate limit |
| 4 | [فاز ۳: شبکه و سیستم‌عامل](phase3%20-%20Network.md) | ۲–۳ ماه — TCP، epoll، performance |
| 5 | [آنچه از لینوکس باید بدانم](linux.md) | راهنمای فول‌استک دولوپر |
| 6 | [grep Command Usage](linux/grep.md) | جستجوی متن در فایل‌ها |
| 7 | [Git Pull و Fast-Forward](git/git-rebase-fast-forward.md) | merge، rebase، ff-only |
| 8 | [HEAD در Git](git/git-head-guide.md) | HEAD~1، detached HEAD، reset |
| 9 | [سؤالات سناریومحور Git](git/git-rebase-fast-forward-questions.md) | ۲۰ سناریو با جواب |

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
