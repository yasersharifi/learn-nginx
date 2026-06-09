---
title: "3. وقتی Fast-Forward ممکن نیست"
description: "3. وقتی Fast-Forward ممکن نیست"
---

# 3. وقتی Fast-Forward ممکن نیست

گاهی هم تو روی branch لوکال commit داده‌ای، هم remote commit جدید دارد.

مثلاً:

```txt
local:  A---B---D
remote: A---B---C
```

اینجا branchها از هم جدا شده‌اند.

به این حالت می‌گویند:

```txt
divergent branches
```

یعنی:

> لوکال و ریموت هر دو تغییراتی دارند که طرف مقابل ندارد.

در این حالت Git نمی‌تواند فقط branch را جلو ببرد. پس باید یکی از این دو کار را انجام دهد:

1. `merge`
2. `rebase`

---
