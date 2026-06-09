---
title: "هفته ۹: Latency و Percentileها"
description: "هفته ۹: Latency و Percentileها"
---

# هفته ۹: Latency و Percentileها

Average کافی نیست.

فرض کن:

```text id="idsb5o"
۹۹ request در 20ms جواب می‌دهند
۱ request در 3000ms جواب می‌دهد
```

میانگین ممکن است قابل قبول باشد، ولی کاربرانی که request کند گرفته‌اند تجربه بدی دارند.

متریک‌های مهم:

| Metric | معنی                                 |
| ------ | ------------------------------------ |
| p50    | نصف requestها سریع‌تر از این مقدارند |
| p95    | ۹۵٪ requestها سریع‌تر از این مقدارند |
| p99    | ۹۹٪ requestها سریع‌تر از این مقدارند |
| max    | بدترین request                       |

## چرا p99 مهم است؟

چون production با average اداره نمی‌شود. tail latency روی تجربه کاربر و reliability اثر جدی دارد.

---

## wrk با latency

```bash id="unxmvo"
wrk -t4 -c100 -d30s --latency http://localhost/
```

به این بخش دقت کن:

```text id="8we852"
Latency Distribution
  50%
  75%
  90%
  99%
```

---
