---
title: "هفته ۲: Load Balancing و Failure Behavior"
description: "هفته ۲: Load Balancing و Failure Behavior"
---

# هفته ۲: Load Balancing و Failure Behavior

## روز ۶: Upstream Production Config

Config ساده:

```nginx
upstream app_backend {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
```

نمونه config برای production:

```nginx
upstream app_backend {
    least_conn;

    server 127.0.0.1:3001 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:3002 max_fails=3 fail_timeout=10s;
    keepalive 32;
}
```

## معنی directiveها

| Directive      | معنی                                               |
| -------------- | -------------------------------------------------- |
| `least_conn`   | request جدید به backend با connection کمتر برود    |
| `max_fails`    | تعداد fail مجاز قبل از temporarily unavailable شدن |
| `fail_timeout` | بازه زمانی fail و مدت کنار گذاشتن server           |
| `keepalive`    | connection reuse بین Nginx و upstream              |

## نکته مهم درباره keepalive

اگر در upstream از `keepalive` استفاده می‌کنی، در location باید HTTP/1.1 ست شود:

```nginx
proxy_http_version 1.1;
proxy_set_header Connection "";
```

Config بهتر برای upstream keepalive:

```nginx
upstream app_backend {
    least_conn;

    server 127.0.0.1:3001 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:3002 max_fails=3 fail_timeout=10s;

    keepalive 32;
}

server {
    listen 80;

    location / {
        proxy_pass http://app_backend;

        proxy_http_version 1.1;
        proxy_set_header Connection "";

        include snippets/proxy-headers.conf;
        include snippets/proxy-timeouts.conf;
    }
}
```

## تمرین

سه app اجرا کن:

```bash
PORT=3001 INSTANCE=app-1 node server.js
PORT=3002 INSTANCE=app-2 node server.js
PORT=3003 INSTANCE=app-3 node server.js
```

Nginx را به سه app وصل کن.

بعد تست:

```bash
for i in {1..30}; do curl -s http://localhost | jq; done
```

یکی از appها را kill کن و error log را ببین:

```bash
sudo tail -f /var/log/nginx/error.log
```

---
