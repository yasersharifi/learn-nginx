---
title: "20. سناریو: توصیه اشتباه درباره rebase"
description: "20. سناریو: توصیه اشتباه درباره rebase"
---

# 20. سناریو: توصیه اشتباه درباره rebase

### جواب

نه، این توصیه همیشه درست نیست.

`rebase` history را بازنویسی می‌کند. اگر branch مشترک باشد و افراد دیگر هم روی همان branch کار کنند، rebase می‌تواند باعث شود commitهای remote و local افراد با هم ناسازگار شوند.

برای branch شخصی:

```bash
git pull --rebase
```

معمولاً خوب است.

برای branch مشترک تیمی:

```bash
git pull --no-rebase
```

معمولاً امن‌تر است.

**خلاصه:** branch شخصی ← rebase · branch مشترک ← merge · محافظه‌کار ← ff-only

---
