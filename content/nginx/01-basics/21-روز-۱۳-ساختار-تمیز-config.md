---
title: "روز ۱۳: ساختار تمیز config"
description: "روز ۱۳: ساختار تمیز config"
---

# روز ۱۳: ساختار تمیز config

به‌جای اینکه همه‌چیز را در یک فایل شلوغ بریزی، common config بساز.

مثلاً:

```text
/etc/nginx/snippets/proxy-headers.conf
```

محتوا:

```nginx
proxy_http_version 1.1;

proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
```

بعد استفاده:

```nginx
location / {
    proxy_pass http://127.0.0.1:3000;
    include snippets/proxy-headers.conf;
}
```

برای SSL هم:

```text
/etc/nginx/snippets/ssl-lab.conf
```

```nginx
ssl_certificate /etc/nginx/ssl/nginx-lab.crt;
ssl_certificate_key /etc/nginx/ssl/nginx-lab.key;
```

استفاده:

```nginx
server {
    listen 443 ssl;
    server_name _;

    include snippets/ssl-lab.conf;

    location / {
        proxy_pass http://127.0.0.1:3000;
        include snippets/proxy-headers.conf;
    }
}
```

این عادت از همین اول مهم است. config کثیف در production دردسر جدی می‌شود.

---
