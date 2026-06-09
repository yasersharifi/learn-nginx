---
title: "5. Detached HEAD چیست؟"
description: "5. Detached HEAD چیست؟"
---

# 5. Detached HEAD چیست؟

`detached HEAD` یعنی:

> `HEAD` دیگر به branch وصل نیست؛ مستقیم روی یک commit خاص ایستاده است.

مثلاً اگر بزنی:

```bash
git checkout a1b2c3d
```

یا:

```bash
git switch --detach a1b2c3d
```

Git ممکن است بگوید:

```txt
You are in 'detached HEAD' state
```

یعنی الان روی یک commit خاص هستی، نه روی یک branch.

مثلاً:

```txt
main: A---B---C---D
          ^
         HEAD
```

اینجا `HEAD` مستقیم روی commit `B` است.

---
