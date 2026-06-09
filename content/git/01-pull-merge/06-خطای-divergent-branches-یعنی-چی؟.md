---
title: "6. خطای divergent branches یعنی چی؟"
description: "6. خطای divergent branches یعنی چی؟"
---

# 6. خطای divergent branches یعنی چی؟

ممکن است موقع `git pull` این خطا را ببینی:

```txt
hint: You have divergent branches and need to specify how to reconcile them.
fatal: Need to specify how to reconcile divergent branches.
```

یعنی:

> هم branch لوکال تو commit جدید دارد، هم branch ریموت. Git نمی‌داند باید merge کند یا rebase.

برای حل آن باید یکی از این‌ها را انتخاب کنی.

### راه‌حل با Rebase

```bash
git pull --rebase
```

یا دقیق‌تر:

```bash
git fetch origin
git rebase origin/main
```

اگر branch اصلی پروژه `master` است:

```bash
git fetch origin
git rebase origin/master
```

### راه‌حل با Merge

```bash
git pull --no-rebase
```

یا:

```bash
git fetch origin
git merge origin/main
```

### راه‌حل با Fast-Forward Only

```bash
git pull --ff-only
```

این یعنی:

> فقط اگر fast-forward ممکن بود pull کن. اگر branchها جدا شده‌اند، خطا بده.

---
