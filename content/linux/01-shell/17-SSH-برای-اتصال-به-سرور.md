---
title: "17. SSH برای اتصال به سرور"
description: "17. SSH برای اتصال به سرور"
---

# 17. SSH برای اتصال به سرور

### اتصال ساده

```bash
ssh ubuntu@SERVER_IP
```

### اتصال با private key

```bash
ssh -i ~/.ssh/my-key.pem ubuntu@SERVER_IP
```

### تنظیم permission کلید

```bash
chmod 600 ~/.ssh/my-key.pem
```

### کپی فایل به سرور با scp

```bash
scp ./app.tar.gz ubuntu@SERVER_IP:/home/ubuntu/
```

### کپی فایل از سرور به سیستم خودتان

```bash
scp ubuntu@SERVER_IP:/var/log/nginx/error.log ./error.log
```

---
