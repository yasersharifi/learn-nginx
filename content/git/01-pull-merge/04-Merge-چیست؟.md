---
title: "4. Merge چیست؟"
description: "4. Merge چیست؟"
---

# 4. Merge چیست؟

`merge` یعنی Git دو مسیر جداشده را با یک commit جدید یکی کند.

مثلاً:

```txt
local:  A---B---D
remote: A---B---C
```

اگر merge انجام شود:

```bash
git pull --no-rebase
```

یا:

```bash
git merge origin/main
```

نتیجه چیزی شبیه این می‌شود:

```txt
A---B---D---M
     \---C---/
```

اینجا `M` یک **merge commit** است.

یعنی Git می‌گوید:

> دو مسیر جدا بودند؛ من آن‌ها را با یک commit جدید ترکیب کردم.

### مزیت Merge

- history واقعی پروژه حفظ می‌شود.
- برای branchهای مشترک و تیمی امن‌تر است.
- commitهای قبلی بازنویسی نمی‌شوند.

### عیب Merge

- history ممکن است شلوغ‌تر شود.
- merge commitهای زیاد می‌توانند خواندن تاریخچه را سخت‌تر کنند.

---
