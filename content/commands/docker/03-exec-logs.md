---
title: "exec و log"
description: "docker exec، logs، attach — ورود به container و دیدن log"
---

# exec و log

| دستور | کاربرد |
| --- | --- |
| `docker logs CONTAINER` | log |
| `docker logs -f CONTAINER` | log زنده |
| `docker logs --tail 100 CONTAINER` | ۱۰۰ خط آخر |
| `docker logs -t CONTAINER` | با timestamp |
| `docker exec -it CONTAINER sh` | shell داخل container |
| `docker exec -it CONTAINER bash` | اگر bash موجود باشد |
| `docker exec CONTAINER ls /app` | یک دستور |
| `docker attach CONTAINER` | اتصال به stdout |
| `docker top CONTAINER` | پروسس‌های داخل |
| `docker stats` | CPU/RAM همه containerها |
| `docker stats CONTAINER` | یک container |

```bash
# اجرای migration داخل container
docker exec -it my-api npm run migrate

# کپی فایل
docker cp CONTAINER:/app/log.txt ./
docker cp ./file.txt CONTAINER:/app/
```
