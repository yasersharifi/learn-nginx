---
title: "روز ۱۹: Custom Access Log برای Production"
description: "روز ۱۹: Custom Access Log برای Production"
---

# روز ۱۹: Custom Access Log برای Production

یک log format خوب بساز.

داخل `http`:

```nginx
log_format production_json escape=json
'{'
  '"time":"$time_iso8601",'
  '"remote_addr":"$remote_addr",'
  '"request_method":"$request_method",'
  '"request_uri":"$request_uri",'
  '"status":$status,'
  '"body_bytes_sent":$body_bytes_sent,'
  '"request_time":$request_time,'
  '"upstream_addr":"$upstream_addr",'
  '"upstream_status":"$upstream_status",'
  '"upstream_response_time":"$upstream_response_time",'
  '"http_referer":"$http_referer",'
  '"http_user_agent":"$http_user_agent",'
  '"request_id":"$request_id"'
'}';
```

استفاده:

```nginx
access_log /var/log/nginx/app.access.log production_json;
```

## چرا JSON log خوب است؟

چون بعداً راحت‌تر می‌توانی آن را وارد این ابزارها کنی:

```text
- Elasticsearch
- OpenSearch
- Loki
- Datadog
- Splunk
- CloudWatch
```

## متریک‌های مهم در log

این فیلدها را در log بگذار:

```text
$request_time
$upstream_response_time
$upstream_status
$upstream_addr
$status
$request_method
$request_uri
$request_id
```

---
