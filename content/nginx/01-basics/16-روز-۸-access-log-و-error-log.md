---
title: "روز ۸: access log و error log"
description: "روز ۸: access log و error log"
---

# روز ۸: access log و error log

## access log

هر request موفق یا ناموفق معمولاً وارد access log می‌شود.

```bash
sudo tail -f /var/log/nginx/access.log
```

نمونه:

```text
127.0.0.1 - - [08/Jun/2026:12:10:00 +0000] "GET / HTTP/1.1" 200 123 "-" "curl/8.0"
```

معنی:

```text
client IP
time
method
path
protocol
status
response size
referer
user agent
```

## error log

برای خطاهای داخلی، upstream failure، permission issue و غیره:

```bash
sudo tail -f /var/log/nginx/error.log
```

---

## تعریف log format سفارشی

داخل `http` context:

```nginx
log_format main_ext '$remote_addr - $remote_user [$time_local] '
                    '"$request" $status $body_bytes_sent '
                    '"$http_referer" "$http_user_agent" '
                    'rt=$request_time '
                    'uct=$upstream_connect_time '
                    'uht=$upstream_header_time '
                    'urt=$upstream_response_time '
                    'ua="$upstream_addr"';

access_log /var/log/nginx/access.log main_ext;
```

این‌ها خیلی مهم‌اند:

| Variable                  | معنی                              |
| ------------------------- | --------------------------------- |
| `$request_time`           | کل زمان request از دید Nginx      |
| `$upstream_connect_time`  | زمان اتصال به upstream            |
| `$upstream_header_time`   | زمان تا دریافت header از upstream |
| `$upstream_response_time` | زمان دریافت response از upstream  |
| `$upstream_addr`          | آدرس upstream پاسخ‌دهنده          |

برای debug production، این‌ها طلا هستند.

---
