---
title: "log و debug"
description: "tail، curl، ss — عیب‌یابی 502، 404، 504 در Nginx"
---

# log و debug

## خواندن log

| دستور | کاربرد |
| --- | --- |
| `sudo tail -f /var/log/nginx/access.log` | access زنده |
| `sudo tail -f /var/log/nginx/error.log` | error زنده |
| `sudo tail -n 200 /var/log/nginx/error.log` | ۲۰۰ خط آخر |
| `sudo grep "502" /var/log/nginx/access.log` | فیلتر status |

## تست

| دستور | کاربرد |
| --- | --- |
| `curl -i http://localhost` | response کامل |
| `curl -I http://localhost` | فقط header |
| `curl -H "Host: app.local" http://127.0.0.1` | virtual host |
| `curl -k https://localhost` | HTTPS self-signed |
| `curl http://127.0.0.1:3000` | تست مستقیم upstream |

## شبکه

| دستور | کاربرد |
| --- | --- |
| `sudo ss -tulpn \| grep nginx` | پورت‌های Nginx |
| `ss -tan sport = :80` | connection به ۸۰ |
| `sudo lsof -i :80` | چه کسی ۸۰ را گرفته |

## خطاهای رایج

| کد | معمولاً یعنی | اولین چک |
| ---: | --- | --- |
| 502 | upstream در دسترس نیست | `curl upstream` + `error.log` |
| 404 | مسیر / root اشتباه | `nginx -T` + `proxy_pass` slash |
| 403 | permission | `ls -la` مسیر فایل |
| 504 | upstream کند | `proxy_read_timeout` + log |

```bash
# benchmark ساده
wrk -t4 -c100 -d30s http://localhost/
hey -n 1000 -c 50 http://localhost/api/health
```
