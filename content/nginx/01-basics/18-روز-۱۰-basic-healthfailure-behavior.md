---
title: "روز ۱۰: basic health/failure behavior"
description: "روز ۱۰: basic health/failure behavior"
---

# روز ۱۰: basic health/failure behavior

در نسخه open source، health check فعال پیشرفته مثل NGINX Plus نداری، ولی می‌توانی رفتار failure را با پارامترهای upstream کنترل کنی.

مثال:

```nginx
upstream node_apps {
    server 127.0.0.1:3001 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:3002 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:3003 max_fails=3 fail_timeout=10s;
}
```

معنی ساده:

```text
اگر یک upstream چند بار fail شود،
برای مدتی کمتر به آن request داده می‌شود.
```

تمرین:

1. سه app را اجرا کن.
2. request loop بزن.
3. یکی از appها را kill کن.
4. log را ببین.
5. ببین Nginx چطور رفتار می‌کند.

```bash
sudo tail -f /var/log/nginx/error.log
```

---
