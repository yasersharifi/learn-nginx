---
title: "هفته ۳: Caching و Compression"
description: "هفته ۳: Caching و Compression"
---

# هفته ۳: Caching و Compression

## روز ۱۰: Static Asset Caching

برای فایل‌های static:

```nginx
location /assets/ {
    root /var/www/app;

    expires 30d;
    add_header Cache-Control "public, immutable";
}
```

برای فایل‌هایی که fingerprint دارند مثل:

```text
app.8f3a91.js
style.3b2ac.css
```

می‌توانی cache طولانی بدهی:

```nginx
location ~* \.(js|css|png|jpg|jpeg|gif|svg|ico|woff2)$ {
    root /var/www/app;

    expires 30d;
    add_header Cache-Control "public, immutable";
}
```

## نکته

فقط وقتی `immutable` بده که فایل‌ها fingerprint یا versioned باشند. اگر `app.js` ساده داری و ممکن است محتوا عوض شود، cache طولانی دردسر می‌سازد.

---
