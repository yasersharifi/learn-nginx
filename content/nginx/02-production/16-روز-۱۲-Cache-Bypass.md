---
title: "روز ۱۲: Cache Bypass"
description: "روز ۱۲: Cache Bypass"
---

# روز ۱۲: Cache Bypass

برای requestهایی با Authorization بهتر است cache bypass شود.

```nginx
proxy_cache_bypass $http_authorization;
proxy_no_cache $http_authorization;
```

نمونه:

```nginx
location /api/public/ {
    proxy_pass http://api_backend/;

    proxy_cache app_cache;
    proxy_cache_valid 200 10m;

    proxy_cache_bypass $http_authorization;
    proxy_no_cache $http_authorization;

    add_header X-Cache-Status $upstream_cache_status;

    include snippets/proxy-headers.conf;
}
```

## Query String

به‌صورت پیش‌فرض cache key معمولاً شامل URI کامل با query string است. اما برای کنترل بهتر می‌توانی cache key تعریف کنی:

```nginx
proxy_cache_key "$scheme$request_method$host$request_uri";
```

## تمرین

این‌ها را تست کن:

```bash
curl -I http://localhost/api/public/posts
curl -I http://localhost/api/public/posts
curl -I -H "Authorization: Bearer test" http://localhost/api/public/posts
```

ببین cache status چطور تغییر می‌کند.

---
