---
title: "هفته ۶: TLS، HTTP/2 و HTTP/3"
description: "هفته ۶: TLS، HTTP/2 و HTTP/3"
---

# هفته ۶: TLS، HTTP/2 و HTTP/3

## هدف هفته ۶

در پایان این هفته باید بفهمی:

* TLS handshake چیست.
* چرا TLS cost دارد.
* certificate chain چیست.
* HTTP/2 چه تفاوتی با HTTP/1.1 دارد.
* multiplexing یعنی چه.
* HTTP/3 و QUIC concept چیست.
* چرا HTTP/3 روی UDP است.
* این موارد چه اثری روی Nginx دارند.

---

## روز ۲۸: TLS Handshake

وقتی browser با HTTPS وصل می‌شود:

```text id="c2xfo9"
ClientHello
ServerHello
Certificate
Key exchange
Finished
Encrypted HTTP
```

TLS قبل از HTTP قرار می‌گیرد:

```text id="cayswj"
HTTP
  ↓
TLS
  ↓
TCP
```

برای مشاهده:

```bash id="py5yu5"
openssl s_client -connect example.com:443 -servername example.com
```

برای local:

```bash id="p70odr"
openssl s_client -connect localhost:443 -servername localhost
```

---

## روز ۲۹: TLS Cost

TLS هزینه دارد:

```text id="vnvvc7"
- CPU برای encryption/decryption
- handshake latency
- certificate validation
- session management
```

چرا keepalive مهم‌تر می‌شود؟

چون اگر برای هر request TLS handshake جدید داشته باشی، هزینه بالا می‌رود.

با keepalive:

```text id="efz9nr"
TLS handshake once
request 1
request 2
request 3
```

---

## روز ۳۰: HTTP/2

HTTP/1.1:

```text id="c5eu2r"
یک connection
requestها معمولاً sequential یا محدود
head-of-line در سطح connection
```

HTTP/2:

```text id="xvl9xm"
یک connection
چند stream همزمان
multiplexing
header compression
```

مزیت:

```text id="w1qd54"
- مناسب assetهای متعدد
- latency کمتر در برخی شرایط
- connection کمتر
```

اما:

```text id="73wqlr"
اگر TCP packet loss رخ دهد، همه streamهای آن TCP connection ممکن است اثر بگیرند.
```

فعال‌سازی:

```nginx id="j4h57v"
listen 443 ssl http2;
```

یا در نسخه‌های جدید:

```nginx id="i408vi"
listen 443 ssl;
http2 on;
```

تست:

```bash id="21yblp"
curl -I --http2 https://example.com
```

---

## روز ۳۱: HTTP/3 و QUIC

HTTP/3 روی QUIC است و QUIC روی UDP.

```text id="sv5nff"
HTTP/3
  ↓
QUIC
  ↓
UDP
```

مزیت‌های concept:

```text id="f3ivtn"
- کاهش head-of-line blocking در سطح TCP
- connection migration
- handshake سریع‌تر در برخی شرایط
- مناسب networkهای ناپایدار موبایل
```

اما:

```text id="i7nldd"
- پیچیدگی بیشتر
- debugging سخت‌تر
- نیاز به پشتیبانی client/server/CDN
- UDP ممکن است در برخی شبکه‌ها محدود باشد
```

برای فاز ۳ لازم نیست HTTP/3 را production-grade کانفیگ کنی. فعلاً مفهومش را بفهم.

---

## روز ۳۲: ALPN

ALPN یعنی client و server هنگام TLS handshake توافق می‌کنند از چه پروتکلی استفاده کنند:

```text id="qwpbm2"
h2
http/1.1
```

با openssl:

```bash id="86uzvb"
openssl s_client -alpn h2 -connect example.com:443 -servername example.com
```

دنبال ALPN negotiated بگرد.

---

## خروجی هفته ۶

باید بتوانی جواب بدهی:

```text id="05mw7f"
[ ] TLS handshake چیست؟
[ ] چرا TLS latency و CPU cost دارد؟
[ ] چرا keepalive برای HTTPS مهم است؟
[ ] HTTP/2 multiplexing چیست؟
[ ] HTTP/2 چه مشکلی را حل می‌کند و چه مشکلی را نه؟
[ ] HTTP/3 چرا روی UDP است؟
[ ] ALPN چیست؟
```

---
