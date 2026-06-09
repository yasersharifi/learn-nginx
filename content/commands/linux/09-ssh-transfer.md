---
title: "SSH و انتقال فایل"
description: "ssh، scp، rsync — اتصال به سرور و sync فایل"
---

# SSH و انتقال فایل

## SSH

| دستور | کاربرد |
| --- | --- |
| `ssh user@SERVER_IP` | اتصال |
| `ssh -i ~/.ssh/key.pem user@IP` | با کلید خصوصی |
| `chmod 600 ~/.ssh/key.pem` | مجوز درست کلید |

## scp

| دستور | کاربرد |
| --- | --- |
| `scp file user@IP:/path/` | آپلود |
| `scp user@IP:/remote/file ./` | دانلود |
| `scp -r dir user@IP:/path/` | پوشه |

## rsync

| دستور | کاربرد |
| --- | --- |
| `rsync -avz ./dist/ user@IP:/var/www/app/` | sync با فشرده‌سازی |
| `rsync -avz --delete ./dist/ user@IP:/var/www/app/` | حذف فایل‌های اضافه در مقصد |

```bash
# deploy ساده
rsync -avz --delete ./build/ ubuntu@server:/var/www/my-app/
ssh ubuntu@server 'sudo systemctl reload nginx'
```
