---
title: "نکته مهم درباره `proxy_pass`"
description: "نکته مهم درباره `proxy_pass`"
---

# نکته مهم درباره `proxy_pass`

این دو config فرق دارند:

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:3000;
}
```

و:

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:3000/;
}
```

فرق subtle ولی مهم است.

## بدون slash آخر

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:3000;
}
```

Request:

```text
/api/users
```

به upstream می‌رود:

```text
/api/users
```

## با slash آخر

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:3000/;
}
```

Request:

```text
/api/users
```

به upstream می‌رود:

```text
/users
```

یعنی prefix `/api/` حذف می‌شود.

این یکی از جاهایی است که خیلی developerها چند ساعت debug می‌کنند.

---
