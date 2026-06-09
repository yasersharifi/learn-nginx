---
title: "هفته ۴: Rate Limiting، Security Headers و Observability"
description: "هفته ۴: Rate Limiting، Security Headers و Observability"
---

# هفته ۴: Rate Limiting، Security Headers و Observability

## روز ۱۵: Rate Limiting

Rate limit برای کنترل abuse و burst مهم است.

داخل `http` context:

```nginx
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
```

داخل location:

```nginx
location /api/ {
    limit_req zone=api_limit burst=20 nodelay;

    proxy_pass http://api_backend/;
    include snippets/proxy-headers.conf;
}
```

## معنی

| بخش                   | معنی                                               |
| --------------------- | -------------------------------------------------- |
| `$binary_remote_addr` | IP client به شکل compact                           |
| `zone=api_limit:10m`  | shared memory zone برای tracking                   |
| `rate=10r/s`          | ۱۰ request در ثانیه                                |
| `burst=20`            | اجازه burst موقت                                   |
| `nodelay`             | requestهای burst را معطل نکن؛ یا قبول یا reject کن |

## تست

```bash
for i in {1..100}; do curl -s -o /dev/null -w "%{http_code}\n" http://localhost/api/test; done
```

باید بخشی از requestها `503` یا status مربوط به limit ببینند.

برای status سفارشی:

```nginx
limit_req_status 429;
```

بهتر:

```nginx
limit_req_status 429;
```

حالا rate limit response با `429 Too Many Requests` برمی‌گردد.

---
