---
title: "11. اگر بعد از Rebase نتوانستی Push کنی"
description: "11. اگر بعد از Rebase نتوانستی Push کنی"
---

# 11. اگر بعد از Rebase نتوانستی Push کنی

چون rebase تاریخچه را بازنویسی می‌کند، ممکن است push معمولی رد شود.

در این حالت، برای branch شخصی خودت از این استفاده کن:

```bash
git push --force-with-lease
```

از این کمتر استفاده کن:

```bash
git push --force
```

چون `--force-with-lease` امن‌تر است. اگر کسی قبل از تو چیزی push کرده باشد، جلوی overwrite شدن کار او را می‌گیرد.

---
