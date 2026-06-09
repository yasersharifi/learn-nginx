---
title: "35. اسکریپت ساده deploy"
description: "35. اسکریپت ساده deploy"
---

# 35. اسکریپت ساده deploy

نمونه `deploy.sh`:

```bash
#!/usr/bin/env bash
set -e

echo "Pull latest code"
git pull

echo "Install dependencies"
pnpm install

echo "Build app"
pnpm build

echo "Restart service"
pm2 restart my-app

echo "Deploy completed"
```

قابل اجرا کردن:

```bash
chmod +x deploy.sh
```

اجرا:

```bash
./deploy.sh
```

نکته مهم:

```bash
set -e
```

باعث می‌شود اگر یک دستور fail شد، اسکریپت ادامه پیدا نکند.

---
