---
title: "13. سناریو: pull همیشه با rebase باشد"
description: "13. سناریو: pull همیشه با rebase باشد"
---

# 13. سناریو: pull همیشه با rebase باشد

### جواب

```bash
git config --global pull.rebase true
```

بعد از این، `git pull` به صورت پیش‌فرض مثل `git pull --rebase` رفتار می‌کند.

این تنظیم برای کسانی که بیشتر روی branchهای شخصی و Pull Request کار می‌کنند مفید است.

---
