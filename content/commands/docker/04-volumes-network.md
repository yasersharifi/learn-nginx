---
title: "Volume و شبکه"
description: "docker volume، network — ذخیره پایدار و ارتباط containerها"
---

# Volume و شبکه

## Volume

| دستور | کاربرد |
| --- | --- |
| `docker volume ls` | لیست volumeها |
| `docker volume create mydata` | ساخت |
| `docker volume inspect mydata` | جزئیات |
| `docker volume rm mydata` | حذف |
| `docker volume prune` | حذف بدون استفاده |

```bash
docker run -v mydata:/var/lib/postgresql/data postgres:16
docker run -v $(pwd)/html:/usr/share/nginx/html:ro nginx
```

## Network

| دستور | کاربرد |
| --- | --- |
| `docker network ls` | لیست شبکه‌ها |
| `docker network create app-net` | شبکه bridge |
| `docker network inspect app-net` | جزئیات |
| `docker network connect app-net CONTAINER` | وصل کردن |
| `docker network disconnect app-net CONTAINER` | قطع |
| `docker network prune` | پاک‌سازی |

## پاک‌سازی کلی

| دستور | کاربرد |
| --- | --- |
| `docker system df` | فضای مصرفی |
| `docker system prune` | پاک‌سازی ایمن |
| `docker system prune -a` | همه imageهای بدون استفاده — **احتیاط** |
