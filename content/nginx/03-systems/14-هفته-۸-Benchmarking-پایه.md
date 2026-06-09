---
title: "هفته ۸: Benchmarking پایه"
description: "هفته ۸: Benchmarking پایه"
---

# هفته ۸: Benchmarking پایه

## ابزارهای پیشنهادی

```text id="rg7lrl"
wrk
hey
ab
k6
vegeta
```

برای شروع `wrk` کافی است.

نصب روی Ubuntu:

```bash id="c8d8lf"
sudo apt install wrk
```

تست ساده:

```bash id="gswqbf"
wrk -t4 -c100 -d30s http://localhost/
```

معنی:

| گزینه   | معنی                 |
| ------- | -------------------- |
| `-t4`   | چهار thread برای wrk |
| `-c100` | صد connection همزمان |
| `-d30s` | مدت تست ۳۰ ثانیه     |

خروجی‌هایی که مهم‌اند:

```text id="8kulib"
Requests/sec
Latency avg
Latency max
Transfer/sec
Socket errors
Non-2xx/3xx responses
```

---

## سناریوهای benchmark

### ۱. Static file

```bash id="powdd3"
wrk -t4 -c100 -d30s http://localhost/static/app.js
```

### ۲. Reverse proxy به app سریع

```bash id="u0cmre"
wrk -t4 -c100 -d30s http://localhost/api/fast
```

### ۳. Reverse proxy به app کند

```bash id="x5jido"
wrk -t4 -c100 -d30s http://localhost/api/slow
```

### ۴. HTTPS

```bash id="zno5cf"
wrk -t4 -c100 -d30s https://localhost/
```

### ۵. Keepalive off/on

با keepalive تنظیمات را مقایسه کن.

---

## قانون benchmark

یک benchmark بد، از benchmark نگرفتن بدتر است.

باید ثابت نگه داری:

```text id="0x6sua"
- hardware
- config
- app version
- endpoint
- concurrency
- duration
- network path
```

---
