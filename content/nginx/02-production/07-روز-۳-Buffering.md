---
title: "روز ۳: Buffering"
description: "روز ۳: Buffering"
---

# روز ۳: Buffering

Buffering یکی از چیزهایی است که اگر نفهمی، production debug برایت سخت می‌شود.

Nginx می‌تواند response upstream را قبل از ارسال کامل به client در buffer نگه دارد.

Config پیش‌فرض معمولاً buffering را فعال دارد:

```nginx
proxy_buffering on;
```

## حالت buffering on

```text
Client
  ↓
Nginx response را از upstream می‌گیرد
در buffer نگه می‌دارد
بعد به client ارسال می‌کند
```

مزایا:

* upstream سریع‌تر آزاد می‌شود
* client کند کمتر روی upstream اثر می‌گذارد
* برای responseهای معمولی بهتر است

معایب:

* برای streaming مناسب نیست
* ممکن است memory/disk بیشتری مصرف شود
* ممکن است latency اولیه بیشتر شود

## حالت buffering off

```nginx
proxy_buffering off;
```

مزایا:

* مناسب streaming
* مناسب Server-Sent Events
* مناسب responseهایی که باید chunk-by-chunk برسند

معایب:

* client کند می‌تواند upstream را درگیر نگه دارد
* تحت فشار ممکن است upstream زودتر اشباع شود

## Config پیشنهادی

برای API معمولی:

```nginx
proxy_buffering on;
```

برای streaming یا SSE:

```nginx
location /events/ {
    proxy_pass http://app_backend;
    proxy_buffering off;
    include snippets/proxy-headers.conf;
}
```

برای WebSocket buffering موضوع متفاوتی است و با upgrade connection سروکار داری.

## تمرین

یک endpoint streaming بساز:

```js
app.get("/stream", (req, res) => {
  res.setHeader("Content-Type", "text/plain");

  let count = 0;

  const interval = setInterval(() => {
    count++;
    res.write(`chunk ${count}\n`);

    if (count === 10) {
      clearInterval(interval);
      res.end();
    }
  }, 1000);
});
```

با buffering روشن و خاموش تست کن:

```bash
curl -N http://localhost/stream
```

ببین chunkها لحظه‌ای می‌آیند یا یک‌جا.

---
