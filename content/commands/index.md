---
title: مرجع دستورات
description: دستورات پرکاربرد Linux، Docker، Nginx، Git و ابزارهای روزمره — برای کپی و مرور سریع
sidebar_position: 6
---

# مرجع دستورات

این بخش **کتاب آموزشی نیست** — فهرست دستوراتی است که در deploy، debug و کار روی سرور مدام لازم می‌شوند. هر صفحه یک موضوع کوچک دارد.

**context و workflow:** [راهنمای عملیات روزمره](/daily-guide) — چرا و کی از این دستورات استفاده کنی.

| فصل | محتوا |
| --- | --- |
| [مرجع · Linux](/category/مرجع--linux) | مسیر، فایل، جستجو، پروسس، شبکه، systemd |
| [Docker](/category/docker) | image، container، exec، log |
| [Docker Compose](/category/docker-compose) | up، down، build، log |
| [مرجع · Nginx](/category/مرجع--nginx) | سرویس، کانفیگ، log |
| [مرجع · Git](/category/مرجع--git) | status، pull، push، stash |
| [سایر ابزارها](/category/سایر-ابزارها) | curl، Node/PM2، DB، cron، firewall |

> نکته: دستورات خطرناک مثل `rm -rf` را فقط با مسیر مشخص اجرا کن. در production قبل از `restart` یا `kill`، سرویس و log را چک کن.
