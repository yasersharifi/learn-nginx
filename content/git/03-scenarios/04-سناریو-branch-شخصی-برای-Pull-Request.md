---
title: "4. سناریو: branch شخصی برای Pull Request"
description: "4. سناریو: branch شخصی برای Pull Request"
---

# 4. سناریو: branch شخصی برای Pull Request

### جواب

برای branch شخصی، معمولاً `rebase` مناسب‌تر است:

```bash
git pull --rebase
```

یا دقیق‌تر:

```bash
git fetch origin
git rebase origin/main
```

چون rebase commitهای تو را روی آخرین نسخه remote می‌چیند و history خطی‌تر می‌ماند.

---
