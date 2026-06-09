---
slug: /
title: مقدمه
sidebar_position: 1
---

# مسیر یادگیری Nginx

یادداشت‌های شخصی برای یادگیری Nginx، Linux و Git — از نصب و reverse proxy تا شبکه و production.

| # | فصل | زمان تقریبی |
| ---: | --- | --- |
| 1 | [فاز ۱: پایه عملی Nginx](nginx/phase1) | ۲–۳ هفته |
| 2 | [فاز ۲: Production Operations](nginx/phase2) | ۴–۶ هفته |
| 3 | [فاز ۳: شبکه و سیستم‌عامل](nginx/phase3-network) | ۲–۳ ماه |
| 4 | [Linux برای توسعه‌دهنده](linux/) | — |
| 5 | [grep](linux/grep) | — |
| 6 | [Git Pull و Fast-Forward](git/rebase-fast-forward) | — |
| 7 | [HEAD در Git](git/head-guide) | — |
| 8 | [سؤالات Git (Pull / Rebase)](git/rebase-questions) | — |

---

## ساختار

1. کانفیگ عملی و production
2. معماری داخلی و moduleها
3. شبکه، OS و performance

---

## زمان‌بندی (تقریبی)

| هدف | زمان |
| --- | ---: |
| استفاده در پروژه | ۱–۲ ماه |
| production / DevOps | ۳–۶ ماه |
| معماری و performance | ۶–۱۲ ماه |
| سطح پژوهشی | ۱۲–۱۸ ماه |

---

## روش کار

```text
بخوان → کانفیگ کن → خراب کن → تست بگیر → log ببین → توضیح بده → درست کن
```

برای هر موضوع: مستندات رسمی، یک config کوچک، عمداً یک چیز را اشتباه کن، log و metric را چک کن، بعد config را بهتر کن.
