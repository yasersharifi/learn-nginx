---
title: "4. HEAD^ یعنی چی؟"
description: "4. HEAD^ یعنی چی؟"
---

# 4. HEAD^ یعنی چی؟

`HEAD^` هم معمولاً یعنی parent قبلی `HEAD`.

در تاریخچه ساده، این دو تقریباً یکی هستند:

```bash
HEAD^
HEAD~1
```

هر دو یعنی یک commit قبل.

اما در merge commit فرق می‌کنند.

مثلاً:

```txt
A---B---D---M
     \---C---/
```

اینجا `M` یک merge commit است و دو parent دارد.

```bash
HEAD^1
```

یعنی parent اول.

```bash
HEAD^2
```

یعنی parent دوم.

برای کارهای روزمره، معمولاً `HEAD~1` واضح‌تر و کاربردی‌تر است.

---
