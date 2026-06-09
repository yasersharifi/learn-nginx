---
title: "مجوز و کاربر"
description: "chmod، chown، sudo — دسترسی فایل و اجرای admin"
---

# مجوز و کاربر

| دستور | کاربرد |
| --- | --- |
| `ls -la` | دیدن مجوزها (`rwx`) |
| `chmod +x script.sh` | قابل اجرا |
| `chmod 644 file` | فایل عادی |
| `chmod 755 script` | اسکریپت / پوشه |
| `chmod 600 key.pem` | کلید خصوصی |
| `chown user:group file` | تغییر مالک |
| `chown -R user:user /var/www/app` | کل پوشه |
| `sudo cmd` | اجرا با دسترسی root |
| `sudo -i` | shell با root |
| `whoami` | کاربر فعلی |
| `id` | uid، gid، گروه‌ها |

معنی رایج `chmod`:

| عدد | معنی |
| ---: | --- |
| 644 | owner می‌نویسد؛ بقیه فقط می‌خوانند |
| 755 | owner همه‌چیز؛ بقیه اجرا و خواندن |
| 600 | فقط owner |
