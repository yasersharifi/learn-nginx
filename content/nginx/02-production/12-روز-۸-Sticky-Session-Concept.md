---
title: "روز ۸: Sticky Session Concept"
description: "روز ۸: Sticky Session Concept"
---

# روز ۸: Sticky Session Concept

در Nginx open source، sticky session رسمی مثل NGINX Plus ساده و آماده نیست، اما می‌توانی با `ip_hash` رفتار نزدیک بسازی.

```nginx
upstream app_backend {
    ip_hash;

    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
```

## معنی

بر اساس IP client، requestها معمولاً به یک backend ثابت می‌روند.

## مشکل

اگر همه کاربران پشت NAT، Cloudflare یا load balancer بالادستی باشند، IP ممکن است واقعی نباشد یا همه کاربران شبیه هم دیده شوند.

پس `ip_hash` همیشه راه‌حل خوب نیست.

## توصیه

اگر اپلیکیشن session state دارد، بهتر است state را از process خارج کنی:

```text
App Instance 1
App Instance 2
App Instance 3
   ↓
Redis / Database / External Session Store
```

این بهتر از وابسته شدن به sticky session است.

---
