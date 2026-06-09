---
title: "5. سناریو: branch مشترک تیمی"
description: "5. سناریو: branch مشترک تیمی"
---

# 5. سناریو: branch مشترک تیمی

### جواب

در branch مشترک تیمی معمولاً **merge** امن‌تر است.

```bash
git pull --no-rebase
```

یا:

```bash
git fetch origin
git merge origin/develop
```

دلیلش این است که merge تاریخچه را بازنویسی نمی‌کند، ولی rebase commitها را دوباره می‌سازد و ممکن است برای بقیه مشکل ایجاد کند.

---
