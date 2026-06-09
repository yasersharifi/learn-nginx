---
title: "7. تنظیم پیش‌فرض Git برای pull"
description: "7. تنظیم پیش‌فرض Git برای pull"
---

# 7. تنظیم پیش‌فرض Git برای pull

Git از تو می‌خواهد مشخص کنی که پیش‌فرض pull چه باشد.

### پیش‌فرض روی Merge

```bash
git config --global pull.rebase false
```

یعنی `git pull` به صورت پیش‌فرض merge کند.

### پیش‌فرض روی Rebase

```bash
git config --global pull.rebase true
```

یعنی `git pull` به صورت پیش‌فرض rebase کند.

### پیش‌فرض روی Fast-Forward Only

```bash
git config --global pull.ff only
```

یعنی فقط وقتی pull انجام شود که fast-forward ممکن باشد.

---
