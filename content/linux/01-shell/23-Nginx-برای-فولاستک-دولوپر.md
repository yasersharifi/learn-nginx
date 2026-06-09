---
title: "23. Nginx برای فول‌استک دولوپر"
description: "23. Nginx برای فول‌استک دولوپر"
---

# 23. Nginx برای فول‌استک دولوپر

Nginx معمولاً برای reverse proxy، static files و SSL termination استفاده می‌شود.

### تست کانفیگ Nginx

```bash
sudo nginx -t
```

### reload کردن Nginx

```bash
sudo systemctl reload nginx
```

### مسیرهای مهم Nginx

```bash
/etc/nginx/nginx.conf
/etc/nginx/sites-available/
/etc/nginx/sites-enabled/
/var/log/nginx/access.log
/var/log/nginx/error.log
```

### نمونه reverse proxy برای Node.js

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

بعد از تغییر کانفیگ:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

---
