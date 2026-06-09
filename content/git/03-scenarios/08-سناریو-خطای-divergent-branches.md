---
title: "8. سناریو: خطای divergent branches"
description: "8. سناریو: خطای divergent branches"
---

# 8. سناریو: خطای divergent branches

### جواب

یعنی local و remote هر دو commitهایی دارند که طرف مقابل ندارد.

Git نمی‌داند باید این دو مسیر را با **merge** یکی کند یا با **rebase**.

برای حلش باید یکی را مشخص کنی:

```bash
git pull --rebase
```

یا:

```bash
git pull --no-rebase
```

یا اگر فقط fast-forward را قبول داری:

```bash
git pull --ff-only
```

---
