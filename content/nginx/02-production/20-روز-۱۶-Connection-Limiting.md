---
title: "روز ۱۶: Connection Limiting"
description: "روز ۱۶: Connection Limiting"
---

# روز ۱۶: Connection Limiting

Rate limit تعداد requestها را کنترل می‌کند. Connection limit تعداد connectionهای همزمان را.

داخل `http`:

```nginx
limit_conn_zone $binary_remote_addr zone=conn_limit:10m;
```

داخل `server` یا `location`:

```nginx
limit_conn conn_limit 20;
```

یعنی هر IP حداکثر ۲۰ connection همزمان داشته باشد.

## استفاده پیشنهادی

```nginx
location /api/ {
    limit_conn conn_limit 20;
    limit_req zone=api_limit burst=20 nodelay;

    proxy_pass http://api_backend/;
    include snippets/proxy-headers.conf;
}
```

## هشدار

اگر کاربران پشت NAT یا proxy مشترک باشند، محدودیت بر اساس IP می‌تواند کاربران واقعی را اذیت کند.

اگر پشت Cloudflare یا load balancer هستی، باید real IP را درست تنظیم کنی، وگرنه همه requestها از IP proxy دیده می‌شوند.

---
