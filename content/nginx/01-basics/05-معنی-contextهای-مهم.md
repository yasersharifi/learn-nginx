---
title: "معنی contextهای مهم"
description: "معنی contextهای مهم"
---

# معنی contextهای مهم

## 1. main context

بیرون از همه blockهاست.

```nginx
user www-data;
worker_processes auto;
pid /run/nginx.pid;
```

اینجا تنظیمات سطح کل process تعریف می‌شود.

مثلاً:

```nginx
worker_processes auto;
```

یعنی Nginx خودش بر اساس CPU تعداد workerها را تعیین کند.

---

## 2. events context

مربوط به connection handling است.

```nginx
events {
    worker_connections 1024;
}
```

فعلاً فقط این را بدان:

```nginx
worker_connections 1024;
```

یعنی هر worker حداکثر چند connection می‌تواند مدیریت کند.

ولی اشتباه رایج این است که فکر کنیم:

```text
worker_processes × worker_connections = تعداد request همزمان
```

تقریباً هست، ولی دقیق نیست. چون connection با request فرق دارد. keep-alive، upstream connection و فایل‌ها هم اثر دارند.

در فازهای بعد عمیق‌تر می‌خوانی.

---

## 3. http context

همه تنظیمات مربوط به HTTP داخل این context می‌آید:

```nginx
http {
    include /etc/nginx/mime.types;

    server {
        listen 80;
        server_name example.com;
    }
}
```

اینجا مواردی مثل این تعریف می‌شوند:

```text
log format
gzip
proxy settings
server blocks
upstream blocks
mime types
timeouts
```

---

## 4. server context

هر `server` معمولاً نماینده یک سایت، دامنه یا virtual host است.

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        root /var/www/example;
        index index.html;
    }
}
```

یعنی:

```text
اگر request روی پورت 80 آمد
و Host برابر example.com بود
این server block مسئول پاسخ دادن است
```

---

## 5. location context

`location` تصمیم می‌گیرد با مسیرهای مختلف URL چه شود.

مثلاً:

```nginx
location / {
    proxy_pass http://localhost:3000;
}

location /static/ {
    root /var/www/app;
}
```

یعنی:

```text
/        ← برو سمت app
/static/ ← فایل static بده
```

---

## 6. upstream context

برای تعریف گروهی از backendها استفاده می‌شود.

```nginx
upstream app_servers {
    server 127.0.0.1:3000;
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
```

بعد در `proxy_pass` استفاده می‌کنی:

```nginx
location / {
    proxy_pass http://app_servers;
}
```

این یعنی Nginx بین چند backend load balance می‌کند.

---
