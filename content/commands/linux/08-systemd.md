---
title: "systemd و journal"
description: "systemctl، journalctl — مدیریت سرویس و خواندن log سیستم"
---

# systemd و journal

## systemctl

| دستور | کاربرد |
| --- | --- |
| `sudo systemctl status nginx` | وضعیت سرویس |
| `sudo systemctl start nginx` | شروع |
| `sudo systemctl stop nginx` | توقف |
| `sudo systemctl restart nginx` | ری‌استارت کامل |
| `sudo systemctl reload nginx` | reload بدون قطع connection |
| `sudo systemctl enable nginx` | اجرا بعد از boot |
| `sudo systemctl disable nginx` | غیرفعال بعد از boot |
| `sudo systemctl is-active nginx` | فعال است؟ |
| `sudo systemctl list-units --type=service` | لیست سرویس‌ها |

## journalctl

| دستور | کاربرد |
| --- | --- |
| `sudo journalctl -u nginx` | log سرویس |
| `sudo journalctl -u nginx -f` | log زنده |
| `sudo journalctl -u nginx -n 100` | ۱۰۰ خط آخر |
| `sudo journalctl -u nginx -b` | از boot فعلی |
| `sudo journalctl -u my-api --no-pager` | بدون pager |

```bash
# افزایش limit فایل برای nginx
sudo systemctl edit nginx
# [Service]
# LimitNOFILE=65535
sudo systemctl daemon-reload
sudo systemctl restart nginx
```
