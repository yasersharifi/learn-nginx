---
title: "حالا proxy headerها را درست کن"
description: "حالا proxy headerها را درست کن"
---

# حالا proxy headerها را درست کن

config بهتر:

```nginx
server {
    listen 80;
    server_name _;

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

معنی headerها:

| Header              | معنی                            |
| ------------------- | ------------------------------- |
| `Host`              | دامنه اصلی request              |
| `X-Real-IP`         | IP مستقیم client از دید Nginx   |
| `X-Forwarded-For`   | زنجیره IPهای proxy شده          |
| `X-Forwarded-Proto` | http یا https بودن request اصلی |

این برای backend خیلی مهم است. مثلاً backend باید بداند request اصلی HTTPS بوده یا HTTP.

---
