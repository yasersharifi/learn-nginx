---
title: "هفته سوم: HTTPS، WebSocket، config hygiene و پروژه نهایی"
description: "هفته سوم: HTTPS، WebSocket، config hygiene و پروژه نهایی"
---

# هفته سوم: HTTPS، WebSocket، config hygiene و پروژه نهایی

## روز ۱۱: HTTPS پایه

برای local lab می‌توانی self-signed certificate بسازی.

```bash
sudo mkdir -p /etc/nginx/ssl
sudo openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout /etc/nginx/ssl/nginx-lab.key \
  -out /etc/nginx/ssl/nginx-lab.crt
```

Nginx:

```nginx
server {
    listen 80;
    server_name _;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name _;

    ssl_certificate /etc/nginx/ssl/nginx-lab.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx-lab.key;

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

تست:

```bash
curl -k https://localhost
```

`-k` یعنی certificate self-signed را قبول کن.

برای production واقعی بعداً باید Let’s Encrypt و Certbot یا روش‌های مشابه را یاد بگیری، ولی برای فاز ۱ self-signed کافی است.

---
