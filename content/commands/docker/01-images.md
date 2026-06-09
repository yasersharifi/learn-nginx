---
title: "Image"
description: "docker images، pull، build، rmi — مدیریت image"
---

# Image

| دستور | کاربرد |
| --- | --- |
| `docker images` | لیست imageها |
| `docker image ls` | همان |
| `docker pull nginx:alpine` | دانلود image |
| `docker build -t my-app:1.0 .` | build از Dockerfile |
| `docker build -t my-app . --no-cache` | build بدون cache |
| `docker tag my-app:1.0 user/my-app:1.0` | tag جدید |
| `docker rmi IMAGE_ID` | حذف image |
| `docker image prune` | حذف imageهای بدون استفاده |
| `docker history IMAGE` | لایه‌های image |
| `docker inspect IMAGE` | جزئیات JSON |

```bash
# build چند stage
docker build -t my-api:latest -f Dockerfile.prod .
```
