---
title: "مسیرها و کانفیگ"
description: "مسیر فایل‌های Nginx، sites-enabled، snippets"
---

# مسیرها و کانفیگ

## مسیرهای مهم (Ubuntu)

| مسیر | کاربرد |
| --- | --- |
| `/etc/nginx/nginx.conf` | کانفیگ اصلی |
| `/etc/nginx/sites-available/` | سایت‌های آماده فعال‌سازی |
| `/etc/nginx/sites-enabled/` | سایت‌های فعال (symlink) |
| `/etc/nginx/conf.d/` | فایل‌های اضافه |
| `/etc/nginx/snippets/` | تکه‌های مشترک |
| `/var/log/nginx/access.log` | log درخواست |
| `/var/log/nginx/error.log` | log خطا |
| `/usr/share/nginx/html/` | static پیش‌فرض |
| `/run/nginx.pid` | PID master |

## فعال‌سازی سایت

```bash
sudo nano /etc/nginx/sites-available/myapp

sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## SSL (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com
sudo certbot renew --dry-run
sudo systemctl status certbot.timer
```

## self-signed (lab)

```bash
sudo mkdir -p /etc/nginx/ssl
sudo openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout /etc/nginx/ssl/lab.key \
  -out /etc/nginx/ssl/lab.crt
```
