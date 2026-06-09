---
title: "دیسک و حافظه"
description: "df، du، free — فضای دیسک و RAM"
---

# دیسک و حافظه

| دستور | کاربرد |
| --- | --- |
| `df -h` | فضای دیسک همه mountها |
| `du -sh *` | حجم پوشه‌ها در مسیر فعلی |
| `du -h --max-depth=1 \| sort -h` | مرتب‌شده بر اساس حجم |
| `free -h` | RAM و swap |
| `ulimit -n` | سقف file descriptor شل |
| `cat /proc/PID/limits` | limitهای یک پروسس |

```bash
# پوشه‌های سنگین پروژه
du -sh node_modules .next dist build logs

# فضای /var
du -h --max-depth=1 /var | sort -h
```
