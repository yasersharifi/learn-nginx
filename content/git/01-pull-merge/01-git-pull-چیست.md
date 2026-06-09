---
title: "1. git pull چیست؟"
description: "1. git pull چیست؟"
---

# 1. git pull چیست؟

دستور `git pull` یعنی:

> آخرین تغییرات branch ریموت را بگیر و با branch لوکال من یکی کن.

در واقع `git pull` ترکیبی از دو کار است:

```bash
git fetch
git merge
```

یا اگر با rebase استفاده شود:

```bash
git fetch
git rebase
```

پس وقتی می‌زنی:

```bash
git pull
```

Git اول تغییرات remote را می‌گیرد، بعد باید تصمیم بگیرد چطور آن‌ها را با تغییرات local یکی کند.

---
