---
title: "curl و HTTP"
description: "درخواست GET، POST، header و تست API"
---

# curl و HTTP

| دستور | کاربرد |
| --- | --- |
| `curl URL` | GET ساده |
| `curl -I URL` | فقط header |
| `curl -i URL` | header + body |
| `curl -v URL` | verbose (debug) |
| `curl -L URL` | follow redirect |
| `curl -o out.bin URL` | ذخیره در فایل |
| `curl -O URL` | ذخیره با نام remote |
| `curl --limit-rate 10k URL` | شبیه‌سازی client کند |
| `curl -N URL` | بدون buffer (stream) |
| `curl --http2 -I https://site` | تست HTTP/2 |

```bash
# POST JSON
curl -X POST http://localhost:4000/api/users \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TOKEN" \
  -d '{"name":"ali"}'

# فرم
curl -X POST http://localhost/upload \
  -F "file=@/path/to/file.bin"

# فقط status code
curl -s -o /dev/null -w "%{http_code}\n" http://localhost/health
```
