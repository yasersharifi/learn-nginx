---
title: "32. مانیتورینگ سریع production issue"
description: "32. مانیتورینگ سریع production issue"
---

# 32. مانیتورینگ سریع production issue

وقتی اپلیکیشن روی سرور مشکل دارد، این ترتیب معمولاً خوب جواب می‌دهد:

### 1. وضعیت سرویس

```bash
sudo systemctl status my-api
```

یا اگر PM2 است:

```bash
pm2 list
```

### 2. لاگ سرویس

```bash
sudo journalctl -u my-api -n 100
```

یا:

```bash
pm2 logs my-api
```

### 3. بررسی پورت

```bash
sudo lsof -i :3000
```

### 4. تست local

```bash
curl http://localhost:3000/health
```

### 5. تست از بیرون با دامنه

```bash
curl -I https://example.com
```

### 6. بررسی Nginx

```bash
sudo nginx -t
sudo systemctl status nginx
sudo tail -f /var/log/nginx/error.log
```

### 7. بررسی منابع

```bash
df -h
free -h
top
```

---
