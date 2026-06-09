---
title: "روز ۵: Proxy Error Handling"
description: "روز ۵: Proxy Error Handling"
---

# روز ۵: Proxy Error Handling

در production بهتر است صفحه یا response خطا را کنترل کنی.

نمونه:

```nginx
proxy_intercept_errors on;

error_page 502 503 504 /50x.html;

location = /50x.html {
    root /var/www/errors;
    internal;
}
```

فایل بساز:

```bash
sudo mkdir -p /var/www/errors
echo "<h1>Service temporarily unavailable</h1>" | sudo tee /var/www/errors/50x.html
```

## نکته

برای API بهتر است HTML برنگردانی. برای API می‌توانی JSON برگردانی:

```nginx
location = /api-50x.json {
    internal;
    default_type application/json;
    return 503 '{"error":"service_unavailable","message":"Service temporarily unavailable"}';
}
```

و در location API:

```nginx
location /api/ {
    proxy_pass http://api_backend/;
    proxy_intercept_errors on;
    error_page 502 503 504 = /api-50x.json;

    include snippets/proxy-headers.conf;
    include snippets/proxy-timeouts.conf;
}
```

## تمرین

Backend را خاموش کن و تست کن:

```bash
curl -i http://localhost/api/users
```

باید response کنترل‌شده ببینی، نه صفحه خام Nginx.

---
