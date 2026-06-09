---
title: "روز ۱۱: Proxy Cache"
description: "روز ۱۱: Proxy Cache"
---

# روز ۱۱: Proxy Cache

Nginx می‌تواند responseهای upstream را cache کند.

داخل `http` context:

```nginx
proxy_cache_path /var/cache/nginx/app_cache
    levels=1:2
    keys_zone=app_cache:10m
    max_size=1g
    inactive=60m
    use_temp_path=off;
```

داخل `location`:

```nginx
location /api/public/ {
    proxy_pass http://api_backend/;

    proxy_cache app_cache;
    proxy_cache_valid 200 10m;
    proxy_cache_valid 404 1m;

    add_header X-Cache-Status $upstream_cache_status;

    include snippets/proxy-headers.conf;
}
```

## معنی

| Directive                | معنی                                         |
| ------------------------ | -------------------------------------------- |
| `proxy_cache_path`       | مسیر و zone cache                            |
| `keys_zone`              | shared memory zone برای metadata             |
| `max_size`               | حداکثر حجم cache                             |
| `inactive`               | حذف آیتم‌هایی که مدت طولانی استفاده نشده‌اند |
| `proxy_cache_valid`      | مدت cache برای statusهای مختلف               |
| `$upstream_cache_status` | وضعیت cache: HIT, MISS, BYPASS, EXPIRED      |

## تست

```bash
curl -I http://localhost/api/public/posts
curl -I http://localhost/api/public/posts
```

بار اول احتمالاً:

```text
X-Cache-Status: MISS
```

بار دوم:

```text
X-Cache-Status: HIT
```

## هشدار

هر چیزی را cache نکن.

نباید cache کنی:

```text
- endpointهای user-specific
- dashboard شخصی
- اطلاعات محرمانه
- responseهایی با Authorization
- payment
- admin API
```

برای cache کردن API باید دقیق بدانی response عمومی است یا خصوصی.

---
