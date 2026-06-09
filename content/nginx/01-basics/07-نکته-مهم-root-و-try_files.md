---
title: "نکته مهم: `root` و `try_files`"
description: "نکته مهم: `root` و `try_files`"
---

# نکته مهم: `root` و `try_files`

این بخش خیلی مهم است چون خیلی‌ها با همین گیر می‌کنند.

```nginx
root /var/www/nginx-lab;
```

یعنی مسیر فایل‌ها از این directory شروع می‌شود.

```nginx
location / {
    try_files $uri $uri/ =404;
}
```

یعنی:

```text
اول دنبال فایل دقیق بگرد
بعد دنبال directory بگرد
اگر نبود 404 بده
```

مثلاً request:

```text
/about.html
```

Nginx دنبال این فایل می‌گردد:

```text
/var/www/nginx-lab/about.html
```

---
