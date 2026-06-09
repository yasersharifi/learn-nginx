---
title: "روز ۱۷: Security Headers پایه"
description: "روز ۱۷: Security Headers پایه"
---

# روز ۱۷: Security Headers پایه

فایل:

```text
/etc/nginx/snippets/security-headers.conf
```

محتوا:

```nginx
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header X-XSS-Protection "0" always;
```

برای HTTPS:

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

## هشدار درباره HSTS

`HSTS` را با احتیاط فعال کن، مخصوصاً `includeSubDomains`.

اگر اشتباه ست شود، مرورگرها تا مدت طولانی سایت را فقط با HTTPS باز می‌کنند. برای دامنه production خوب است، ولی برای lab یا دامنه‌ای که HTTPS کامل ندارد خطرناک است.

## Content Security Policy

CSP خیلی مهم است، ولی نباید کورکورانه اضافه شود.

مثال ساده:

```nginx
add_header Content-Security-Policy "default-src 'self'" always;
```

اما برای اپلیکیشن‌های واقعی معمولاً assetها، API، analytics، fontها و CDNها باعث پیچیدگی می‌شوند.

در فاز ۲ فقط concept را بفهم. CSP جدی را در فاز Security عمیق‌تر بخوان.

---
