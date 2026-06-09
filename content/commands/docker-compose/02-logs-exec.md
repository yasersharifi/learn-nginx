---
title: "log و exec"
description: "docker compose logs، exec — debug سرویس‌های compose"
---

# log و exec

| دستور | کاربرد |
| --- | --- |
| `docker compose logs` | log همه سرویس‌ها |
| `docker compose logs -f` | log زنده |
| `docker compose logs -f api` | log یک سرویس |
| `docker compose logs --tail=50 api` | ۵۰ خط آخر |
| `docker compose exec api sh` | shell در سرویس |
| `docker compose exec db psql -U postgres` | دستور در سرویس db |
| `docker compose run api npm test` | container یک‌بار مصرف |
| `docker compose cp api:/app/log ./log` | کپی از container |
| `docker compose watch` | rebuild/restart با تغییر فایل (نسخه جدید) |

```bash
# بعد از تغییر env
docker compose up -d --force-recreate api

# فقط rebuild یک سرویس
docker compose build api && docker compose up -d api
```
