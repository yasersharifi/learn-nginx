---
title: "هفته ۳: TCP/IP و Connection Lifecycle"
description: "هفته ۳: TCP/IP و Connection Lifecycle"
---

# هفته ۳: TCP/IP و Connection Lifecycle

## هدف هفته ۳

در پایان این هفته باید بتوانی:

- TCP handshake را توضیح بدهی.
- تفاوت TCP و UDP را بفهمی.
- stateهای TCP را تشخیص بدهی.
- backlog، SYN queue و accept queue را بفهمی.
- TIME_WAIT را توضیح بدهی.
- بفهمی keepalive چرا مهم است.
- با `tcpdump` connection را ببینی.

---

## روز ۱۱: TCP Handshake

TCP connection با three-way handshake شروع می‌شود:

```text id="5a6ku4"
Client ← SYN ← Server
Client ← SYN-ACK ← Server
Client ← ACK ← Server
```

بعد connection برقرار می‌شود:

```text id="lrzuhi"
ESTABLISHED
```

برای مشاهده با `tcpdump`:

```bash id="615wm8"
sudo tcpdump -i lo -nn tcp port 80
```

در terminal دیگر:

```bash id="8whsm3"
curl http://localhost/
```

دنبال این‌ها بگرد:

```text id="g6ci6g"
Flags [S]
Flags [S.]
Flags [.]
```

معنی:

| Flag | معنی       |
| ---- | ---------- |
| `S`  | SYN        |
| `S.` | SYN-ACK    |
| `.`  | ACK        |
| `P.` | PUSH + ACK |
| `F.` | FIN + ACK  |

---

## روز ۱۲: TCP States

برای دیدن stateها:

```bash id="1olrgt"
ss -tan
```

stateهای مهم:

```text id="0riivf"
LISTEN
SYN-SENT
SYN-RECV
ESTAB
FIN-WAIT-1
FIN-WAIT-2
CLOSE-WAIT
LAST-ACK
TIME-WAIT
CLOSED
```

## TIME_WAIT چیست؟

بعد از بسته شدن connection، یک طرف مدتی در `TIME_WAIT` می‌ماند تا packetهای دیررس باعث خراب شدن connectionهای بعدی نشوند.

دیدن تعداد TIME_WAIT:

```bash id="ys7u3f"
ss -tan state time-wait | wc -l
```

## نکته

دیدن TIME_WAIT همیشه مشکل نیست. مشکل وقتی است که تعدادش خیلی زیاد شود و port/resource pressure ایجاد کند.

---

## روز ۱۳: Listen Backlog

در Nginx:

```nginx id="kg7zf4"
listen 80 backlog=1024;
```

Backlog به queue connectionهای در انتظار accept مربوط است.

اما فقط Nginx مهم نیست. kernel هم limit دارد.

دیدن:

```bash id="6tmjh4"
sysctl net.core.somaxconn
```

اگر Nginx backlog بزرگ بگذاری ولی kernel limit کوچک باشد، kernel سقف خودش را اعمال می‌کند.

## SYN Queue

وقتی SYN می‌آید ولی handshake کامل نشده:

```text id="ch38v1"
SYN queue
```

## Accept Queue

وقتی handshake کامل شده ولی application هنوز accept نکرده:

```text id="t4fovi"
accept queue
```

## چرا مهم است؟

وقتی traffic burst داری، queueها پر می‌شوند و connection drop یا delay رخ می‌دهد.

---

## روز ۱۴: TCP Keepalive vs HTTP Keep-Alive

این دو را قاطی نکن.

### HTTP keep-alive

چند HTTP request روی یک TCP connection:

```text id="17ffps"
TCP connection
  ├── HTTP request 1
  ├── HTTP response 1
  ├── HTTP request 2
  └── HTTP response 2
```

### TCP keepalive

مکانیزم kernel برای تشخیص connection مرده در سطح TCP.

در Nginx:

```nginx id="2trn3k"
keepalive_timeout 65;
```

این مربوط به HTTP keep-alive سمت client است.

برای upstream keepalive:

```nginx id="9mc5v9"
upstream app_backend {
    server 127.0.0.1:3000;
    keepalive 32;
}
```

در location:

```nginx id="8392vs"
proxy_http_version 1.1;
proxy_set_header Connection "";
```

---

## روز ۱۵: Connection Reuse

بدون keepalive:

```text id="1qkrhq"
request 1 ← TCP handshake ← response ← close
request 2 ← TCP handshake ← response ← close
request 3 ← TCP handshake ← response ← close
```

با keepalive:

```text id="bl77zd"
TCP handshake
request 1 ← response
request 2 ← response
request 3 ← response
close later
```

مزیت:

```text id="rpxpdx"
- latency کمتر
- CPU کمتر
- handshake کمتر
- TLS cost کمتر
```

عیب:

```text id="u51iqs"
- connectionها بیشتر باز می‌مانند
- fd مصرف می‌شود
- باید timeout درست تنظیم شود
```

---

## تمرین هفته ۳

با HTTP keepalive:

```bash id="s2bj2b"
curl -v http://localhost/
```

دنبال headerها و connection reuse بگرد.

با چند request:

```bash id="t0l1x6"
curl -v http://localhost/ http://localhost/
```

همزمان:

```bash id="bexqn1"
ss -tan | grep ':80'
```

---

## خروجی هفته ۳

باید بتوانی جواب بدهی:

```text id="vbnxfj"
[ ] TCP three-way handshake چیست؟
[ ] SYN queue چیست؟
[ ] accept queue چیست؟
[ ] backlog چه اثری دارد؟
[ ] TIME_WAIT چیست؟
[ ] HTTP keep-alive و TCP keepalive چه فرقی دارند؟
[ ] connection reuse چه مزایا و معایبی دارد؟
```

---
