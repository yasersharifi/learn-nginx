---
title: "هفته ۴: HTTP/1.1 و Reverse Proxy Behavior"
description: "هفته ۴: HTTP/1.1 و Reverse Proxy Behavior"
---

# هفته ۴: HTTP/1.1 و Reverse Proxy Behavior

## هدف هفته ۴

در پایان هفته باید بفهمی:

* HTTP request و response چه ساختاری دارند.
* Host header چرا مهم است.
* HTTP/1.1 keep-alive چطور کار می‌کند.
* Nginx چطور request را به upstream می‌فرستد.
* proxy headers دقیقاً چرا لازم‌اند.
* chunked transfer چیست.
* buffering چه ربطی به HTTP دارد.

---

## روز ۱۶: ساختار HTTP Request

یک request ساده:

```http id="xsxj5b"
GET /api/users HTTP/1.1
Host: example.com
User-Agent: curl/8.0
Accept: */*
Connection: keep-alive
```

اجزای اصلی:

| بخش     | مثال                |
| ------- | ------------------- |
| Method  | `GET`               |
| Path    | `/api/users`        |
| Version | `HTTP/1.1`          |
| Header  | `Host: example.com` |
| Body    | برای POST/PUT       |

---

## روز ۱۷: Host Header

Nginx با `server_name` و `Host` تصمیم می‌گیرد کدام server block را انتخاب کند.

```nginx id="taky9e"
server {
    listen 80;
    server_name app.local;
}

server {
    listen 80;
    server_name api.local;
}
```

تست:

```bash id="r6uosq"
curl -H "Host: app.local" http://127.0.0.1/
curl -H "Host: api.local" http://127.0.0.1/
```

## چرا Host مهم است؟

چون چند سایت می‌توانند روی یک IP و port باشند:

```text id="bdljvb"
same IP:80
  ├── app.example.com
  ├── api.example.com
  └── admin.example.com
```

---

## روز ۱۸: Proxy Headers

وقتی Nginx جلوی backend است، backend واقعیت اصلی client را مستقیم نمی‌بیند.

```text id="66dyf1"
Client
  ↓
Nginx
  ↓
Backend
```

از دید backend، client ممکن است Nginx باشد.

پس باید headerها را پاس بدهی:

```nginx id="yt3h8d"
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Request-ID $request_id;
```

معنی:

| Header              | معنی                   |
| ------------------- | ---------------------- |
| `Host`              | دامنه اصلی             |
| `X-Real-IP`         | IP client از دید Nginx |
| `X-Forwarded-For`   | زنجیره IPهای proxy     |
| `X-Forwarded-Proto` | `http` یا `https`      |
| `X-Request-ID`      | شناسه trace request    |

---

## خطر X-Forwarded-For

اگر Nginx مستقیم روی اینترنت است، client می‌تواند خودش header جعلی بفرستد:

```bash id="ifpowk"
curl -H "X-Forwarded-For: 1.2.3.4" http://example.com/
```

برای همین backend نباید کورکورانه به این header اعتماد کند مگر اینکه از trusted proxy آمده باشد.

در معماری درست:

```text id="znb40e"
Internet
  ↓
Trusted Proxy / Load Balancer
  ↓
Nginx
  ↓
Backend
```

باید real IP handling درست داشته باشی.

---

## روز ۱۹: Chunked Transfer

در HTTP/1.1 وقتی طول response از اول معلوم نیست، ممکن است response به شکل chunked ارسال شود.

مثال concept:

```http id="ei33pn"
Transfer-Encoding: chunked
```

کاربرد:

```text id="lvyui2"
- streaming
- responseهای تدریجی
- زمانی که Content-Length از اول معلوم نیست
```

با endpoint stream تست کن:

```js id="7n27dn"
app.get("/stream", (req, res) => {
  res.setHeader("Content-Type", "text/plain");

  let i = 0;

  const timer = setInterval(() => {
    i++;
    res.write(`chunk ${i}\n`);

    if (i === 5) {
      clearInterval(timer);
      res.end();
    }
  }, 1000);
});
```

تست:

```bash id="4buiq5"
curl -v -N http://localhost/stream
```

---

## روز ۲۰: Buffering دوباره، اما عمیق‌تر

در فاز ۲ buffering را دیدی. اینجا باید بفهمی چرا از نظر network مهم است.

با buffering on:

```text id="mtu31q"
Upstream سریع response را به Nginx می‌دهد.
Nginx response را buffer می‌کند.
Client با سرعت خودش دریافت می‌کند.
Upstream زودتر آزاد می‌شود.
```

با buffering off:

```text id="eo2y1f"
Upstream مستقیم‌تر به client وصل می‌شود.
اگر client کند باشد، upstream هم درگیر می‌ماند.
برای streaming خوب است.
برای response معمولی تحت فشار ممکن است بدتر باشد.
```

## تمرین

یک client کند شبیه‌سازی کن:

```bash id="ilclqc"
curl --limit-rate 10k http://localhost/large-file -o /tmp/out
```

بعد رفتار upstream و Nginx را با buffering on/off مقایسه کن.

---

## خروجی هفته ۴

باید بتوانی جواب بدهی:

```text id="d2y5pm"
[ ] HTTP request از چه بخش‌هایی تشکیل شده؟
[ ] Host header چرا مهم است؟
[ ] proxy_set_header دقیقاً چه مشکلی را حل می‌کند؟
[ ] X-Forwarded-For چه ریسکی دارد؟
[ ] chunked transfer چیست؟
[ ] چرا buffering برای client کند مهم است؟
```

---
