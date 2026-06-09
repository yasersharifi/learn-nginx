---
title: "14. سناریو: تیم history واقعی mergeها را می‌خواهد"
description: "14. سناریو: تیم history واقعی mergeها را می‌خواهد"
---

# 14. سناریو: تیم history واقعی mergeها را می‌خواهد

### جواب

```bash
git config --global pull.rebase false
```

یعنی `git pull` به صورت پیش‌فرض merge انجام می‌دهد، نه rebase.

این انتخاب برای branchهای مشترک تیمی امن‌تر است.

---
