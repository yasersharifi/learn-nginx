---
title: "31. Firewall ساده با UFW"
description: "31. Firewall ساده با UFW"
---

# 31. Firewall ساده با UFW

### وضعیت firewall

```bash
sudo ufw status
```

### اجازه SSH

```bash
sudo ufw allow ssh
```

### اجازه HTTP و HTTPS

```bash
sudo ufw allow 80
sudo ufw allow 443
```

### فعال کردن firewall

```bash
sudo ufw enable
```

### حذف rule

```bash
sudo ufw delete allow 3000
```

> قبل از فعال کردن firewall مطمئن شوید SSH باز است، وگرنه ممکن است دسترسی به سرور را از دست بدهید.

---
