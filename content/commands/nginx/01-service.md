---
title: "سرویس Nginx"
description: "systemctl و nginx — نصب، start، stop، reload"
---

# سرویس Nginx

## نصب (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install nginx
nginx -v
```

## systemctl

| دستور | کاربرد |
| --- | --- |
| `sudo systemctl status nginx` | وضعیت |
| `sudo systemctl start nginx` | شروع |
| `sudo systemctl stop nginx` | توقف |
| `sudo systemctl restart nginx` | ری‌استارت کامل |
| `sudo systemctl reload nginx` | reload — **ترجیح در production** |
| `sudo systemctl enable nginx` | بعد از boot |
| `sudo systemctl is-active nginx` | فعال؟ |

## دستور مستقیم nginx

| دستور | کاربرد |
| --- | --- |
| `sudo nginx -t` | تست syntax کانفیگ |
| `sudo nginx -T` | نمایش config کامل merge‌شده |
| `sudo kill -HUP $(cat /run/nginx.pid)` | reload دستی |
| `ps aux \| grep nginx` | پروسس master/worker |

```bash
# deploy امن
sudo nginx -t && sudo systemctl reload nginx
```
