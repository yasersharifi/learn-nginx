---
title: "26. PM2 برای اجرای Node.js در سرور"
description: "26. PM2 برای اجرای Node.js در سرور"
---

# 26. PM2 برای اجرای Node.js در سرور

PM2 برای نگه داشتن اپلیکیشن Node.js در background استفاده می‌شود.

### نصب

```bash
npm install -g pm2
```

### اجرای اپ

```bash
pm2 start npm --name my-app -- start
```

### لیست پروسس‌ها

```bash
pm2 list
```

### دیدن لاگ‌ها

```bash
pm2 logs my-app
```

### ری‌استارت

```bash
pm2 restart my-app
```

### توقف

```bash
pm2 stop my-app
```

### اجرای خودکار بعد از reboot

```bash
pm2 startup
pm2 save
```

---
