---
title: "تصویر ذهنی درست از Nginx"
description: "تصویر ذهنی درست از Nginx"
---

# تصویر ذهنی درست از Nginx

اول باید جایگاه Nginx را بفهمی.

معمولاً کاربر مستقیم با اپلیکیشن تو حرف نمی‌زند. درخواست اول به Nginx می‌رسد، بعد Nginx تصمیم می‌گیرد با آن چه کند.

```text
User / Browser
      ↓
    Nginx
      ↓
Application Server
Node.js / Next.js / Django / Laravel / Go / ...
```

Nginx می‌تواند چند نقش داشته باشد:

```text
Nginx as:
- Web Server
- Reverse Proxy
- Load Balancer
- SSL/TLS Terminator
- Static File Server
- Cache Layer
- Security Gate
- API Gateway سبک
```

در فاز ۱ فعلاً فقط این نقش‌ها را جدی می‌گیریم:

```text
- Web Server
- Reverse Proxy
- Static File Server
- Basic Load Balancer
- Basic HTTPS Gateway
```

---
