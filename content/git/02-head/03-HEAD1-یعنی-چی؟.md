---
title: "3. HEAD~1 یعنی چی؟"
description: "3. HEAD~1 یعنی چی؟"
---

# 3. HEAD~1 یعنی چی؟

`HEAD~1` یعنی:

> یک commit قبل از HEAD

مثلاً:

```txt
A---B---C---D
            ^
           HEAD
```

در این حالت:

```txt
HEAD    = D
HEAD~1  = C
HEAD~2  = B
HEAD~3  = A
```

مثال:

```bash
git show HEAD
```

آخرین commit را نشان می‌دهد.

```bash
git show HEAD~1
```

commit قبلی را نشان می‌دهد.

```bash
git show HEAD~2
```

دو commit قبل‌تر را نشان می‌دهد.

---
