---
title: "روز ۲۳: HTTP/2"
description: "روز ۲۳: HTTP/2"
---

# روز ۲۳: HTTP/2

برای فعال‌سازی HTTP/2:

```nginx
listen 443 ssl http2;
```

یا در نسخه‌های جدیدتر Nginx ممکن است syntax جدا توصیه شود:

```nginx
listen 443 ssl;
http2 on;
```

## چرا HTTP/2؟

* multiplexing
* header compression
* performance بهتر برای assetهای متعدد
* کاهش نیاز به چند connection جدا

## تست

```bash
curl -I --http2 https://example.com
```

---
