<div dir="rtl" align="right">

# فاز ۲: Production Operations در Nginx

در فاز ۱ هدف این بود که Nginx را عملی یاد بگیری: نصب، static file serving، reverse proxy، upstream، basic load balancing، HTTPS ساده، WebSocket و debug خطاهای رایج.

در فاز ۲ وارد سطح جدی‌تری می‌شویم: **استفاده از Nginx در محیط production**.

اینجا دیگر فقط مهم نیست که config کار کند. مهم این است که config:

* پایدار باشد
* قابل debug باشد
* قابل مانیتور باشد
* تحت فشار رفتار قابل پیش‌بینی داشته باشد
* failure را کنترل کند
* امنیت پایه داشته باشد
* برای تیم قابل نگهداری باشد

---

<details>
<summary><strong>📑 فهرست مطالب</strong> — <em>کلیک برای باز / بسته کردن</em></summary>

| # | بخش |
| ---: | --- |
| 1 | [هدف فاز ۲](#هدف-فاز-۲) |
| 2 | [پیش‌نیازهای فاز ۲](#پیشنیازهای-فاز-۲) |
| 3 | [تصویر ذهنی فاز ۲](#تصویر-ذهنی-فاز-۲) |
| 4 | [هفته ۱: Production Reverse Proxy](#هفته-۱-production-reverse-proxy) |
| 5 | [روز ۲: Timeoutهای مهم](#روز-۲-timeoutهای-مهم) |
| 6 | [روز ۳: Buffering](#روز-۳-buffering) |
| 7 | [روز ۴: Request Body و Upload Limits](#روز-۴-request-body-و-upload-limits) |
| 8 | [روز ۵: Proxy Error Handling](#روز-۵-proxy-error-handling) |
| 9 | [هفته ۲: Load Balancing و Failure Behavior](#هفته-۲-load-balancing-و-failure-behavior) |
| 10 | [روز ۷: Retry Behavior](#روز-۷-retry-behavior) |
| 11 | [روز ۸: Sticky Session Concept](#روز-۸-sticky-session-concept) |
| 12 | [روز ۹: Health Endpoint و Readiness](#روز-۹-health-endpoint-و-readiness) |
| 13 | [هفته ۳: Caching و Compression](#هفته-۳-caching-و-compression) |
| 14 | [روز ۱۱: Proxy Cache](#روز-۱۱-proxy-cache) |
| 15 | [روز ۱۲: Cache Bypass](#روز-۱۲-cache-bypass) |
| 16 | [روز ۱۳: Compression](#روز-۱۳-compression) |
| 17 | [روز ۱۴: Brotli Concept](#روز-۱۴-brotli-concept) |
| 18 | [هفته ۴: Rate Limiting، Security Headers و Observability](#هفته-۴-rate-limiting،-security-headers-و-observability) |
| 19 | [روز ۱۶: Connection Limiting](#روز-۱۶-connection-limiting) |
| 20 | [روز ۱۷: Security Headers پایه](#روز-۱۷-security-headers-پایه) |
| 21 | [روز ۱۸: Real IP Handling](#روز-۱۸-real-ip-handling) |
| 22 | [روز ۱۹: Custom Access Log برای Production](#روز-۱۹-custom-access-log-برای-production) |
| 23 | [روز ۲۰: Request ID](#روز-۲۰-request-id) |
| 24 | [هفته ۵: HTTPS Production و Deployment Hygiene](#هفته-۵-https-production-و-deployment-hygiene) |
| 25 | [روز ۲۲: SSL Parameters](#روز-۲۲-ssl-parameters) |
| 26 | [روز ۲۳: HTTP/2](#روز-۲۳-http2) |
| 27 | [روز ۲۴: Graceful Reload و Config Safety](#روز-۲۴-graceful-reload-و-config-safety) |
| 28 | [روز ۲۵: Backup و Rollback](#روز-۲۵-backup-و-rollback) |
| 29 | [هفته ۶: Final Production Lab](#هفته-۶-final-production-lab) |
| 30 | [Config نهایی نمونه](#config-نهایی-نمونه) |
| 31 | [تست‌های نهایی فاز ۲](#تستهای-نهایی-فاز-۲) |
| 32 | [Checklist فاز ۲](#checklist-فاز-۲) |
| 33 | [سؤال‌هایی که باید بتوانی جواب بدهی](#سؤالهایی-که-باید-بتوانی-جواب-بدهی) |
| 34 | [برنامه روزانه پیشنهادی فاز ۲](#برنامه-روزانه-پیشنهادی-فاز-۲) |
| 35 | [گزارش نهایی فاز ۲](#گزارش-نهایی-فاز-۲) |
| 36 | [Nginx Phase 2 Production Report](#nginx-phase-2-production-report) |
| 37 | [معیار موفقیت فاز ۲](#معیار-موفقیت-فاز-۲) |
| 38 | [توصیه جدی](#توصیه-جدی) |

[↑ بالا](#فاز-۲-production-operations-در-nginx)

</details>

---

# هدف فاز ۲

<details>
<summary>هدف فاز ۲</summary>

بعد از فاز ۲ باید بتوانی:

* یک Nginx config production-grade برای اپلیکیشن واقعی بنویسی.
* timeoutها، buffering، caching و headerها را آگاهانه تنظیم کنی.
* رفتار Nginx را هنگام کند شدن یا fail شدن upstream بفهمی.
* logهای قابل تحلیل بسازی.
* basic observability برای Nginx داشته باشی.
* rate limiting و connection limiting پیاده کنی.
* رفتار 502، 503، 504 و retryها را کنترل کنی.
* config را modular و maintainable نگه داری.
* برای deploy واقعی آماده‌تر باشی.

مدت پیشنهادی: **۴ تا ۶ هفته**

اگر روزی ۱ تا ۲ ساعت وقت بگذاری، این فاز حدود **۴۰ تا ۶۰ ساعت** کار جدی می‌خواهد.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [بعدی →](#پیشنیازهای-فاز-۲)

</div>


---

# پیش‌نیازهای فاز ۲

<details>
<summary>پیش‌نیازهای فاز ۲</summary>

قبل از شروع فاز ۲ باید این‌ها را بلد باشی:

```text
[ ] نصب و اجرای Nginx
[ ] ساخت server block
[ ] static file serving
[ ] root و alias
[ ] location matching پایه
[ ] reverse proxy
[ ] proxy_pass
[ ] proxy headers
[ ] upstream
[ ] basic load balancing
[ ] HTTPS self-signed
[ ] خواندن access.log و error.log
[ ] debug کردن 502، 403، 404، 504
```

اگر این‌ها هنوز برایت مبهم‌اند، فاز ۱ را سریع مرور کن. فاز ۲ روی همان‌ها ساخته می‌شود.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#هدف-فاز-۲) · [بعدی →](#تصویر-ذهنی-فاز-۲)

</div>


---

# تصویر ذهنی فاز ۲

<details>
<summary>تصویر ذهنی فاز ۲</summary>

در production، Nginx فقط یک واسطه ساده نیست. Nginx جلوی سیستم می‌ایستد و باید جلوی خیلی از مشکلات را بگیرد.

```text
Internet
  ↓
Nginx
  ├── TLS termination
  ├── Request routing
  ├── Rate limiting
  ├── Static serving
  ├── Caching
  ├── Compression
  ├── Logging
  ├── Failure handling
  └── Reverse proxy
        ↓
      Apps / APIs / Services
```

هدف این فاز این است که برای هرکدام از این نقش‌ها config قابل دفاع داشته باشی.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#پیشنیازهای-فاز-۲) · [بعدی →](#هفته-۱-production-reverse-proxy)

</div>


---

# هفته ۱: Production Reverse Proxy

<details>
<summary>هفته ۱: Production Reverse Proxy</summary>

## روز ۱: ساختار Production Config

در فاز ۱ احتمالاً config ساده‌ای مثل این داشتی:

```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000;
    }
}
```

برای production این کافی نیست.

یک ساختار بهتر:

```text
/etc/nginx/
  nginx.conf
  sites-available/
    app.conf
  sites-enabled/
    app.conf -> ../sites-available/app.conf
  snippets/
    proxy-headers.conf
    proxy-timeouts.conf
    ssl-params.conf
    security-headers.conf
```

هدف این است که configها readable و reusable باشند.

---

## snippet برای proxy headers

فایل:

```text
/etc/nginx/snippets/proxy-headers.conf
```

محتوا:

```nginx
proxy_http_version 1.1;

proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Host $host;
proxy_set_header X-Forwarded-Port $server_port;
```

استفاده:

```nginx
location / {
    proxy_pass http://app_backend;
    include snippets/proxy-headers.conf;
}
```

## چرا این مهم است؟

Backend معمولاً باید بداند:

* request اصلی از چه IP آمده
* request اصلی HTTP بوده یا HTTPS
* host اصلی چه بوده
* آیا پشت proxy است یا نه

بدون این headerها، backend ممکن است redirect اشتباه بسازد، IP کاربر را اشتباه تشخیص دهد یا HTTPS را درست detect نکند.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#تصویر-ذهنی-فاز-۲) · [بعدی →](#روز-۲-timeoutهای-مهم)

</div>


---

# روز ۲: Timeoutهای مهم

<details>
<summary>روز ۲: Timeoutهای مهم</summary>

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

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#هفته-۱-production-reverse-proxy) · [بعدی →](#روز-۳-buffering)

</div>


---

# روز ۳: Buffering

<details>
<summary>روز ۳: Buffering</summary>

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

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۲-timeoutهای-مهم) · [بعدی →](#روز-۴-request-body-و-upload-limits)

</div>


---

# روز ۴: Request Body و Upload Limits

<details>
<summary>روز ۴: Request Body و Upload Limits</summary>

در production باید محدودیت request body داشته باشی.

Directive مهم:

```nginx
client_max_body_size 10m;
```

اگر upload داری، ممکن است بیشتر نیاز باشد:

```nginx
client_max_body_size 50m;
```

برای مسیر خاص:

```nginx
location /api/uploads/ {
    client_max_body_size 100m;

    proxy_pass http://api_backend/;
    include snippets/proxy-headers.conf;
    include snippets/proxy-timeouts.conf;
}
```

## چرا مهم است؟

بدون limit درست:

* کاربر می‌تواند body خیلی بزرگ بفرستد
* memory/disk فشار می‌گیرد
* backend درگیر request غیرضروری می‌شود
* امکان abuse بیشتر می‌شود

## تمرین

با `curl` فایل بزرگ بفرست:

```bash
dd if=/dev/zero of=/tmp/test-20mb.bin bs=1M count=20
curl -i -X POST --data-binary @/tmp/test-20mb.bin http://localhost/api/upload
```

اگر `client_max_body_size 10m` باشد، باید خطای `413 Request Entity Too Large` ببینی.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۳-buffering) · [بعدی →](#روز-۵-proxy-error-handling)

</div>


---

# روز ۵: Proxy Error Handling

<details>
<summary>روز ۵: Proxy Error Handling</summary>

در production بهتر است صفحه یا response خطا را کنترل کنی.

نمونه:

```nginx
proxy_intercept_errors on;

error_page 502 503 504 /50x.html;

location = /50x.html {
    root /var/www/errors;
    internal;
}
```

فایل بساز:

```bash
sudo mkdir -p /var/www/errors
echo "<h1>Service temporarily unavailable</h1>" | sudo tee /var/www/errors/50x.html
```

## نکته

برای API بهتر است HTML برنگردانی. برای API می‌توانی JSON برگردانی:

```nginx
location = /api-50x.json {
    internal;
    default_type application/json;
    return 503 '{"error":"service_unavailable","message":"Service temporarily unavailable"}';
}
```

و در location API:

```nginx
location /api/ {
    proxy_pass http://api_backend/;
    proxy_intercept_errors on;
    error_page 502 503 504 = /api-50x.json;

    include snippets/proxy-headers.conf;
    include snippets/proxy-timeouts.conf;
}
```

## تمرین

Backend را خاموش کن و تست کن:

```bash
curl -i http://localhost/api/users
```

باید response کنترل‌شده ببینی، نه صفحه خام Nginx.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۴-request-body-و-upload-limits) · [بعدی →](#هفته-۲-load-balancing-و-failure-behavior)

</div>


---

# هفته ۲: Load Balancing و Failure Behavior

<details>
<summary>هفته ۲: Load Balancing و Failure Behavior</summary>

## روز ۶: Upstream Production Config

Config ساده:

```nginx
upstream app_backend {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
```

Config production-like:

```nginx
upstream app_backend {
    least_conn;

    server 127.0.0.1:3001 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:3002 max_fails=3 fail_timeout=10s;
    keepalive 32;
}
```

## معنی directiveها

| Directive      | معنی                                               |
| -------------- | -------------------------------------------------- |
| `least_conn`   | request جدید به backend با connection کمتر برود    |
| `max_fails`    | تعداد fail مجاز قبل از temporarily unavailable شدن |
| `fail_timeout` | بازه زمانی fail و مدت کنار گذاشتن server           |
| `keepalive`    | connection reuse بین Nginx و upstream              |

## نکته مهم درباره keepalive

اگر در upstream از `keepalive` استفاده می‌کنی، در location باید HTTP/1.1 ست شود:

```nginx
proxy_http_version 1.1;
proxy_set_header Connection "";
```

Config بهتر برای upstream keepalive:

```nginx
upstream app_backend {
    least_conn;

    server 127.0.0.1:3001 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:3002 max_fails=3 fail_timeout=10s;

    keepalive 32;
}

server {
    listen 80;

    location / {
        proxy_pass http://app_backend;

        proxy_http_version 1.1;
        proxy_set_header Connection "";

        include snippets/proxy-headers.conf;
        include snippets/proxy-timeouts.conf;
    }
}
```

## تمرین

سه app اجرا کن:

```bash
PORT=3001 INSTANCE=app-1 node server.js
PORT=3002 INSTANCE=app-2 node server.js
PORT=3003 INSTANCE=app-3 node server.js
```

Nginx را به سه app وصل کن.

بعد تست:

```bash
for i in {1..30}; do curl -s http://localhost | jq; done
```

یکی از appها را kill کن و error log را ببین:

```bash
sudo tail -f /var/log/nginx/error.log
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۵-proxy-error-handling) · [بعدی →](#روز-۷-retry-behavior)

</div>


---

# روز ۷: Retry Behavior

<details>
<summary>روز ۷: Retry Behavior</summary>

Directive مهم:

```nginx
proxy_next_upstream error timeout http_502 http_503 http_504;
```

مثال:

```nginx
location / {
    proxy_pass http://app_backend;

    proxy_next_upstream error timeout http_502 http_503 http_504;
    proxy_next_upstream_tries 2;
    proxy_next_upstream_timeout 10s;

    include snippets/proxy-headers.conf;
    include snippets/proxy-timeouts.conf;
}
```

## معنی

اگر upstream اول fail شد، Nginx می‌تواند request را به upstream بعدی امتحان کند.

## هشدار مهم

برای requestهای غیر idempotent مثل `POST`, `PATCH`, `DELETE` باید خیلی مراقب retry باشی.

مثلاً اگر یک `POST /payments` دوبار ارسال شود، ممکن است دوبار پرداخت ثبت شود.

برای APIهای حساس، retry را محدود و آگاهانه تنظیم کن.

## تفکیک GET و POST

برای مسیرهای safe:

```nginx
location /api/read/ {
    proxy_pass http://api_backend/;

    proxy_next_upstream error timeout http_502 http_503 http_504;
    proxy_next_upstream_tries 2;

    include snippets/proxy-headers.conf;
}
```

برای مسیرهای حساس:

```nginx
location /api/payments/ {
    proxy_pass http://api_backend/;

    proxy_next_upstream off;

    include snippets/proxy-headers.conf;
}
```

## تمرین

یک endpoint بساز که گاهی 502 یا timeout بدهد. سپس ببین Nginx چطور request را retry می‌کند.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#هفته-۲-load-balancing-و-failure-behavior) · [بعدی →](#روز-۸-sticky-session-concept)

</div>


---

# روز ۸: Sticky Session Concept

<details>
<summary>روز ۸: Sticky Session Concept</summary>

در Nginx open source، sticky session رسمی مثل NGINX Plus ساده و آماده نیست، اما می‌توانی با `ip_hash` رفتار نزدیک بسازی.

```nginx
upstream app_backend {
    ip_hash;

    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
```

## معنی

بر اساس IP client، requestها معمولاً به یک backend ثابت می‌روند.

## مشکل

اگر همه کاربران پشت NAT، Cloudflare یا load balancer بالادستی باشند، IP ممکن است واقعی نباشد یا همه کاربران شبیه هم دیده شوند.

پس `ip_hash` همیشه راه‌حل خوب نیست.

## توصیه

اگر اپلیکیشن session state دارد، بهتر است state را از process خارج کنی:

```text
App Instance 1
App Instance 2
App Instance 3
   ↓
Redis / Database / External Session Store
```

این بهتر از وابسته شدن به sticky session است.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۷-retry-behavior) · [بعدی →](#روز-۹-health-endpoint-و-readiness)

</div>


---

# روز ۹: Health Endpoint و Readiness

<details>
<summary>روز ۹: Health Endpoint و Readiness</summary>

حتی اگر Nginx open source active health check پیشرفته نداشته باشد، خودت باید در app endpointهای سلامت داشته باشی.

حداقل:

```text
GET /health
GET /ready
```

فرق:

| Endpoint  | معنی                         |
| --------- | ---------------------------- |
| `/health` | process زنده است             |
| `/ready`  | app آماده دریافت traffic است |

مثلاً `/ready` باید شاید database، redis یا dependency مهم را چک کند.

## Config Nginx برای health خود Nginx

```nginx
location = /nginx-health {
    access_log off;
    return 200 "ok\n";
}
```

## تمرین

برای app endpointهای زیر بساز:

```text
/health
/ready
```

بعد در Nginx route کن:

```nginx
location = /health {
    proxy_pass http://app_backend/health;
    include snippets/proxy-headers.conf;
}

location = /nginx-health {
    access_log off;
    return 200 "ok\n";
}
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۸-sticky-session-concept) · [بعدی →](#هفته-۳-caching-و-compression)

</div>


---

# هفته ۳: Caching و Compression

<details>
<summary>هفته ۳: Caching و Compression</summary>

## روز ۱۰: Static Asset Caching

برای فایل‌های static:

```nginx
location /assets/ {
    root /var/www/app;

    expires 30d;
    add_header Cache-Control "public, immutable";
}
```

برای فایل‌هایی که fingerprint دارند مثل:

```text
app.8f3a91.js
style.3b2ac.css
```

می‌توانی cache طولانی بدهی:

```nginx
location ~* \.(js|css|png|jpg|jpeg|gif|svg|ico|woff2)$ {
    root /var/www/app;

    expires 30d;
    add_header Cache-Control "public, immutable";
}
```

## نکته

فقط وقتی `immutable` بده که فایل‌ها fingerprint یا versioned باشند. اگر `app.js` ساده داری و ممکن است محتوا عوض شود، cache طولانی دردسر می‌سازد.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۹-health-endpoint-و-readiness) · [بعدی →](#روز-۱۱-proxy-cache)

</div>


---

# روز ۱۱: Proxy Cache

<details>
<summary>روز ۱۱: Proxy Cache</summary>

Nginx می‌تواند responseهای upstream را cache کند.

داخل `http` context:

```nginx
proxy_cache_path /var/cache/nginx/app_cache
    levels=1:2
    keys_zone=app_cache:10m
    max_size=1g
    inactive=60m
    use_temp_path=off;
```

داخل `location`:

```nginx
location /api/public/ {
    proxy_pass http://api_backend/;

    proxy_cache app_cache;
    proxy_cache_valid 200 10m;
    proxy_cache_valid 404 1m;

    add_header X-Cache-Status $upstream_cache_status;

    include snippets/proxy-headers.conf;
}
```

## معنی

| Directive                | معنی                                         |
| ------------------------ | -------------------------------------------- |
| `proxy_cache_path`       | مسیر و zone cache                            |
| `keys_zone`              | shared memory zone برای metadata             |
| `max_size`               | حداکثر حجم cache                             |
| `inactive`               | حذف آیتم‌هایی که مدت طولانی استفاده نشده‌اند |
| `proxy_cache_valid`      | مدت cache برای statusهای مختلف               |
| `$upstream_cache_status` | وضعیت cache: HIT, MISS, BYPASS, EXPIRED      |

## تست

```bash
curl -I http://localhost/api/public/posts
curl -I http://localhost/api/public/posts
```

بار اول احتمالاً:

```text
X-Cache-Status: MISS
```

بار دوم:

```text
X-Cache-Status: HIT
```

## هشدار

هر چیزی را cache نکن.

نباید cache کنی:

```text
- endpointهای user-specific
- dashboard شخصی
- اطلاعات محرمانه
- responseهایی با Authorization
- payment
- admin API
```

برای cache کردن API باید دقیق بدانی response عمومی است یا خصوصی.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#هفته-۳-caching-و-compression) · [بعدی →](#روز-۱۲-cache-bypass)

</div>


---

# روز ۱۲: Cache Bypass

<details>
<summary>روز ۱۲: Cache Bypass</summary>

برای requestهایی با Authorization بهتر است cache bypass شود.

```nginx
proxy_cache_bypass $http_authorization;
proxy_no_cache $http_authorization;
```

نمونه:

```nginx
location /api/public/ {
    proxy_pass http://api_backend/;

    proxy_cache app_cache;
    proxy_cache_valid 200 10m;

    proxy_cache_bypass $http_authorization;
    proxy_no_cache $http_authorization;

    add_header X-Cache-Status $upstream_cache_status;

    include snippets/proxy-headers.conf;
}
```

## Query String

به‌صورت پیش‌فرض cache key معمولاً شامل URI کامل با query string است. اما برای کنترل بهتر می‌توانی cache key تعریف کنی:

```nginx
proxy_cache_key "$scheme$request_method$host$request_uri";
```

## تمرین

این‌ها را تست کن:

```bash
curl -I http://localhost/api/public/posts
curl -I http://localhost/api/public/posts
curl -I -H "Authorization: Bearer test" http://localhost/api/public/posts
```

ببین cache status چطور تغییر می‌کند.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۱۱-proxy-cache) · [بعدی →](#روز-۱۳-compression)

</div>


---

# روز ۱۳: Compression

<details>
<summary>روز ۱۳: Compression</summary>

برای gzip:

```nginx
gzip on;
gzip_comp_level 5;
gzip_min_length 1024;
gzip_types
    text/plain
    text/css
    application/json
    application/javascript
    application/xml
    image/svg+xml;
```

این را معمولاً داخل `http` context می‌گذاری.

## نکته

همه چیز را gzip نکن.

معمولاً این‌ها مناسب‌اند:

```text
- HTML
- CSS
- JS
- JSON
- XML
- SVG
```

این‌ها معمولاً مناسب نیستند:

```text
- jpg
- png
- webp
- mp4
- zip
- pdf
```

چون از قبل compressed هستند.

## تست gzip

```bash
curl -H "Accept-Encoding: gzip" -I http://localhost/assets/app.js
```

دنبال این header بگرد:

```text
Content-Encoding: gzip
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۱۲-cache-bypass) · [بعدی →](#روز-۱۴-brotli-concept)

</div>


---

# روز ۱۴: Brotli Concept

<details>
<summary>روز ۱۴: Brotli Concept</summary>

Brotli معمولاً برای assetهای text-based compression بهتری نسبت به gzip دارد، مخصوصاً برای frontend assetها.

اما در Nginx open source ممکن است نیاز به module جدا داشته باشد، بسته به نحوه نصب و distro.

برای فاز ۲ کافی است مفهوم را بفهمی:

```text
gzip:
- رایج
- built-in در اکثر نصب‌ها
- ساده‌تر

brotli:
- compression بهتر
- گاهی نیازمند module جدا
- مناسب static assets
```

در production، اگر CDN جلوی سیستم داری، ممکن است compression را CDN انجام دهد و Nginx لازم نباشد همه بار compression را بردارد.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۱۳-compression) · [بعدی →](#هفته-۴-rate-limiting،-security-headers-و-observability)

</div>


---

# هفته ۴: Rate Limiting، Security Headers و Observability

<details>
<summary>هفته ۴: Rate Limiting، Security Headers و Observability</summary>

## روز ۱۵: Rate Limiting

Rate limit برای کنترل abuse و burst مهم است.

داخل `http` context:

```nginx
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
```

داخل location:

```nginx
location /api/ {
    limit_req zone=api_limit burst=20 nodelay;

    proxy_pass http://api_backend/;
    include snippets/proxy-headers.conf;
}
```

## معنی

| بخش                   | معنی                                               |
| --------------------- | -------------------------------------------------- |
| `$binary_remote_addr` | IP client به شکل compact                           |
| `zone=api_limit:10m`  | shared memory zone برای tracking                   |
| `rate=10r/s`          | ۱۰ request در ثانیه                                |
| `burst=20`            | اجازه burst موقت                                   |
| `nodelay`             | requestهای burst را معطل نکن؛ یا قبول یا reject کن |

## تست

```bash
for i in {1..100}; do curl -s -o /dev/null -w "%{http_code}\n" http://localhost/api/test; done
```

باید بخشی از requestها `503` یا status مربوط به limit ببینند.

برای status سفارشی:

```nginx
limit_req_status 429;
```

بهتر:

```nginx
limit_req_status 429;
```

حالا rate limit response با `429 Too Many Requests` برمی‌گردد.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۱۴-brotli-concept) · [بعدی →](#روز-۱۶-connection-limiting)

</div>


---

# روز ۱۶: Connection Limiting

<details>
<summary>روز ۱۶: Connection Limiting</summary>

Rate limit تعداد requestها را کنترل می‌کند. Connection limit تعداد connectionهای همزمان را.

داخل `http`:

```nginx
limit_conn_zone $binary_remote_addr zone=conn_limit:10m;
```

داخل `server` یا `location`:

```nginx
limit_conn conn_limit 20;
```

یعنی هر IP حداکثر ۲۰ connection همزمان داشته باشد.

## استفاده پیشنهادی

```nginx
location /api/ {
    limit_conn conn_limit 20;
    limit_req zone=api_limit burst=20 nodelay;

    proxy_pass http://api_backend/;
    include snippets/proxy-headers.conf;
}
```

## هشدار

اگر کاربران پشت NAT یا proxy مشترک باشند، محدودیت بر اساس IP می‌تواند کاربران واقعی را اذیت کند.

اگر پشت Cloudflare یا load balancer هستی، باید real IP را درست تنظیم کنی، وگرنه همه requestها از IP proxy دیده می‌شوند.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#هفته-۴-rate-limiting،-security-headers-و-observability) · [بعدی →](#روز-۱۷-security-headers-پایه)

</div>


---

# روز ۱۷: Security Headers پایه

<details>
<summary>روز ۱۷: Security Headers پایه</summary>

فایل:

```text
/etc/nginx/snippets/security-headers.conf
```

محتوا:

```nginx
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header X-XSS-Protection "0" always;
```

برای HTTPS:

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

## هشدار درباره HSTS

`HSTS` را با احتیاط فعال کن، مخصوصاً `includeSubDomains`.

اگر اشتباه ست شود، مرورگرها تا مدت طولانی سایت را فقط با HTTPS باز می‌کنند. برای دامنه production خوب است، ولی برای lab یا دامنه‌ای که HTTPS کامل ندارد خطرناک است.

## Content Security Policy

CSP خیلی مهم است، ولی نباید کورکورانه اضافه شود.

مثال ساده:

```nginx
add_header Content-Security-Policy "default-src 'self'" always;
```

اما برای اپلیکیشن‌های واقعی معمولاً assetها، API، analytics، fontها و CDNها باعث پیچیدگی می‌شوند.

در فاز ۲ فقط concept را بفهم. CSP جدی را در فاز Security عمیق‌تر بخوان.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۱۶-connection-limiting) · [بعدی →](#روز-۱۸-real-ip-handling)

</div>


---

# روز ۱۸: Real IP Handling

<details>
<summary>روز ۱۸: Real IP Handling</summary>

اگر Nginx پشت Cloudflare، AWS ELB، Kubernetes ingress یا یک load balancer دیگر باشد، `$remote_addr` ممکن است IP واقعی کاربر نباشد.

مثلاً:

```text
User
  ↓
Cloudflare
  ↓
Nginx
  ↓
App
```

از دید Nginx، client ممکن است Cloudflare باشد، نه user.

Config concept:

```nginx
set_real_ip_from 10.0.0.0/8;
real_ip_header X-Forwarded-For;
real_ip_recursive on;
```

## هشدار بسیار مهم

هرگز کورکورانه این کار را نکن:

```nginx
set_real_ip_from 0.0.0.0/0;
```

چون در این صورت هر client می‌تواند `X-Forwarded-For` جعلی بفرستد و IP خودش را جعل کند.

فقط IPهای trusted proxy را داخل `set_real_ip_from` بگذار.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۱۷-security-headers-پایه) · [بعدی →](#روز-۱۹-custom-access-log-برای-production)

</div>


---

# روز ۱۹: Custom Access Log برای Production

<details>
<summary>روز ۱۹: Custom Access Log برای Production</summary>

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

حتماً این‌ها را داشته باش:

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

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۱۸-real-ip-handling) · [بعدی →](#روز-۲۰-request-id)

</div>


---

# روز ۲۰: Request ID

<details>
<summary>روز ۲۰: Request ID</summary>

برای trace کردن request بین Nginx و backend، request id مهم است.

Nginx variable داخلی دارد:

```nginx
$request_id
```

به backend پاس بده:

```nginx
proxy_set_header X-Request-ID $request_id;
```

در snippet proxy headers اضافه کن:

```nginx
proxy_set_header X-Request-ID $request_id;
```

حالا backend هم باید همین request id را log کند.

## نتیجه

وقتی مشکلی پیش آمد، می‌توانی یک request را از Nginx تا backend دنبال کنی:

```text
Nginx access.log:
request_id=abc123

Backend log:
request_id=abc123
```

این یکی از ساده‌ترین و مفیدترین کارهای production observability است.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۱۹-custom-access-log-برای-production) · [بعدی →](#هفته-۵-https-production-و-deployment-hygiene)

</div>


---

# هفته ۵: HTTPS Production و Deployment Hygiene

<details>
<summary>هفته ۵: HTTPS Production و Deployment Hygiene</summary>

## روز ۲۱: HTTPS جدی‌تر

در فاز ۱ self-signed کافی بود. در production باید certificate معتبر داشته باشی.

روش رایج:

```text
Let's Encrypt + Certbot
```

روی Ubuntu معمولاً:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d example.com -d www.example.com
```

بعد renew را بررسی کن:

```bash
sudo systemctl status certbot.timer
```

تست renew:

```bash
sudo certbot renew --dry-run
```

## نکته

برای production واقعی باید قبل از فعال‌سازی HSTS، مطمئن باشی:

```text
[ ] certificate معتبر است
[ ] auto-renew کار می‌کند
[ ] همه subdomainهای لازم HTTPS دارند
[ ] redirectها درست‌اند
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۲۰-request-id) · [بعدی →](#روز-۲۲-ssl-parameters)

</div>


---

# روز ۲۲: SSL Parameters

<details>
<summary>روز ۲۲: SSL Parameters</summary>

snippet:

```text
/etc/nginx/snippets/ssl-params.conf
```

نمونه ساده:

```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers off;

ssl_session_cache shared:SSL:10m;
ssl_session_timeout 1d;
ssl_session_tickets off;
```

استفاده:

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    include snippets/ssl-params.conf;

    location / {
        proxy_pass http://app_backend;
        include snippets/proxy-headers.conf;
    }
}
```

## نکته

Cipherها و تنظیمات TLS با زمان تغییر می‌کنند. برای production واقعی بهتر است از Mozilla SSL Configuration Generator یا guidelineهای معتبر به‌روز استفاده کنی.

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#هفته-۵-https-production-و-deployment-hygiene) · [بعدی →](#روز-۲۳-http2)

</div>


---

# روز ۲۳: HTTP/2

<details>
<summary>روز ۲۳: HTTP/2</summary>

برای فعال‌سازی HTTP/2:

```nginx
listen 443 ssl http2;
```

یا در نسخه‌های جدیدتر Nginx ممکن است syntax جدا توصیه شود:

```nginx
listen 443 ssl;
http2 on;
```

## چرا HTTP/2؟

* multiplexing
* header compression
* performance بهتر برای assetهای متعدد
* کاهش نیاز به چند connection جدا

## تست

```bash
curl -I --http2 https://example.com
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۲۲-ssl-parameters) · [بعدی →](#روز-۲۴-graceful-reload-و-config-safety)

</div>


---

# روز ۲۴: Graceful Reload و Config Safety

<details>
<summary>روز ۲۴: Graceful Reload و Config Safety</summary>

قبل از هر reload:

```bash
sudo nginx -t
```

بعد:

```bash
sudo systemctl reload nginx
```

نه همیشه restart.

## فرق reload و restart

| دستور   | رفتار                                                                 |
| ------- | --------------------------------------------------------------------- |
| reload  | config جدید را بدون قطع ناگهانی connectionهای فعال اعمال می‌کند       |
| restart | process را متوقف و دوباره اجرا می‌کند؛ ممکن است connectionها قطع شوند |

## deploy script ساده

```bash
#!/usr/bin/env bash
set -e

sudo nginx -t
sudo systemctl reload nginx
```

ذخیره:

```text
/usr/local/bin/nginx-safe-reload
```

اجراپذیر کردن:

```bash
sudo chmod +x /usr/local/bin/nginx-safe-reload
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۲۳-http2) · [بعدی →](#روز-۲۵-backup-و-rollback)

</div>


---

# روز ۲۵: Backup و Rollback

<details>
<summary>روز ۲۵: Backup و Rollback</summary>

قبل از تغییر بزرگ:

```bash
sudo cp /etc/nginx/sites-available/app.conf /etc/nginx/sites-available/app.conf.bak
```

یا بهتر: configها را در Git نگه دار.

ساختار repo:

```text
infra-nginx/
  nginx.conf
  sites-available/
    app.conf
  snippets/
    proxy-headers.conf
    proxy-timeouts.conf
    ssl-params.conf
    security-headers.conf
  README.md
```

## قانون مهم

تغییرات Nginx production نباید دستی و بدون history باشد.

حداقل باید بدانی:

```text
- چه کسی تغییر داد
- چه چیزی تغییر کرد
- چرا تغییر کرد
- چطور rollback کنیم
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۲۴-graceful-reload-و-config-safety) · [بعدی →](#هفته-۶-final-production-lab)

</div>


---

# هفته ۶: Final Production Lab

<details>
<summary>هفته ۶: Final Production Lab</summary>

در هفته آخر باید همه چیز را ترکیب کنی.

## معماری نهایی

```text
Internet
  ↓
Nginx
  ├── HTTP → HTTPS redirect
  ├── TLS termination
  ├── HTTP/2
  ├── Security headers
  ├── Rate limiting
  ├── Connection limiting
  ├── Static asset caching
  ├── Proxy cache for public API
  ├── JSON access logs
  ├── Request ID
  ├── Custom error responses
  └── Reverse proxy
        ├── frontend_app
        └── api_backend
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#روز-۲۵-backup-و-rollback) · [بعدی →](#config-نهایی-نمونه)

</div>


---

# Config نهایی نمونه

<details>
<summary>Config نهایی نمونه</summary>

## `/etc/nginx/snippets/proxy-headers.conf`

```nginx
proxy_http_version 1.1;

proxy_set_header Connection "";
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Host $host;
proxy_set_header X-Forwarded-Port $server_port;
proxy_set_header X-Request-ID $request_id;
```

---

## `/etc/nginx/snippets/proxy-timeouts.conf`

```nginx
proxy_connect_timeout 5s;
proxy_send_timeout 30s;
proxy_read_timeout 30s;
send_timeout 30s;
```

---

## `/etc/nginx/snippets/security-headers.conf`

```nginx
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header X-XSS-Protection "0" always;
```

برای HTTPS production بعد از اطمینان:

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

---

## `/etc/nginx/snippets/ssl-params.conf`

```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers off;

ssl_session_cache shared:SSL:10m;
ssl_session_timeout 1d;
ssl_session_tickets off;
```

---

## بخش‌هایی در `http` context

داخل `/etc/nginx/nginx.conf` در context `http`:

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

limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
limit_conn_zone $binary_remote_addr zone=conn_limit:10m;

proxy_cache_path /var/cache/nginx/app_cache
    levels=1:2
    keys_zone=app_cache:10m
    max_size=1g
    inactive=60m
    use_temp_path=off;

gzip on;
gzip_comp_level 5;
gzip_min_length 1024;
gzip_types
    text/plain
    text/css
    application/json
    application/javascript
    application/xml
    image/svg+xml;

upstream frontend_app {
    server 127.0.0.1:3000 max_fails=3 fail_timeout=10s;
    keepalive 16;
}

upstream api_backend {
    least_conn;

    server 127.0.0.1:4001 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:4002 max_fails=3 fail_timeout=10s;

    keepalive 32;
}
```

---

## `/etc/nginx/sites-available/app.conf`

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com www.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    include snippets/ssl-params.conf;

    access_log /var/log/nginx/app.access.log production_json;
    error_log /var/log/nginx/app.error.log warn;

    include snippets/security-headers.conf;

    client_max_body_size 20m;

    limit_conn conn_limit 20;

    location = /nginx-health {
        access_log off;
        return 200 "ok\n";
    }

    location = /api-50x.json {
        internal;
        default_type application/json;
        return 503 '{"error":"service_unavailable","message":"Service temporarily unavailable","request_id":"$request_id"}';
    }

    location /assets/ {
        root /var/www/app;

        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /uploads/ {
        alias /var/www/uploads/;
        try_files $uri =404;

        expires 7d;
        add_header Cache-Control "public";
    }

    location /api/public/ {
        limit_req zone=api_limit burst=20 nodelay;
        limit_req_status 429;

        proxy_pass http://api_backend/;

        proxy_cache app_cache;
        proxy_cache_valid 200 10m;
        proxy_cache_valid 404 1m;
        proxy_cache_bypass $http_authorization;
        proxy_no_cache $http_authorization;
        proxy_cache_key "$scheme$request_method$host$request_uri";

        add_header X-Cache-Status $upstream_cache_status always;

        proxy_intercept_errors on;
        error_page 502 503 504 = /api-50x.json;

        proxy_next_upstream error timeout http_502 http_503 http_504;
        proxy_next_upstream_tries 2;
        proxy_next_upstream_timeout 10s;

        include snippets/proxy-headers.conf;
        include snippets/proxy-timeouts.conf;
    }

    location /api/ {
        limit_req zone=api_limit burst=20 nodelay;
        limit_req_status 429;

        proxy_pass http://api_backend/;

        proxy_intercept_errors on;
        error_page 502 503 504 = /api-50x.json;

        proxy_next_upstream error timeout http_502 http_503 http_504;
        proxy_next_upstream_tries 2;
        proxy_next_upstream_timeout 10s;

        include snippets/proxy-headers.conf;
        include snippets/proxy-timeouts.conf;
    }

    location / {
        proxy_pass http://frontend_app;

        include snippets/proxy-headers.conf;
        include snippets/proxy-timeouts.conf;
    }
}
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#هفته-۶-final-production-lab) · [بعدی →](#تستهای-نهایی-فاز-۲)

</div>


---

# تست‌های نهایی فاز ۲

<details>
<summary>تست‌های نهایی فاز ۲</summary>

## تست config

```bash
sudo nginx -t
sudo systemctl reload nginx
```

---

## تست HTTPS redirect

```bash
curl -I http://example.com
```

باید چیزی شبیه این ببینی:

```text
HTTP/1.1 301 Moved Permanently
Location: https://example.com/
```

---

## تست health

```bash
curl -i https://example.com/nginx-health
```

باید:

```text
HTTP/2 200
ok
```

---

## تست rate limit

```bash
for i in {1..100}; do
  curl -s -o /dev/null -w "%{http_code}\n" https://example.com/api/test
done
```

باید بخشی از requestها `429` شوند.

---

## تست cache

```bash
curl -I https://example.com/api/public/posts
curl -I https://example.com/api/public/posts
```

انتظار:

```text
X-Cache-Status: MISS
X-Cache-Status: HIT
```

---

## تست Authorization bypass

```bash
curl -I -H "Authorization: Bearer test" https://example.com/api/public/posts
```

نباید cache عمومی را مثل request بدون Authorization استفاده کند.

---

## تست upstream failure

یکی از backendها را خاموش کن:

```bash
pkill -f "PORT=4001"
```

بعد:

```bash
curl -i https://example.com/api/test
sudo tail -f /var/log/nginx/app.error.log
```

ببین Nginx request را به upstream دیگر retry می‌کند یا نه.

---

## تست custom error

همه backendهای API را خاموش کن:

```bash
pkill -f "PORT=400"
```

بعد:

```bash
curl -i https://example.com/api/test
```

باید JSON کنترل‌شده ببینی:

```json
{
  "error": "service_unavailable",
  "message": "Service temporarily unavailable",
  "request_id": "..."
}
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#config-نهایی-نمونه) · [بعدی →](#checklist-فاز-۲)

</div>


---

# Checklist فاز ۲

<details>
<summary>Checklist فاز ۲</summary>

در پایان فاز ۲ باید بتوانی این‌ها را انجام بدهی:

```text
[ ] ساختار production config بسازی
[ ] snippets reusable تعریف کنی
[ ] proxy headers استاندارد تنظیم کنی
[ ] timeoutهای مهم را توضیح بدهی
[ ] buffering را روشن/خاموش و اثر آن را بفهمی
[ ] request body limit تنظیم کنی
[ ] error response سفارشی بسازی
[ ] upstream با max_fails و fail_timeout تنظیم کنی
[ ] least_conn و round-robin را مقایسه کنی
[ ] retry behavior را کنترل کنی
[ ] خطر retry روی POST را بفهمی
[ ] sticky session concept را بفهمی
[ ] static asset caching تنظیم کنی
[ ] proxy cache برای API عمومی بسازی
[ ] cache bypass برای Authorization تنظیم کنی
[ ] gzip فعال کنی
[ ] rate limit بسازی
[ ] connection limit بسازی
[ ] security headers پایه اضافه کنی
[ ] real IP handling را بفهمی
[ ] JSON access log بسازی
[ ] request id را به backend پاس بدهی
[ ] HTTPS production با Let's Encrypt راه بیندازی
[ ] HTTP/2 فعال کنی
[ ] safe reload script بسازی
[ ] backup/rollback برای config داشته باشی
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#تستهای-نهایی-فاز-۲) · [بعدی →](#سؤالهایی-که-باید-بتوانی-جواب-بدهی)

</div>


---

# سؤال‌هایی که باید بتوانی جواب بدهی

<details>
<summary>سؤال‌هایی که باید بتوانی جواب بدهی</summary>

## Reverse Proxy

* چرا فقط `proxy_pass` برای production کافی نیست؟
* چه headerهایی باید به backend پاس داده شود؟
* `X-Forwarded-For` چه ریسکی دارد؟
* چرا `X-Forwarded-Proto` مهم است؟

## Timeout

* فرق `proxy_connect_timeout` و `proxy_read_timeout` چیست؟
* چرا timeout خیلی بالا خطرناک است؟
* چرا timeout خیلی پایین باعث false failure می‌شود؟
* برای endpointهای long-running چه کار باید کرد؟

## Buffering

* `proxy_buffering on` چه مزیتی دارد؟
* چه زمانی باید buffering را خاموش کرد؟
* چرا streaming با buffering مشکل دارد؟
* client کند چطور می‌تواند upstream را تحت فشار بگذارد؟

## Load Balancing

* round-robin چیست؟
* least_conn چه زمانی بهتر است؟
* `max_fails` و `fail_timeout` چه می‌کنند؟
* چرا sticky session معمولاً راه‌حل ایده‌آل نیست؟
* چرا session state بهتر است در Redis یا DB باشد؟

## Retry

* `proxy_next_upstream` چه می‌کند؟
* چرا retry کردن `POST` خطرناک است؟
* برای endpointهای payment چه strategy باید داشت؟
* `proxy_next_upstream_tries` چه چیزی را محدود می‌کند؟

## Caching

* چه endpointهایی را نباید cache کرد؟
* `X-Cache-Status` چه کمکی می‌کند؟
* فرق static asset cache و proxy cache چیست؟
* چرا `Authorization` باید cache را bypass کند؟
* چه زمانی `immutable` خطرناک است؟

## Rate Limiting

* فرق rate limit و connection limit چیست؟
* چرا limit بر اساس IP همیشه دقیق نیست؟
* چرا پشت Cloudflare باید real IP را درست تنظیم کرد؟
* چرا status بهتر برای rate limit معمولاً `429` است؟

## Observability

* چرا JSON log مفید است؟
* `$request_time` و `$upstream_response_time` چه فرقی دارند؟
* چرا `request_id` مهم است؟
* چطور یک request را از Nginx تا backend دنبال می‌کنی؟

## HTTPS

* چرا reload بهتر از restart است؟
* چرا auto-renew certificate مهم است؟
* چرا HSTS را نباید عجولانه فعال کرد؟
* HTTP/2 چه مزیتی دارد؟

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#checklist-فاز-۲) · [بعدی →](#برنامه-روزانه-پیشنهادی-فاز-۲)

</div>


---

# برنامه روزانه پیشنهادی فاز ۲

<details>
<summary>برنامه روزانه پیشنهادی فاز ۲</summary>

## هفته ۱: Production Reverse Proxy

### روز ۱

* ساختار production config
* snippets
* proxy headers

### روز ۲

* timeoutها
* تست endpoint کند
* 504 debugging

### روز ۳

* proxy buffering
* streaming endpoint
* buffering on/off

### روز ۴

* request body limit
* upload size
* 413 debugging

### روز ۵

* custom error response
* API error JSON
* upstream failure simulation

---

## هفته ۲: Load Balancing و Failure

### روز ۶

* upstream production config
* least_conn
* keepalive
* max_fails/fail_timeout

### روز ۷

* retry behavior
* proxy_next_upstream
* خطر retry روی POST

### روز ۸

* sticky session concept
* ip_hash
* external session store

### روز ۹

* health/readiness endpoint
* Nginx health endpoint
* readiness concept

---

## هفته ۳: Cache و Compression

### روز ۱۰

* static asset caching
* immutable
* cache headers

### روز ۱۱

* proxy_cache
* cache path
* X-Cache-Status

### روز ۱۲

* cache bypass
* Authorization
* cache key

### روز ۱۳

* gzip
* gzip_types
* تست compression

### روز ۱۴

* brotli concept
* CDN compression
* tradeoffها

---

## هفته ۴: Protection و Observability

### روز ۱۵

* rate limiting
* limit_req_zone
* 429

### روز ۱۶

* connection limiting
* NAT/proxy caveat

### روز ۱۷

* security headers
* HSTS warning
* CSP concept

### روز ۱۸

* real IP handling
* trusted proxy
* خطر spoofing

### روز ۱۹

* JSON log
* upstream timing variables

### روز ۲۰

* request id
* correlation بین Nginx و backend

---

## هفته ۵: HTTPS و Deployment Hygiene

### روز ۲۱

* Let's Encrypt
* Certbot
* renew dry-run

### روز ۲۲

* SSL params
* TLSv1.2/TLSv1.3
* session cache

### روز ۲۳

* HTTP/2
* تست با curl

### روز ۲۴

* graceful reload
* safe reload script

### روز ۲۵

* backup
* rollback
* Git برای config

---

## هفته ۶: Final Lab

### روز ۲۶ تا ۳۰

* ساخت lab نهایی
* تست cache
* تست rate limit
* تست failure
* تست timeout
* تست logs
* تست request id
* نوشتن گزارش نهایی

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#سؤالهایی-که-باید-بتوانی-جواب-بدهی) · [بعدی →](#گزارش-نهایی-فاز-۲)

</div>


---

# گزارش نهایی فاز ۲

<details>
<summary>گزارش نهایی فاز ۲</summary>

در پایان فاز ۲ یک فایل Markdown بساز:

```md

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#برنامه-روزانه-پیشنهادی-فاز-۲) · [بعدی →](#nginx-phase-2-production-report)

</div>


---

# Nginx Phase 2 Production Report

<details>
<summary>Nginx Phase 2 Production Report</summary>

## Architecture

Describe the final architecture.

## Config Structure

List config files and snippets.

## Reverse Proxy

Explain proxy headers and timeout values.

## Load Balancing

Explain upstream strategy.

## Failure Testing

### Backend Down

Result:

### Slow Backend

Result:

### Timeout

Result:

## Caching

### Static Asset Cache

Result:

### Proxy Cache

Result:

### Cache Bypass

Result:

## Rate Limiting

Rate:

Burst:

Status:

Result:

## Security Headers

List enabled headers.

## HTTPS

Certificate method:

HTTP to HTTPS redirect:

HTTP/2 enabled:

## Observability

Log format:

Request ID:

Important fields:

## Problems Found

List problems you encountered.

## Fixes Applied

List fixes.

## Lessons Learned

Write 15 lessons.
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#گزارش-نهایی-فاز-۲) · [بعدی →](#معیار-موفقیت-فاز-۲)

</div>


---

# معیار موفقیت فاز ۲

<details>
<summary>معیار موفقیت فاز ۲</summary>

فاز ۲ را زمانی واقعاً تمام کرده‌ای که بتوانی این سناریوها را بدون panic debug کنی:

```text
- backend خاموش شده و Nginx 502 می‌دهد
- backend کند شده و 504 می‌گیری
- بعضی requestها cache می‌شوند و بعضی نه
- کاربران زیادی request می‌زنند و rate limit فعال می‌شود
- upload بزرگ 413 می‌گیرد
- لاگ‌ها نشان می‌دهند کدام upstream کند است
- request id را از Nginx تا backend دنبال می‌کنی
- certificate renew را تست کرده‌ای
- قبل از reload کردن همیشه nginx -t می‌گیری
- می‌توانی config را rollback کنی
```

---

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#nginx-phase-2-production-report) · [بعدی →](#توصیه-جدی)

</div>


---

# توصیه جدی

<details>
<summary>توصیه جدی</summary>

در فاز ۲ عجله نکن.

Nginx production جایی نیست که فقط با copy/paste جلو بروی. هر directive که اضافه می‌کنی باید بتوانی جواب بدهی:

```text
چرا این را گذاشتم؟
اگر حذفش کنم چه می‌شود؟
اگر مقدارش زیاد شود چه می‌شود؟
اگر مقدارش کم شود چه می‌شود؟
تحت فشار چه رفتاری دارد؟
آیا روی امنیت اثر دارد؟
آیا روی backend اثر دارد؟
آیا قابل مشاهده و debug است؟
```

اگر این سؤال‌ها را برای config خودت جواب بدهی، داری Nginx را مهندسی می‌خوانی، نه حفظی.

</details>


<div align="center">

[↑ بالا](#فاز-۲-production-operations-در-nginx) · [← قبلی](#معیار-موفقیت-فاز-۲)

</div>


</div>
