---
title: "9. استفاده از HEAD با reset"
description: "9. استفاده از HEAD با reset"
---

# 9. استفاده از HEAD با reset

`HEAD` خیلی وقت‌ها با `git reset` استفاده می‌شود.

### حذف آخرین commit ولی نگه داشتن تغییرات در stage

```bash
git reset --soft HEAD~1
```

کاربرد:

> آخرین commit حذف می‌شود، اما تغییرات همچنان staged می‌مانند.

---

### حذف آخرین commit و نگه داشتن تغییرات در working directory

```bash
git reset --mixed HEAD~1
```

یا ساده‌تر:

```bash
git reset HEAD~1
```

کاربرد:

> آخرین commit حذف می‌شود، تغییرات باقی می‌مانند، ولی staged نیستند.

---

### حذف آخرین commit و پاک کردن تغییرات

```bash
git reset --hard HEAD~1
```

هشدار:

> این دستور تغییرات را واقعاً پاک می‌کند. با احتیاط استفاده کن.

---
