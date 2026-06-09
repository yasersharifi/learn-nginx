---
title: "15. Pipe و Redirect"
description: "15. Pipe و Redirect"
---

# 15. Pipe و Redirect

### ارسال خروجی یک دستور به دستور بعدی

```bash
ps aux | grep node
```

### ذخیره خروجی در فایل

```bash
ls -la > files.txt
```

### اضافه کردن خروجی به آخر فایل

```bash
echo "Deploy started" >> deploy.log
```

### ذخیره خطاها همزمان با خروجی

```bash
npm run build > build.log 2>&1
```

### دیدن خروجی و ذخیره همزمان

```bash
npm run build 2>&1 | tee build.log
```

---
