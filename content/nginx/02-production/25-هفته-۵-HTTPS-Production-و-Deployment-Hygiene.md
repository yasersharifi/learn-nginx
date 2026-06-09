---
title: "هفته ۵: HTTPS Production و Deployment Hygiene"
description: "هفته ۵: HTTPS Production و Deployment Hygiene"
---

# هفته ۵: HTTPS Production و Deployment Hygiene

## روز ۲۱: HTTPS جدی‌تر

در فاز ۱ self-signed کافی بود. در production باید certificate معتبر داشته باشی.

روش رایج:

```text
Let's Encrypt + Certbot
```

روی Ubuntu معمولاً:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com
```

بعد renew را بررسی کن:

```bash
sudo systemctl status certbot.timer
```

تست renew:

```bash
sudo certbot renew --dry-run
```

## نکته

برای production واقعی باید قبل از فعال‌سازی HSTS، مطمئن باشی:

```text
[ ] certificate معتبر است
[ ] auto-renew کار می‌کند
[ ] همه subdomainهای لازم HTTPS دارند
[ ] redirectها درست‌اند
```

---
