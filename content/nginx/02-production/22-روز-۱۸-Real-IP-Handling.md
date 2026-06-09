---
title: "روز ۱۸: Real IP Handling"
description: "روز ۱۸: Real IP Handling"
---

# روز ۱۸: Real IP Handling

اگر Nginx پشت Cloudflare، AWS ELB، Kubernetes ingress یا یک load balancer دیگر باشد، `$remote_addr` ممکن است IP واقعی کاربر نباشد.

مثلاً:

```text
User
  ↓
Cloudflare
  ↓
Nginx
  ↓
App
```

از دید Nginx، client ممکن است Cloudflare باشد، نه user.

Config concept:

```nginx
set_real_ip_from 10.0.0.0/8;
real_ip_header X-Forwarded-For;
real_ip_recursive on;
```

## هشدار بسیار مهم

هرگز کورکورانه این کار را نکن:

```nginx
set_real_ip_from 0.0.0.0/0;
```

چون در این صورت هر client می‌تواند `X-Forwarded-For` جعلی بفرستد و IP خودش را جعل کند.

فقط IPهای trusted proxy را داخل `set_real_ip_from` بگذار.

---
