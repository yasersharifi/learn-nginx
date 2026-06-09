---
title: "1. HEAD دقیقاً به چه چیزی اشاره می‌کند؟"
description: "1. HEAD دقیقاً به چه چیزی اشاره می‌کند؟"
---

# 1. HEAD دقیقاً به چه چیزی اشاره می‌کند؟

در حالت معمول، `HEAD` مستقیم به commit اشاره نمی‌کند؛ بلکه به branch فعلی اشاره می‌کند، و آن branch به آخرین commit خودش اشاره دارد.

مثلاً:

```txt
HEAD -> main -> C
```

یعنی:

- `HEAD` به branch `main` اشاره می‌کند.
- `main` به commit آخر خودش اشاره می‌کند.
- commit آخر در این مثال `C` است.

وقتی commit جدید می‌زنی:

```bash
git commit -m "add nginx config"
```

branch جلو می‌رود و `HEAD` هم همراه آن جلو می‌رود.

قبل:

```txt
main: A---B---C
              ^
             HEAD
```

بعد:

```txt
main: A---B---C---D
                  ^
                 HEAD
```

---
