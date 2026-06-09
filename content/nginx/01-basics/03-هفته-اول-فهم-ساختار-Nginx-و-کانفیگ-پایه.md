---
title: "هفته اول: فهم ساختار Nginx و کانفیگ پایه"
description: "هفته اول: فهم ساختار Nginx و کانفیگ پایه"
---

# هفته اول: فهم ساختار Nginx و کانفیگ پایه

## روز ۱: نصب و اجرای اولیه

### چیزهایی که باید یاد بگیری

* Nginx چطور نصب می‌شود.
* سرویس Nginx چطور start/stop/reload می‌شود.
* فایل‌های اصلی کجا هستند.
* config syntax چطور validate می‌شود.

روی Ubuntu/Debian:

```bash
sudo apt update
sudo apt install nginx
```

بررسی وضعیت:

```bash
sudo systemctl status nginx
```

شروع:

```bash
sudo systemctl start nginx
```

توقف:

```bash
sudo systemctl stop nginx
```

ری‌استارت:

```bash
sudo systemctl restart nginx
```

reload بدون قطع connectionهای فعال:

```bash
sudo systemctl reload nginx
```

تست صحت config:

```bash
sudo nginx -t
```

نمایش config نهایی که Nginx واقعاً می‌بیند:

```bash
sudo nginx -T
```

این دستور خیلی مهم است. چون ممکن است configها از چند فایل include شده باشند و تو فقط یک فایل را ببینی.

---

## فایل‌ها و مسیرهای مهم

در Ubuntu معمولاً این‌ها را می‌بینی:

```text
/etc/nginx/nginx.conf
/etc/nginx/sites-available/
/etc/nginx/sites-enabled/
/var/log/nginx/access.log
/var/log/nginx/error.log
/usr/share/nginx/html/
```

معنی‌شان:

| مسیر                          | کاربرد                           |
| ----------------------------- | -------------------------------- |
| `/etc/nginx/nginx.conf`       | config اصلی                      |
| `/etc/nginx/sites-available/` | فایل‌های سایت‌های قابل فعال‌سازی |
| `/etc/nginx/sites-enabled/`   | سایت‌های فعال‌شده                |
| `/var/log/nginx/access.log`   | لاگ requestها                    |
| `/var/log/nginx/error.log`    | لاگ خطاها                        |
| `/usr/share/nginx/html/`      | مسیر پیش‌فرض static files        |

در بعضی distroها مثل CentOS/RHEL ساختار فرق می‌کند و ممکن است `conf.d` بیشتر استفاده شود:

```text
/etc/nginx/conf.d/
```

---
