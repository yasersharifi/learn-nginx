---
title: "10. اگر هنگام Rebase conflict پیش آمد"
description: "10. اگر هنگام Rebase conflict پیش آمد"
---

# 10. اگر هنگام Rebase conflict پیش آمد

وقتی conflict رخ می‌دهد، Git rebase را متوقف می‌کند.

اول فایل‌های conflictدار را باز کن و مشکل را حل کن.

بعد:

```bash
git add .
git rebase --continue
```

اگر خواستی کل rebase را لغو کنی:

```bash
git rebase --abort
```

---
