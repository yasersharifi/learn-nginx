---
title: "8. کاربردهای رایج HEAD"
description: "8. کاربردهای رایج HEAD"
---

# 8. کاربردهای رایج HEAD

### دیدن آخرین commit

```bash
git show HEAD
```

### دیدن commit قبلی

```bash
git show HEAD~1
```

### دیدن چند commit آخر

```bash
git log --oneline
```

### برگشت دادن یک فایل به وضعیت آخرین commit

```bash
git restore file.txt
```

یا روش قدیمی‌تر:

```bash
git checkout HEAD -- file.txt
```

---
