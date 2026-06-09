---
title: "روز ۱۴: Brotli Concept"
description: "روز ۱۴: Brotli Concept"
---

# روز ۱۴: Brotli Concept

Brotli معمولاً برای assetهای text-based compression بهتری نسبت به gzip دارد، مخصوصاً برای frontend assetها.

اما در Nginx open source ممکن است نیاز به module جدا داشته باشد، بسته به نحوه نصب و distro.

برای فاز ۲ کافی است مفهوم را بفهمی:

```text
gzip:
- رایج
- built-in در اکثر نصب‌ها
- ساده‌تر

brotli:
- compression بهتر
- گاهی نیازمند module جدا
- مناسب static assets
```

در production، اگر CDN جلوی سیستم داری، ممکن است compression را CDN انجام دهد و Nginx لازم نباشد همه بار compression را بردارد.

---
