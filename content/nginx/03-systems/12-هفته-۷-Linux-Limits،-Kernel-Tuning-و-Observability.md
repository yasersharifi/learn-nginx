---
title: "هفته ۷: Linux Limits، Kernel Tuning و Observability"
description: "هفته ۷: Linux Limits، Kernel Tuning و Observability"
---

# هفته ۷: Linux Limits، Kernel Tuning و Observability

## هدف هفته ۷

در این هفته باید بفهمی کدام limitهای Linux روی Nginx اثر دارند و چطور آن‌ها را مشاهده کنی.

---

## روز ۳۳: limits مهم

موارد مهم:

```text id="ekyxwu"
- max open files
- worker_connections
- somaxconn
- ephemeral ports
- TIME_WAIT
- TCP backlog
- memory
- CPU
- network bandwidth
```

دیدن limits:

```bash id="pbot7p"
ulimit -a
```

برای process:

```bash id="ou8amf"
cat /proc/<PID>/limits
```

---

## روز ۳۴: sysctlهای مهم

دیدن همه TCP settings:

```bash id="evg0a5"
sysctl -a | grep net.ipv4.tcp
```

موارد قابل بررسی:

```bash id="4rbywd"
sysctl net.core.somaxconn
sysctl net.ipv4.ip_local_port_range
sysctl net.ipv4.tcp_fin_timeout
sysctl net.ipv4.tcp_tw_reuse
```

## هشدار

Kernel tuning را کورکورانه انجام نده. اول bottleneck را مشاهده کن، بعد تغییر بده.

قانون:

```text id="7cyiit"
Measure first, tune second.
```

---

## روز ۳۵: CPU و Memory

برای مشاهده CPU:

```bash id="dm5d5y"
top
htop
pidstat -p <PID> 1
```

برای memory:

```bash id="lpcqwh"
free -h
ps aux --sort=-%mem | head
```

برای Nginx workerها:

```bash id="9ea1sl"
ps -o pid,ppid,cmd,%cpu,%mem,rss,vsz -C nginx
```

---

## روز ۳۶: Network Observability

ابزارها:

```text id="d2ybsn"
ss
ip
iftop
nload
sar
tcpdump
```

دیدن interfaceها:

```bash id="6he888"
ip addr
```

دیدن routeها:

```bash id="im8s3n"
ip route
```

دیدن traffic:

```bash id="a0wzgv"
sudo iftop
```

یا:

```bash id="2r163m"
sar -n DEV 1
```

---

## روز ۳۷: Nginx Access Log به‌عنوان ابزار observability

Log format خوب:

```nginx id="bljy4w"
log_format perf_json escape=json
'{'
  '"time":"$time_iso8601",'
  '"remote_addr":"$remote_addr",'
  '"method":"$request_method",'
  '"uri":"$request_uri",'
  '"status":$status,'
  '"request_time":$request_time,'
  '"upstream_time":"$upstream_response_time",'
  '"upstream_addr":"$upstream_addr",'
  '"upstream_status":"$upstream_status",'
  '"bytes":$body_bytes_sent,'
  '"request_id":"$request_id"'
'}';
```

با این log می‌توانی بفهمی:

```text id="kwp00q"
- کدام endpoint کند است
- کدام upstream کند است
- p95/p99 تقریبی چقدر است
- خطاها از کدام upstream می‌آیند
- latency از Nginx است یا backend
```

---

## خروجی هفته ۷

باید بتوانی جواب بدهی:

```text id="l5wl68"
[ ] ulimit و worker_rlimit_nofile چه رابطه‌ای دارند؟
[ ] somaxconn چیست؟
[ ] ip_local_port_range چه زمانی مهم می‌شود؟
[ ] TIME_WAIT زیاد همیشه بد است؟
[ ] چرا kernel tuning بدون measurement خطرناک است؟
[ ] از روی access log چطور upstream کند را پیدا می‌کنی؟
```

---
