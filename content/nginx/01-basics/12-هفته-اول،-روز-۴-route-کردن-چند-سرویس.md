---
title: "هفته اول، روز ۴: route کردن چند سرویس"
description: "هفته اول، روز ۴: route کردن چند سرویس"
---

# هفته اول، روز ۴: route کردن چند سرویس

فرض کن دو سرویس داری:

```text
Frontend: localhost:3000
API:      localhost:4000
```

Nginx:

```nginx
server {
    listen 80;
    server_name _;

    location /api/ {
        proxy_pass http://127.0.0.1:4000/;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location / {
        proxy_pass http://127.0.0.1:3000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

معنی:

```text
/api/* ← backend API
/*      ← frontend
```

این ساختار در پروژه‌های واقعی زیاد استفاده می‌شود.

---
