---
title: "پکیج و محیط"
description: "apt، env، pipe، redirect — نصب نرم‌افزار و متغیر محیطی"
---

# پکیج و محیط

## apt (Ubuntu/Debian)

| دستور | کاربرد |
| --- | --- |
| `sudo apt update` | به‌روز لیست پکیج |
| `sudo apt upgrade` | آپگرید |
| `sudo apt install nginx` | نصب |
| `sudo apt remove nginx` | حذف |
| `sudo apt install -y pkg` | بدون تأیید |
| `dpkg -l \| grep nginx` | پکیج نصب‌شده |

## env و shell

| دستور | کاربرد |
| --- | --- |
| `env` | همه متغیرها |
| `env \| grep NODE` | فیلتر |
| `export VAR=value` | تعریف موقت |
| `VAR=1 cmd` | env فقط برای یک دستور |
| `echo $PATH` | مقدار متغیر |

## pipe و redirect

| دستور | کاربرد |
| --- | --- |
| `cmd1 \| cmd2` | خروجی به ورودی بعدی |
| `cmd > file` | redirect خروجی |
| `cmd >> file` | append |
| `cmd 2>&1` | stderr به stdout |
| `cmd > log 2>&1` | همه در فایل |
| `cmd 2>&1 \| tee log` | نمایش + ذخیره |

## ویرایشگر

| دستور | کاربرد |
| --- | --- |
| `nano file` | ویرایش ساده (`Ctrl+O` ذخیره، `Ctrl+X` خروج) |
| `vim file` | ویرایش پیشرفته (`i` insert، `:wq` ذخیره و خروج) |

```bash
node -v && npm -v && git --version && nginx -v
```
