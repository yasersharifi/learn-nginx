---
title: "روز ۲: Timeoutهای مهم"
description: "روز ۲: Timeoutهای مهم"
---

# روز ۲: Timeoutهای مهم

یکی از مهم‌ترین بخش‌های production Nginx، timeoutها هستند.

Config پایه:

```nginx
proxy_connect_timeout 5s;
proxy_send_timeout 30s;
proxy_read_timeout 30s;
send_timeout 30s;
```

بهتر است این‌ها را در snippet جدا بگذاری.

فایل:

```text
/etc/nginx/snippets/proxy-timeouts.conf
```

محتوا:

```nginx
proxy_connect_timeout 5s;
proxy_send_timeout 30s;
proxy_read_timeout 30s;
send_timeout 30s;
```

استفاده:

```nginx
location / {
    proxy_pass http://app_backend;
    include snippets/proxy-headers.conf;
    include snippets/proxy-timeouts.conf;
}
```

## معنی timeoutها

| Directive               | معنی                                                |
| ----------------------- | --------------------------------------------------- |
| `proxy_connect_timeout` | حداکثر زمان برای اتصال Nginx به upstream            |
| `proxy_send_timeout`    | حداکثر زمان برای ارسال request از Nginx به upstream |
| `proxy_read_timeout`    | حداکثر زمان انتظار برای خواندن response از upstream |
| `send_timeout`          | حداکثر زمان ارسال response از Nginx به client       |

## نکته مهم

`proxy_read_timeout` کل زمان اجرای endpoint نیست. این timeout معمولاً بین دو read operation محاسبه می‌شود. یعنی اگر upstream هر چند ثانیه داده‌ای بفرستد، ممکن است connection زنده بماند.

## مقادیر پیشنهادی اولیه

برای API معمولی:

```nginx
proxy_connect_timeout 5s;
proxy_send_timeout 30s;
proxy_read_timeout 30s;
send_timeout 30s;
```

برای endpointهای طولانی مثل export یا report:

```nginx
proxy_connect_timeout 5s;
proxy_send_timeout 120s;
proxy_read_timeout 120s;
send_timeout 120s;
```

برای WebSocket:

```nginx
proxy_read_timeout 3600s;
proxy_send_timeout 3600s;
```

## تمرین

یک endpoint کند در Node.js بساز:

```js
app.get("/slow", async (req, res) => {
  await new Promise((resolve) => setTimeout(resolve, 40000));
  res.json({ ok: true });
});
```

بعد با `proxy_read_timeout 10s` تست کن:

```bash
curl -i http://localhost/slow
```

باید timeout ببینی.

بعد timeout را بیشتر کن و دوباره تست کن.

---
