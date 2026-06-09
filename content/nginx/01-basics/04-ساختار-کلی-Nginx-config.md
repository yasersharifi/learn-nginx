---
title: "ساختار کلی Nginx config"
description: "ساختار کلی Nginx config"
---

# ساختار کلی Nginx config

Nginx config از context و directive ساخته می‌شود.

نمونه ساده:

```nginx
user www-data;

worker_processes auto;

events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        server_name example.com;

        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
```

## مفهوم directive

هر خطی مثل این یک directive است:

```nginx
worker_processes auto;
```

یا:

```nginx
listen 80;
```

Directiveها معمولاً با `;` تمام می‌شوند.

## مفهوم context یا block

هر چیزی که داخل `{}` است یک context است:

```nginx
http {
    server {
        location / {
        }
    }
}
```

contextهای مهم:

```text
main
events
http
server
location
upstream
```

---
