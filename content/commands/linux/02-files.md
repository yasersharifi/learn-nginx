---
title: "فایل و پوشه"
description: "mkdir، cp، mv، rm، touch — ساخت و مدیریت فایل"
---

# فایل و پوشه

| دستور | کاربرد |
| --- | --- |
| `mkdir dir` | ساخت پوشه |
| `mkdir -p a/b/c` | ساخت مسیر چندمرحله‌ای |
| `touch file.txt` | فایل خالی یا به‌روز timestamp |
| `cp src dst` | کپی فایل |
| `cp -r src/ dst/` | کپی پوشه |
| `mv old new` | انتقال یا تغییر نام |
| `rm file` | حذف فایل |
| `rm -r dir` | حذف پوشه |
| `rm -rf dir` | حذف اجباری — **خطرناک** |

```bash
# آرشیو
tar -czvf backup.tar.gz ./app/
tar -xzvf backup.tar.gz

zip -r app.zip app/
unzip app.zip
```
