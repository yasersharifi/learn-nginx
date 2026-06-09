---
title: "Container"
description: "docker run، ps، stop، rm — اجرا و مدیریت container"
---

# Container

| دستور | کاربرد |
| --- | --- |
| `docker ps` | containerهای در حال اجرا |
| `docker ps -a` | همه containerها |
| `docker run -p 3000:3000 my-app` | اجرا با map پورت |
| `docker run -d --name api my-app` | detached + نام |
| `docker run -d -p 80:80 --restart unless-stopped nginx` | با restart خودکار |
| `docker run -it ubuntu bash` | interactive |
| `docker run --rm -it node:20 sh` | حذف بعد از exit |
| `docker stop CONTAINER` | توقف |
| `docker start CONTAINER` | شروع مجدد |
| `docker restart CONTAINER` | ری‌استارت |
| `docker rm CONTAINER` | حذف |
| `docker rm -f CONTAINER` | حذف اجباری |
| `docker container prune` | حذف متوقف‌شده‌ها |
| `docker inspect CONTAINER` | جزئیات |

```bash
# env و volume
docker run -d \
  -p 3000:3000 \
  -e NODE_ENV=production \
  -v $(pwd)/data:/app/data \
  --name my-api \
  my-api:latest
```
