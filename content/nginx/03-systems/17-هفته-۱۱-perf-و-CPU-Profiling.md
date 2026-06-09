---
title: "هفته ۱۱: perf و CPU Profiling"
description: "هفته ۱۱: perf و CPU Profiling"
---

# هفته ۱۱: perf و CPU Profiling

اگر CPU bottleneck داری، باید بتوانی ببینی CPU کجا مصرف می‌شود.

نصب:

```bash id="5eq6sl"
sudo apt install linux-tools-common linux-tools-generic
```

ضبط profile:

```bash id="ke6nu5"
sudo perf top -p <NGINX_WORKER_PID>
```

یا:

```bash id="rvl8pb"
sudo perf record -p <NGINX_WORKER_PID> -g -- sleep 30
sudo perf report
```

## چه زمانی perf مفید است؟

```text id="rm4j4g"
- TLS CPU بالا
- gzip CPU بالا
- static serving سنگین
- request rate خیلی بالا
- regex locationهای سنگین
```

---
