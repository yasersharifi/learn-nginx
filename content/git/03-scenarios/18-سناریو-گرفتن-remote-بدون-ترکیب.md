---
title: "18. سناریو: گرفتن remote بدون ترکیب"
description: "18. سناریو: گرفتن remote بدون ترکیب"
---

# 18. سناریو: گرفتن remote بدون ترکیب

### جواب

```bash
git fetch origin
```

`fetch` تغییرات remote را می‌گیرد، اما آن‌ها را با branch فعلی تو merge یا rebase نمی‌کند.

بعد از fetch می‌توانی تصمیم بگیری:

```bash
git rebase origin/main
```

یا:

```bash
git merge origin/main
```

---
