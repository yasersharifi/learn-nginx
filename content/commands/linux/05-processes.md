---
title: "پروسس"
description: "ps، top، kill، pkill — دیدن و متوقف کردن پروسس"
---

# پروسس

| دستور | کاربرد |
| --- | --- |
| `ps aux` | همه پروسس‌ها |
| `ps aux \| grep node` | جستجوی پروسس |
| `pgrep -f "nginx: worker"` | PID با الگو |
| `top` | مانیتور زنده CPU/RAM |
| `htop` | top بهتر (اگر نصب باشد) |
| `kill PID` | توقف ملایم (SIGTERM) |
| `kill -9 PID` | توقف اجباری |
| `pkill node` | kill با نام — **محتاط** |
| `nohup cmd &` | اجرا در پس‌زمینه بعد از بستن ترمینال |

```bash
# منابع یک پروسس
ps -o pid,ppid,cmd,%cpu,%mem -p PID
cat /proc/PID/limits
```
