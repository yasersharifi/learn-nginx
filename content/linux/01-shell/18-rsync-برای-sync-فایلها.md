---
title: "18. rsync برای sync فایل‌ها"
description: "18. rsync برای sync فایل‌ها"
---

# 18. rsync برای sync فایل‌ها

`rsync` برای deploy ساده یا sync فایل‌ها بهتر از `scp` است.

```bash
rsync -avz ./dist/ ubuntu@SERVER_IP:/var/www/my-app/
```

حذف فایل‌هایی که در source دیگر وجود ندارند:

```bash
rsync -avz --delete ./dist/ ubuntu@SERVER_IP:/var/www/my-app/
```

---
