---
title: "شبکه"
description: "curl، ss، lsof، ping، dig — تست اتصال و پورت"
---

# شبکه

| دستور | کاربرد |
| --- | --- |
| `ip addr` | IP و interfaceها |
| `ip route` | جدول مسیریابی |
| `ping host` | تست reachability |
| `curl http://localhost:3000` | درخواست HTTP |
| `curl -I https://example.com` | فقط header |
| `curl -v http://localhost/api` | verbose |
| `curl -k https://localhost` | قبول self-signed |
| `ss -tulpn` | پورت‌های listening |
| `ss -tan` | همه TCP connectionها |
| `sudo lsof -i :3000` | چه چیزی روی پورت ۳۰۰۰ |
| `sudo lsof -i :80` | چه چیزی روی پورت ۸۰ |
| `nslookup example.com` | DNS |
| `dig example.com` | DNS با جزئیات |
| `dig example.com TXT` | رکورد TXT (SPF و …) |
| `wget -O file URL` | دانلود فایل |

```bash
# POST JSON
curl -X POST http://localhost:3000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"a@b.com","password":"x"}'
```
