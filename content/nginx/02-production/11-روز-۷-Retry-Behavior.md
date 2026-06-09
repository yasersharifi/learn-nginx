---
title: "روز ۷: Retry Behavior"
description: "روز ۷: Retry Behavior"
---

# روز ۷: Retry Behavior

Directive مهم:

```nginx
proxy_next_upstream error timeout http_502 http_503 http_504;
```

مثال:

```nginx
location / {
    proxy_pass http://app_backend;

    proxy_next_upstream error timeout http_502 http_503 http_504;
    proxy_next_upstream_tries 2;
    proxy_next_upstream_timeout 10s;

    include snippets/proxy-headers.conf;
    include snippets/proxy-timeouts.conf;
}
```

## معنی

اگر upstream اول fail شد، Nginx می‌تواند request را به upstream بعدی امتحان کند.

## هشدار مهم

برای requestهای غیر idempotent مثل `POST`, `PATCH`, `DELETE` باید خیلی مراقب retry باشی.

مثلاً اگر یک `POST /payments` دوبار ارسال شود، ممکن است دوبار پرداخت ثبت شود.

برای APIهای حساس، retry را محدود و آگاهانه تنظیم کن.

## تفکیک GET و POST

برای مسیرهای safe:

```nginx
location /api/read/ {
    proxy_pass http://api_backend/;

    proxy_next_upstream error timeout http_502 http_503 http_504;
    proxy_next_upstream_tries 2;

    include snippets/proxy-headers.conf;
}
```

برای مسیرهای حساس:

```nginx
location /api/payments/ {
    proxy_pass http://api_backend/;

    proxy_next_upstream off;

    include snippets/proxy-headers.conf;
}
```

## تمرین

یک endpoint بساز که گاهی 502 یا timeout بدهد. سپس ببین Nginx چطور request را retry می‌کند.

---
