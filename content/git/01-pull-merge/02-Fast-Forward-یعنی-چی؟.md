---
title: "2. Fast-Forward یعنی چی؟"
description: "2. Fast-Forward یعنی چی؟"
---

# 2. Fast-Forward یعنی چی؟

`fast-forward` ساده‌ترین حالت آپدیت شدن branch است.

فرض کن branch لوکال تو اینجاست:

```txt
local:  A---B
```

ولی روی remote یک commit جدید آمده:

```txt
remote: A---B---C
```

تو روی لوکال commit جدیدی نداده‌ای. فقط عقب‌تر از remote هستی.

در این حالت Git فقط اشاره‌گر branch تو را جلو می‌برد:

```txt
local:  A---B---C
```

این می‌شود **fast-forward**.

یعنی:

> Git هیچ commit جدیدی نمی‌سازد؛ فقط branch را جلو می‌برد.

### ویژگی‌های Fast-Forward

- history تمیز می‌ماند.
- merge commit ساخته نمی‌شود.
- معمولاً conflict ندارد.
- فقط وقتی ممکن است که branch لوکال از remote جدا نشده باشد.

---
