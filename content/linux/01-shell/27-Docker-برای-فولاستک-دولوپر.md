---
title: "27. Docker برای فول‌استک دولوپر"
description: "27. Docker برای فول‌استک دولوپر"
---

# 27. Docker برای فول‌استک دولوپر

### دیدن containerها

```bash
docker ps
```

همه containerها:

```bash
docker ps -a
```

### دیدن imageها

```bash
docker images
```

### اجرای container

```bash
docker run -p 3000:3000 my-app
```

### توقف container

```bash
docker stop CONTAINER_ID
```

### حذف container

```bash
docker rm CONTAINER_ID
```

### حذف image

```bash
docker rmi IMAGE_ID
```

### دیدن لاگ container

```bash
docker logs CONTAINER_ID
```

لاگ زنده:

```bash
docker logs -f CONTAINER_ID
```

### ورود به shell داخل container

```bash
docker exec -it CONTAINER_ID sh
```

یا اگر bash موجود باشد:

```bash
docker exec -it CONTAINER_ID bash
```

---
