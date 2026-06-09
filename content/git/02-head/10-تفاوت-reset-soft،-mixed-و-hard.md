---
title: "10. تفاوت reset soft، mixed و hard"
description: "10. تفاوت reset soft، mixed و hard"
---

# 10. تفاوت reset soft، mixed و hard

```txt
--soft   = commit حذف می‌شود، تغییرات staged می‌مانند
--mixed  = commit حذف می‌شود، تغییرات unstaged می‌شوند
--hard   = commit و تغییرات هر دو پاک می‌شوند
```

مثلاً اگر آخرین commit اشتباه بوده ولی کد را می‌خواهی نگه داری:

```bash
git reset --soft HEAD~1
```

اگر commit اشتباه بوده و می‌خواهی تغییرات را دوباره بررسی کنی:

```bash
git reset HEAD~1
```

اگر commit و تغییرات هر دو اشتباه بوده‌اند و می‌خواهی کامل حذفشان کنی:

```bash
git reset --hard HEAD~1
```

---
