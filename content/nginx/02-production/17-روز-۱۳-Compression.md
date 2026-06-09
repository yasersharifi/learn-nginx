---
title: "روز ۱۳: Compression"
description: "روز ۱۳: Compression"
---

# روز ۱۳: Compression

برای gzip:

```nginx
gzip on;
gzip_comp_level 5;
gzip_min_length 1024;
gzip_types
    text/plain
    text/css
    application/json
    application/javascript
    application/xml
    image/svg+xml;
```

این را معمولاً داخل `http` context می‌گذاری.

## نکته

همه چیز را gzip نکن.

معمولاً این‌ها مناسب‌اند:

```text
- HTML
- CSS
- JS
- JSON
- XML
- SVG
```

این‌ها معمولاً مناسب نیستند:

```text
- jpg
- png
- webp
- mp4
- zip
- pdf
```

چون از قبل compressed هستند.

## تست gzip

```bash
curl -H "Accept-Encoding: gzip" -I http://localhost/assets/app.js
```

دنبال این header بگرد:

```text
Content-Encoding: gzip
```

---
