---
title: "7. سناریو: تنظیم دائمی fast-forward only"
description: "7. سناریو: تنظیم دائمی fast-forward only"
---

# 7. سناریو: تنظیم دائمی fast-forward only

### جواب

```bash
git config --global pull.ff only
```

بعد از این، `git pull` فقط وقتی موفق می‌شود که fast-forward ممکن باشد.

اگر branchها divergent باشند، Git خطا می‌دهد و تو باید آگاهانه تصمیم بگیری:

```bash
git pull --rebase
```

یا:

```bash
git pull --no-rebase
```

---
