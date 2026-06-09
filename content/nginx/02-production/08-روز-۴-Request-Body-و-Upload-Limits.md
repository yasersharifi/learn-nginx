---
title: "روز ۴: Request Body و Upload Limits"
description: "روز ۴: Request Body و Upload Limits"
---

# روز ۴: Request Body و Upload Limits

در production باید محدودیت request body داشته باشی.

Directive مهم:

```nginx
client_max_body_size 10m;
```

اگر upload داری، ممکن است بیشتر نیاز باشد:

```nginx
client_max_body_size 50m;
```

برای مسیر خاص:

```nginx
location /api/uploads/ {
    client_max_body_size 100m;

    proxy_pass http://api_backend/;
    include snippets/proxy-headers.conf;
    include snippets/proxy-timeouts.conf;
}
```

## چرا مهم است؟

بدون limit درست:

* کاربر می‌تواند body خیلی بزرگ بفرستد
* memory/disk فشار می‌گیرد
* backend درگیر request غیرضروری می‌شود
* امکان abuse بیشتر می‌شود

## تمرین

با `curl` فایل بزرگ بفرست:

```bash
dd if=/dev/zero of=/tmp/test-20mb.bin bs=1M count=20
curl -i -X POST --data-binary @/tmp/test-20mb.bin http://localhost/api/upload
```

اگر `client_max_body_size 10m` باشد، باید خطای `413 Request Entity Too Large` ببینی.

---
