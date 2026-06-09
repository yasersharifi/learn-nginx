---
title: "10. سناریو: push امن بعد از rebase"
description: "10. سناریو: push امن بعد از rebase"
---

# 10. سناریو: push امن بعد از rebase

### جواب

```bash
git push --force-with-lease
```

این از `--force` امن‌تر است، چون اگر کسی قبل از تو روی remote چیزی push کرده باشد، Git اجازه نمی‌دهد کار او را overwrite کنی.

---
