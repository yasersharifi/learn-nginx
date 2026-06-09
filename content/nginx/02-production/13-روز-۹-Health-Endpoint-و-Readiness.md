---
title: "روز ۹: Health Endpoint و Readiness"
description: "روز ۹: Health Endpoint و Readiness"
---

# روز ۹: Health Endpoint و Readiness

حتی اگر Nginx open source active health check پیشرفته نداشته باشد، خودت باید در app endpointهای سلامت داشته باشی.

حداقل:

```text
GET /health
GET /ready
```

فرق:

| Endpoint  | معنی                         |
| --------- | ---------------------------- |
| `/health` | process زنده است             |
| `/ready`  | app آماده دریافت traffic است |

مثلاً `/ready` باید شاید database، redis یا dependency مهم را چک کند.

## Config Nginx برای health خود Nginx

```nginx
location = /nginx-health {
    access_log off;
    return 200 "ok\n";
}
```

## تمرین

برای app endpointهای زیر بساز:

```text
/health
/ready
```

بعد در Nginx route کن:

```nginx
location = /health {
    proxy_pass http://app_backend/health;
    include snippets/proxy-headers.conf;
}

location = /nginx-health {
    access_log off;
    return 200 "ok\n";
}
```

---
