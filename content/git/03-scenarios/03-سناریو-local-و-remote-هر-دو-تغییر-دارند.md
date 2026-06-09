---
title: "3. سناریو: local و remote هر دو تغییر دارند"
description: "3. سناریو: local و remote هر دو تغییر دارند"
---

# 3. سناریو: local و remote هر دو تغییر دارند

### جواب

این وضعیت **divergent branches** است.

یعنی local و remote از یک نقطه مشترک جدا شده‌اند و هرکدام commitهایی دارند که دیگری ندارد.

```txt
local فقط D را دارد.
remote فقط C را دارد.
```

در این حالت fast-forward ممکن نیست و باید بین **merge** و **rebase** تصمیم بگیری.

---
