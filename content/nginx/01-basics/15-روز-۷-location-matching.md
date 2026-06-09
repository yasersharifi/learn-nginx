---
title: "روز ۷: location matching"
description: "روز ۷: location matching"
---

# روز ۷: location matching

این بخش بسیار مهم است.

Nginx چند نوع `location` دارد:

```nginx
location / {}
location = /exact {}
location ^~ /static/ {}
location ~ \.php$ {}
location ~* \.(jpg|png)$ {}
```

## انواع location

| نوع                  | معنی                        |
| -------------------- | --------------------------- |
| `location /`         | prefix match عمومی          |
| `location = /path`   | exact match                 |
| `location ^~ /path/` | prefix match با اولویت بالا |
| `location ~ regex`   | regex case-sensitive        |
| `location ~* regex`  | regex case-insensitive      |

مثال:

```nginx
server {
    listen 80;
    server_name _;

    location = /health {
        return 200 "exact health\n";
    }

    location ^~ /static/ {
        return 200 "static prefix\n";
    }

    location ~ \.jpg$ {
        return 200 "jpg regex\n";
    }

    location / {
        return 200 "default location\n";
    }
}
```

تست:

```bash
curl http://localhost/health
curl http://localhost/static/app.js
curl http://localhost/image.jpg
curl http://localhost/anything
```

## قانون ذهنی ساده

برای فاز ۱ همین را حفظ کن:

```text
Exact match اولویت بالایی دارد.
بعد prefixهای خاص.
بعد regexها.
در نهایت location /.
```

بعداً می‌توانی دقیق‌تر الگوریتم matching را بخوانی.

---
