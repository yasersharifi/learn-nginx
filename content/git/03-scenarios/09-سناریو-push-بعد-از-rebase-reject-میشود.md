---
title: "9. سناریو: push بعد از rebase reject می‌شود"
description: "9. سناریو: push بعد از rebase reject می‌شود"
---

# 9. سناریو: push بعد از rebase reject می‌شود

### جواب

چون `rebase` تاریخچه را بازنویسی می‌کند.

Commit قبلی تو مثلاً `D` بوده، اما بعد از rebase تبدیل شده به commit جدیدی مثل `D'`.

حتی اگر محتوای commit یکی باشد، hash آن تغییر کرده است.

```txt
قبل:

A---B---D

بعد از rebase:

A---B---C---D'
```

پس remote هنوز commit قدیمی را می‌شناسد، ولی local commit جدیدی دارد. به همین دلیل push معمولی ممکن است reject شود.

---
