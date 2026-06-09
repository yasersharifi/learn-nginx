---
title: "21. systemd و مدیریت سرویس‌ها"
description: "21. systemd و مدیریت سرویس‌ها"
---

# 21. systemd و مدیریت سرویس‌ها

بسیاری از سرویس‌ها در لینوکس با `systemd` مدیریت می‌شوند.

### وضعیت سرویس

```bash
sudo systemctl status nginx
```

### شروع سرویس

```bash
sudo systemctl start nginx
```

### توقف سرویس

```bash
sudo systemctl stop nginx
```

### ری‌استارت سرویس

```bash
sudo systemctl restart nginx
```

### reload بدون قطع کامل

```bash
sudo systemctl reload nginx
```

### فعال کردن اجرا بعد از reboot

```bash
sudo systemctl enable nginx
```

### غیرفعال کردن اجرا بعد از reboot

```bash
sudo systemctl disable nginx
```

---
