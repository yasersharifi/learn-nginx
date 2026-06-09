---
title: "cron و firewall"
description: "crontab، ufw — زمان‌بندی و firewall"
---

# cron و firewall

## cron

| دستور | کاربرد |
| --- | --- |
| `crontab -e` | ویرایش cron کاربر |
| `crontab -l` | نمایش cronها |
| `crontab -r` | حذف همه — **احتیاط** |

نمونه در crontab:

```cron
# هر روز ۲ صبح
0 2 * * * /home/user/scripts/backup.sh

# هر ۵ دقیقه
*/5 * * * * /usr/bin/curl -fsS http://localhost/health || echo fail

# با log
*/10 * * * * /usr/bin/node /app/worker.js >> /app/worker.log 2>&1
```

## UFW (firewall)

| دستور | کاربرد |
| --- | --- |
| `sudo ufw status` | وضعیت |
| `sudo ufw allow ssh` | باز کردن SSH |
| `sudo ufw allow 80` | HTTP |
| `sudo ufw allow 443` | HTTPS |
| `sudo ufw allow 3000/tcp` | پورت مشخص |
| `sudo ufw enable` | فعال‌سازی |
| `sudo ufw disable` | غیرفعال |
| `sudo ufw delete allow 3000` | حذف rule |

> قبل از `ufw enable` حتماً SSH (`22`) را allow کن.
