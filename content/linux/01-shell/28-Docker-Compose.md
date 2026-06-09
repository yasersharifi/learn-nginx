---
title: "28. Docker Compose"
description: "28. Docker Compose"
---

# 28. Docker Compose

### بالا آوردن سرویس‌ها

```bash
docker compose up
```

در background:

```bash
docker compose up -d
```

### توقف سرویس‌ها

```bash
docker compose down
```

### build مجدد

```bash
docker compose up -d --build
```

### دیدن لاگ‌ها

```bash
docker compose logs
```

لاگ یک سرویس:

```bash
docker compose logs -f api
```

### اجرای دستور داخل سرویس

```bash
docker compose exec api sh
```

مثال برای دیتابیس:

```bash
docker compose exec postgres psql -U postgres
```

---
