---
slug: /
title: پیش‌گفتار
description: زیرساخت عملی وب — راهنمای گام‌به‌گام Nginx، Linux و Git برای توسعه‌دهنده فول‌استک و بک‌اند
sidebar_position: 1
---

# زیرساخت عملی وب

**راهنمای Nginx، Linux و Git برای توسعه‌دهنده**

مرجع فنی برای کار روزمره: deploy روی سرور، عیب‌یابی 502 و timeout، خواندن log، و حل مشکل Git — نه حفظ directive، بلکه **فهمیدن چه اتفاقی می‌افتد و چطور زودتر fix کنی**.

---

## این کتاب برای چه کسی است؟

| | |
| --- | --- |
| **مخاطب** | توسعه‌دهنده فول‌استک و بک‌اند |
| **هدف** | مرجع روزانه برای deploy، debug و همکاری Git |
| **نتیجه** | خطاهای شبکه را زودتر پیدا کنی، Nginx را با اطمینان manage کنی، Git conflict را بدون panic حل کنی |
| **لحن** | حرفه‌ای و فنی — بدون jargon اضافی |

اگر گاهی روی سرور deploy می‌کنی، Nginx جلوی اپت است، و `git pull` گاهی خطا می‌دهد — این کتاب برای توست.

---

## از کجا شروع کنم؟

**→ [راهنمای عملیات روزمره](/daily-guide)** — سند اصلی: دستورات ضروری، workflow عیب‌یابی 502، Git روزمره، ریسک‌ها و گام بعدی.

برای **مرور سریع** هر فصل ← [فهرست مرور](review).

برای **کپی دستور** ← [مرجع دستورات](/commands).

---

## ساختار کتاب

| بخش | موضوع | چه چیزی یاد می‌گیری |
| --- | --- | --- |
| [Nginx · پایه عملی](/category/فصل-۱--پایه-عملی) | نصب، کانفیگ، proxy، HTTPS | reverse proxy، errorهای 502/404، log |
| [Nginx · Production](/category/فصل-۲--production) | timeout، cache، rate limit | پایداری، error handling، observability |
| [Nginx · شبکه و OS](/category/فصل-۳--شبکه-و-os) | TCP، epoll، benchmark | چرا کند است — نه فقط چطور fix |
| [Linux · خط فرمان](/category/خط-فرمان) | shell، سرویس، deploy | `curl`، `ss`، journalctl، PM2، Docker |
| [Linux · grep](/category/grep) | جستجو در log و کد | پیدا کردن خطا در gigabyte log |
| [Git · Pull و Merge](/category/pull-و-merge) | pull، rebase، fast-forward | merge vs rebase با دلیل |
| [Git · سناریوها](/category/سناریوها) | ۲۰ حالت رایج | جواب آماده وقتی گیر کردی |
| [مرجع دستورات](/commands) | cheat sheet | Linux، Docker، Nginx، Git |

---

## روش مطالعه

> بخوان ← کانفیگ کن ← عمداً خراب کن ← log ببین ← توضیح بده ← درست کن

برای هر درس: یک config کوچک بساز، یک چیز را عمداً wrong کن، `error.log` را بخوان، بعد config را بهتر کن. این روش باعث می‌شود در production به‌جای حدس، **evidence** داشته باشی.

---

## محدودیت‌ها

- مثال‌ها عمدتاً **Ubuntu/Debian** و Nginx به‌عنوان reverse proxy هستند.
- Kubernetes، CDN و multi-region پوشش داده نشده — workflow debug (upstream → log → config) قابل انتقال است.
- Git فرض می‌کند remote روی GitHub/GitLab و branch اصلی `main` است.

جزئیات فرضیات ← [راهنمای عملیات روزمره · فرضیات](/daily-guide#فرضیات).
