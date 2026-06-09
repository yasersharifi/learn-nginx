---
title: "22. خواندن لاگ سرویس‌ها با journalctl"
description: "22. خواندن لاگ سرویس‌ها با journalctl"
---

# 22. خواندن لاگ سرویس‌ها با journalctl

### لاگ یک سرویس

```bash
sudo journalctl -u nginx
```

### لاگ زنده

```bash
sudo journalctl -u nginx -f
```

### لاگ از boot فعلی

```bash
sudo journalctl -u nginx -b
```

### دیدن آخرین ۱۰۰ خط

```bash
sudo journalctl -u nginx -n 100
```

مثال برای سرویس Node.js:

```bash
sudo journalctl -u my-api -f
```

---
