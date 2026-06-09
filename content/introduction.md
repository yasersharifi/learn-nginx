---
slug: /
title: پیش‌گفتار
description: زیرساخت عملی وب — راهنمای گام‌به‌گام Nginx، Linux و Git برای توسعه‌دهنده
sidebar_position: 1
---

# زیرساخت عملی وب

**راهنمای Nginx، Linux و Git برای توسعه‌دهنده**

یادداشت‌های شخصی برای یادگیری زیرساخت سرور — از reverse proxy و production تا خط فرمان لینوکس و Git روزمره. هر صفحه فقط **یک موضوع کوچک** دارد تا مثل یک کتاب واقعی، قابل مرور و مرور مجدد باشد.

---

## این کتاب برای چه کسی است؟

برای توسعه‌دهنده‌ای که فرانت و بک می‌زند، گاهی روی سرور deploy می‌کند، و می‌خواهد Nginx را **عملی** یاد بگیرد — نه فقط directiveها را حفظ کند. Linux و Git هم به‌عنوان ابزارهای روزمره کنار Nginx آمده‌اند.

---

## ساختار کتاب

| بخش                                               | موضوع                                     |
| ------------------------------------------------- | ----------------------------------------- |
| [Nginx · پایه عملی](/category/فصل-۱--پایه-عملی)   | نصب، کانفیگ، proxy، HTTPS                 |
| [Nginx · Production](/category/فصل-۲--production) | timeout، cache، rate limit، observability |
| [Nginx · شبکه و OS](/category/فصل-۳--شبکه-و-os)   | TCP، epoll، benchmark                     |
| [Linux · خط فرمان](/category/خط-فرمان)            | shell، سرویس، deploy                      |
| [Linux · grep](/category/grep)                    | جستجو در log و کد                         |
| [Git · Pull و Merge](/category/pull-و-merge)      | pull، rebase، fast-forward                |

برای **مرور سریع** هر بخش ← [فهرست مرور](review).

---

## روش مطالعه

> بخوان ← کانفیگ کن ← خراب کن ← log ببین ← توضیح بده ← درست کن

برای هر درس: یک config کوچک، عمداً یک چیز را اشتباه کن، error log را بخوان، بعد config را بهتر کن.
