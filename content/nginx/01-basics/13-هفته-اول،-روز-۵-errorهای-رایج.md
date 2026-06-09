---
title: "هفته اول، روز ۵: errorهای رایج"
description: "هفته اول، روز ۵: errorهای رایج"
---

# هفته اول، روز ۵: errorهای رایج

## 502 Bad Gateway

معمولاً یعنی Nginx نتوانسته به upstream وصل شود.

دلایل رایج:

```text
- app خاموش است
- port اشتباه است
- app فقط روی IPv6 گوش می‌دهد
- firewall بسته است
- Docker networking اشتباه است
- upstream crash کرده
```

Debug:

```bash
sudo tail -f /var/log/nginx/error.log
```

تست upstream مستقیم:

```bash
curl http://127.0.0.1:3000
```

اگر این کار نمی‌کند، مشکل از Nginx نیست؛ مشکل از app است.

---

## 404 Not Found

دلایل رایج:

```text
- root اشتباه است
- try_files اشتباه است
- location match اشتباه است
- proxy_pass با slash اشتباه نوشته شده
- app route ندارد
```

Debug:

```bash
curl -i http://localhost/some-path
```

و بررسی access log:

```bash
sudo tail -f /var/log/nginx/access.log
```

---

## 403 Forbidden

دلایل رایج:

```text
- permission فایل/دایرکتوری اشتباه است
- index file وجود ندارد
- autoindex خاموش است
- user اجرای Nginx به فایل دسترسی ندارد
```

بررسی user:

```bash
ps aux | grep nginx
```

بررسی permission:

```bash
ls -la /var/www/nginx-lab
```

---

## 504 Gateway Timeout

یعنی upstream دیر جواب داده.

دلایل:

```text
- backend کند است
- query دیتابیس طولانی است
- proxy timeout کوتاه است
- upstream گیر کرده
```

configهای مرتبط:

```nginx
proxy_connect_timeout 5s;
proxy_send_timeout 30s;
proxy_read_timeout 30s;
```

فعلاً فقط معنی پایه را بدان:

| Directive               | معنی                                       |
| ----------------------- | ------------------------------------------ |
| `proxy_connect_timeout` | زمان مجاز برای وصل شدن به upstream         |
| `proxy_send_timeout`    | زمان مجاز برای ارسال request به upstream   |
| `proxy_read_timeout`    | زمان مجاز برای دریافت response از upstream |

---
