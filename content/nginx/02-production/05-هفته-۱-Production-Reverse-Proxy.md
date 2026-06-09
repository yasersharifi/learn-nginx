---
title: "هفته ۱: Production Reverse Proxy"
description: "هفته ۱: Production Reverse Proxy"
---

# هفته ۱: Production Reverse Proxy

## روز ۱: ساختار Production Config

در فاز ۱ احتمالاً config ساده‌ای مثل این داشتی:

```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000;
    }
}
```

برای production این کافی نیست.

یک ساختار بهتر:

```text
/etc/nginx/
  nginx.conf
  sites-available/
    app.conf
  sites-enabled/
    app.conf -> ../sites-available/app.conf
  snippets/
    proxy-headers.conf
    proxy-timeouts.conf
    ssl-params.conf
    security-headers.conf
```

config را طوری بنویس که بفهمی و دوباره استفاده کنی.

---

## snippet برای proxy headers

فایل:

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
proxy_set_header X-Forwarded-Host $host;
proxy_set_header X-Forwarded-Port $server_port;
```

استفاده:

```nginx
location / {
    proxy_pass http://app_backend;
    include snippets/proxy-headers.conf;
}
```

## چرا این مهم است؟

Backend معمولاً باید بداند:

* request اصلی از چه IP آمده
* request اصلی HTTP بوده یا HTTPS
* host اصلی چه بوده
* آیا پشت proxy است یا نه

بدون این headerها، backend ممکن است redirect اشتباه بسازد، IP کاربر را اشتباه تشخیص دهد یا HTTPS را درست detect نکند.

---
