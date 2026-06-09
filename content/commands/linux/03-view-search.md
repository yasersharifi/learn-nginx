---
title: "مشاهده و جستجو"
description: "cat، less، tail، grep، find — خواندن فایل و پیدا کردن متن"
---

# مشاهده و جستجو

## مشاهده

| دستور | کاربرد |
| --- | --- |
| `cat file` | نمایش کل فایل |
| `less file` | صفحه‌به‌صفحه (`q` خروج، `/` جستجو) |
| `head -n 50 file` | ۵۰ خط اول |
| `tail -n 100 file` | ۱۰۰ خط آخر |
| `tail -f file` | دنبال کردن log زنده |
| `tail -f /var/log/nginx/error.log` | log زنده Nginx |

## grep

| دستور | کاربرد |
| --- | --- |
| `grep "ERROR" app.log` | جستجو در فایل |
| `grep -i "error" app.log` | بدون حساسیت به حروف |
| `grep -n "TODO" file` | با شماره خط |
| `grep -r "API_URL" .` | جستجوی بازگشتی |
| `grep -R "text" . --exclude-dir=node_modules` | بدون node_modules |
| `ps aux \| grep nginx` | فیلتر خروجی pipe |

## find

| دستور | کاربرد |
| --- | --- |
| `find . -name "*.md"` | پیدا کردن با نام |
| `find . -name ".env*"` | فایل‌های env |
| `find . -type f -size +100M` | فایل‌های بزرگ |
| `find . -type f -mtime -1` | تغییر در ۲۴ ساعت گذشته |

```bash
rg "pattern" src/    # ripgrep — سریع‌تر از grep در پروژه
```
