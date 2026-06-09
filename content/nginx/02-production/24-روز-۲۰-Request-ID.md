---
title: "روز ۲۰: Request ID"
description: "روز ۲۰: Request ID"
---

# روز ۲۰: Request ID

برای trace کردن request بین Nginx و backend، request id مهم است.

Nginx variable داخلی دارد:

```nginx
$request_id
```

به backend پاس بده:

```nginx
proxy_set_header X-Request-ID $request_id;
```

در snippet proxy headers اضافه کن:

```nginx
proxy_set_header X-Request-ID $request_id;
```

حالا backend هم باید همین request id را log کند.

## نتیجه

وقتی مشکلی پیش آمد، می‌توانی یک request را از Nginx تا backend دنبال کنی:

```text
Nginx access.log:
request_id=abc123

Backend log:
request_id=abc123
```

این یکی از ساده‌ترین و مفیدترین کارهای production observability است.

---
