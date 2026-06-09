---
title: "هفته دوم: server_name، location matching، logs و load balancing"
description: "هفته دوم: server_name، location matching، logs و load balancing"
---

# هفته دوم: server_name، location matching، logs و load balancing

## روز ۶: `server_name` و virtual hosts

Nginx می‌تواند چند سایت را روی یک سرور هندل کند.

```nginx
server {
    listen 80;
    server_name app.local;

    location / {
        return 200 "App Site\n";
    }
}

server {
    listen 80;
    server_name api.local;

    location / {
        return 200 "API Site\n";
    }
}
```

تست بدون DNS واقعی:

```bash
curl -H "Host: app.local" http://127.0.0.1
curl -H "Host: api.local" http://127.0.0.1
```

نتیجه:

```text
App Site
API Site
```

---

## default server

اگر Host match نشود، Nginx از default server استفاده می‌کند.

```nginx
server {
    listen 80 default_server;
    server_name _;

    return 444;
}
```

`444` یک status خاص Nginx است که connection را بدون response می‌بندد.

برای production معمولاً بهتر است default server رفتار مشخص داشته باشد.

مثلاً:

```nginx
server {
    listen 80 default_server;
    server_name _;

    return 404;
}
```

یا redirect به دامنه اصلی:

```nginx
server {
    listen 80 default_server;
    server_name _;

    return 301 https://example.com$request_uri;
}
```

---
