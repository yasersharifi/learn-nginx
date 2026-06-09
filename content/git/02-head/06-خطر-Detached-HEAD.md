---
title: "6. خطر Detached HEAD"
description: "6. خطر Detached HEAD"
---

# 6. خطر Detached HEAD

اگر در حالت detached HEAD تغییر بدهی و commit بزنی، آن commit روی هیچ branch مشخصی نیست.

یعنی ممکن است بعداً راحت گم شود.

برای جلوگیری از این مشکل، اگر تغییر مهمی دادی، سریع یک branch بساز:

```bash
git switch -c my-new-branch
```

یا با دستور قدیمی‌تر:

```bash
git checkout -b my-new-branch
```

---
