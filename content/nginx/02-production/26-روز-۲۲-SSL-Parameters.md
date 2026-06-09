---
title: "روز ۲۲: SSL Parameters"
description: "روز ۲۲: SSL Parameters"
---

# روز ۲۲: SSL Parameters

snippet:

```text
/etc/nginx/snippets/ssl-params.conf
```

نمونه ساده:

```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers off;

ssl_session_cache shared:SSL:10m;
ssl_session_timeout 1d;
ssl_session_tickets off;
```

استفاده:

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    include snippets/ssl-params.conf;

    location / {
        proxy_pass http://app_backend;
        include snippets/proxy-headers.conf;
    }
}
```

## نکته

Cipherها و تنظیمات TLS با زمان تغییر می‌کنند. برای production واقعی بهتر است از Mozilla SSL Configuration Generator یا guidelineهای معتبر به‌روز استفاده کنی.

---
