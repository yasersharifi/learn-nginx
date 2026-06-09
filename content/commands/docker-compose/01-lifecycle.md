---
title: "چرخه حیات"
description: "docker compose up، down، ps — بالا و پایین آوردن سرویس‌ها"
---

# چرخه حیات

| دستور | کاربرد |
| --- | --- |
| `docker compose up` | اجرا (foreground) |
| `docker compose up -d` | detached (پس‌زمینه) |
| `docker compose up -d --build` | build + اجرا |
| `docker compose down` | توقف و حذف container |
| `docker compose down -v` | + حذف volumeها |
| `docker compose stop` | فقط توقف |
| `docker compose start` | شروع مجدد |
| `docker compose restart` | ری‌استارت |
| `docker compose ps` | وضعیت سرویس‌ها |
| `docker compose top` | پروسس‌ها |
| `docker compose pull` | pull imageها |
| `docker compose build` | build همه |
| `docker compose build api` | build یک سرویس |
| `docker compose config` | نمایش config نهایی |
| `docker compose validate` | اعتبارسنجی فایل |

```bash
# فایل مشخص
docker compose -f docker-compose.prod.yml up -d

# scale (اگر سرویس اجازه دهد)
docker compose up -d --scale worker=3
```

> نسخه قدیمی: `docker-compose` (با خط تیره) — در اکثر سیستم‌های جدید `docker compose` (با فاصله) است.
