حتماً. فاز ۱ باید کاملاً عملی، پایه‌ای و عمیق باشد. هدف این فاز این نیست که همه Nginx را یاد بگیری؛ هدف این است که **Nginx را به‌عنوان ابزار واقعی جلوی یک اپلیکیشن بفهمی و بتوانی با اعتمادبه‌نفس کانفیگ اولیه production-like بسازی.**

# فاز ۱: پایه عملی Nginx

## هدف اصلی فاز ۱

بعد از این فاز باید بتوانی این کارها را انجام بدهی:

* بفهمی Nginx دقیقاً کجای معماری سیستم می‌نشیند.
* یک اپلیکیشن واقعی مثل Node.js، Next.js، Laravel، Django یا هر backend دیگر را پشت Nginx قرار بدهی.
* static file سرو کنی.
* reverse proxy بنویسی.
* چند route مختلف را به چند سرویس مختلف وصل کنی.
* basic load balancing انجام بدهی.
* logها را بخوانی.
* HTTPS پایه راه بیندازی.
* مشکل‌های رایج مثل `502 Bad Gateway`، `404`، `403` و timeout را debug کنی.

مدت پیشنهادی: **۲ تا ۳ هفته**

اگر روزی ۱ تا ۲ ساعت وقت بگذاری، این فاز در ۲۰ تا ۳۰ ساعت قابل جمع شدن است.

---

# تصویر ذهنی درست از Nginx

اول باید جایگاه Nginx را بفهمی.

معمولاً کاربر مستقیم با اپلیکیشن تو حرف نمی‌زند. درخواست اول به Nginx می‌رسد، بعد Nginx تصمیم می‌گیرد با آن چه کند.

```text
User / Browser
      ↓
    Nginx
      ↓
Application Server
Node.js / Next.js / Django / Laravel / Go / ...
```

Nginx می‌تواند چند نقش داشته باشد:

```text
Nginx as:
- Web Server
- Reverse Proxy
- Load Balancer
- SSL/TLS Terminator
- Static File Server
- Cache Layer
- Security Gate
- API Gateway سبک
```

در فاز ۱ فعلاً فقط این نقش‌ها را جدی می‌گیریم:

```text
- Web Server
- Reverse Proxy
- Static File Server
- Basic Load Balancer
- Basic HTTPS Gateway
```

---

# هفته اول: فهم ساختار Nginx و کانفیگ پایه

## روز ۱: نصب و اجرای اولیه

### چیزهایی که باید یاد بگیری

* Nginx چطور نصب می‌شود.
* سرویس Nginx چطور start/stop/reload می‌شود.
* فایل‌های اصلی کجا هستند.
* config syntax چطور validate می‌شود.

روی Ubuntu/Debian:

```bash
sudo apt update
sudo apt install nginx
```

بررسی وضعیت:

```bash
sudo systemctl status nginx
```

شروع:

```bash
sudo systemctl start nginx
```

توقف:

```bash
sudo systemctl stop nginx
```

ری‌استارت:

```bash
sudo systemctl restart nginx
```

reload بدون قطع connectionهای فعال:

```bash
sudo systemctl reload nginx
```

تست صحت config:

```bash
sudo nginx -t
```

نمایش config نهایی که Nginx واقعاً می‌بیند:

```bash
sudo nginx -T
```

این دستور خیلی مهم است. چون ممکن است configها از چند فایل include شده باشند و تو فقط یک فایل را ببینی.

---

## فایل‌ها و مسیرهای مهم

در Ubuntu معمولاً این‌ها را می‌بینی:

```text
/etc/nginx/nginx.conf
/etc/nginx/sites-available/
/etc/nginx/sites-enabled/
/var/log/nginx/access.log
/var/log/nginx/error.log
/usr/share/nginx/html/
```

معنی‌شان:

| مسیر                          | کاربرد                           |
| ----------------------------- | -------------------------------- |
| `/etc/nginx/nginx.conf`       | config اصلی                      |
| `/etc/nginx/sites-available/` | فایل‌های سایت‌های قابل فعال‌سازی |
| `/etc/nginx/sites-enabled/`   | سایت‌های فعال‌شده                |
| `/var/log/nginx/access.log`   | لاگ requestها                    |
| `/var/log/nginx/error.log`    | لاگ خطاها                        |
| `/usr/share/nginx/html/`      | مسیر پیش‌فرض static files        |

در بعضی distroها مثل CentOS/RHEL ساختار فرق می‌کند و ممکن است `conf.d` بیشتر استفاده شود:

```text
/etc/nginx/conf.d/
```

---

# ساختار کلی Nginx config

Nginx config از context و directive ساخته می‌شود.

نمونه ساده:

```nginx
user www-data;

worker_processes auto;

events {
    worker_connections 1024;
}

http {
    server {
        listen 80;
        server_name example.com;

        location / {
            root /var/www/html;
            index index.html;
        }
    }
}
```

## مفهوم directive

هر خطی مثل این یک directive است:

```nginx
worker_processes auto;
```

یا:

```nginx
listen 80;
```

Directiveها معمولاً با `;` تمام می‌شوند.

## مفهوم context یا block

هر چیزی که داخل `{}` است یک context است:

```nginx
http {
    server {
        location / {
        }
    }
}
```

contextهای مهم:

```text
main
events
http
server
location
upstream
```

---

# معنی contextهای مهم

## 1. main context

بیرون از همه blockهاست.

```nginx
user www-data;
worker_processes auto;
pid /run/nginx.pid;
```

اینجا تنظیمات سطح کل process تعریف می‌شود.

مثلاً:

```nginx
worker_processes auto;
```

یعنی Nginx خودش بر اساس CPU تعداد workerها را تعیین کند.

---

## 2. events context

مربوط به connection handling است.

```nginx
events {
    worker_connections 1024;
}
```

فعلاً فقط این را بدان:

```nginx
worker_connections 1024;
```

یعنی هر worker حداکثر چند connection می‌تواند مدیریت کند.

ولی اشتباه رایج این است که فکر کنیم:

```text
worker_processes × worker_connections = تعداد request همزمان
```

تقریباً هست، ولی دقیق نیست. چون connection با request فرق دارد. keep-alive، upstream connection و فایل‌ها هم اثر دارند.

در فازهای بعد عمیق‌تر می‌خوانی.

---

## 3. http context

همه تنظیمات مربوط به HTTP داخل این context می‌آید:

```nginx
http {
    include /etc/nginx/mime.types;

    server {
        listen 80;
        server_name example.com;
    }
}
```

اینجا مواردی مثل این تعریف می‌شوند:

```text
log format
gzip
proxy settings
server blocks
upstream blocks
mime types
timeouts
```

---

## 4. server context

هر `server` معمولاً نماینده یک سایت، دامنه یا virtual host است.

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        root /var/www/example;
        index index.html;
    }
}
```

یعنی:

```text
اگر request روی پورت 80 آمد
و Host برابر example.com بود
این server block مسئول پاسخ دادن است
```

---

## 5. location context

`location` تصمیم می‌گیرد با مسیرهای مختلف URL چه شود.

مثلاً:

```nginx
location / {
    proxy_pass http://localhost:3000;
}

location /static/ {
    root /var/www/app;
}
```

یعنی:

```text
/        → برو سمت app
/static/ → فایل static بده
```

---

## 6. upstream context

برای تعریف گروهی از backendها استفاده می‌شود.

```nginx
upstream app_servers {
    server 127.0.0.1:3000;
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
```

بعد در `proxy_pass` استفاده می‌کنی:

```nginx
location / {
    proxy_pass http://app_servers;
}
```

این یعنی Nginx بین چند backend load balance می‌کند.

---

# تمرین روز ۱

یک فایل HTML ساده بساز:

```bash
sudo mkdir -p /var/www/nginx-lab
echo "<h1>Hello from Nginx</h1>" | sudo tee /var/www/nginx-lab/index.html
```

یک config بساز:

```bash
sudo nano /etc/nginx/sites-available/nginx-lab
```

محتوا:

```nginx
server {
    listen 80;
    server_name _;

    root /var/www/nginx-lab;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

فعال کردن:

```bash
sudo ln -s /etc/nginx/sites-available/nginx-lab /etc/nginx/sites-enabled/nginx-lab
sudo nginx -t
sudo systemctl reload nginx
```

حالا در browser یا curl:

```bash
curl http://localhost
```

باید ببینی:

```html
<h1>Hello from Nginx</h1>
```

---

# نکته مهم: `root` و `try_files`

این بخش خیلی مهم است چون خیلی‌ها با همین گیر می‌کنند.

```nginx
root /var/www/nginx-lab;
```

یعنی مسیر فایل‌ها از این directory شروع می‌شود.

```nginx
location / {
    try_files $uri $uri/ =404;
}
```

یعنی:

```text
اول دنبال فایل دقیق بگرد
بعد دنبال directory بگرد
اگر نبود 404 بده
```

مثلاً request:

```text
/about.html
```

Nginx دنبال این فایل می‌گردد:

```text
/var/www/nginx-lab/about.html
```

---

# هفته اول، روز ۲: static file serving

حالا باید static serving را درست بفهمی.

ساختار بساز:

```bash
sudo mkdir -p /var/www/nginx-lab/assets
echo "<h1>Home</h1>" | sudo tee /var/www/nginx-lab/index.html
echo "<h1>About</h1>" | sudo tee /var/www/nginx-lab/about.html
echo "body { font-family: sans-serif; }" | sudo tee /var/www/nginx-lab/assets/style.css
```

config:

```nginx
server {
    listen 80;
    server_name _;

    root /var/www/nginx-lab;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location /assets/ {
        expires 7d;
        add_header Cache-Control "public";
    }
}
```

تست:

```bash
curl -I http://localhost/assets/style.css
```

باید headerهای cache را ببینی.

---

## تفاوت `root` و `alias`

این یکی از مهم‌ترین دام‌های Nginx است.

### با root

```nginx
location /images/ {
    root /var/www/app;
}
```

Request:

```text
/images/a.png
```

File path:

```text
/var/www/app/images/a.png
```

### با alias

```nginx
location /images/ {
    alias /data/uploads/;
}
```

Request:

```text
/images/a.png
```

File path:

```text
/data/uploads/a.png
```

پس:

```text
root مسیر URL را به مسیر filesystem اضافه می‌کند.
alias مسیر location را جایگزین می‌کند.
```

اشتباه در `alias` یکی از دلیل‌های رایج 404 و حتی مشکل امنیتی است.

---

# هفته اول، روز ۳: ساخت اولین Reverse Proxy

حالا یک app ساده Node.js بساز.

```bash
mkdir ~/nginx-node-lab
cd ~/nginx-node-lab
npm init -y
npm install express
```

فایل `server.js`:

```js
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.json({
    message: "Hello from Node app",
    host: req.headers.host,
    forwardedFor: req.headers["x-forwarded-for"],
    realIp: req.headers["x-real-ip"],
  });
});

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

app.listen(3000, () => {
  console.log("App listening on port 3000");
});
```

اجرا:

```bash
node server.js
```

حالا Nginx config:

```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000;
    }
}
```

تست:

```bash
curl http://localhost
```

باید JSON از Node ببینی.

---

# حالا proxy headerها را درست کن

config بهتر:

```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000;

        proxy_http_version 1.1;

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

معنی headerها:

| Header              | معنی                            |
| ------------------- | ------------------------------- |
| `Host`              | دامنه اصلی request              |
| `X-Real-IP`         | IP مستقیم client از دید Nginx   |
| `X-Forwarded-For`   | زنجیره IPهای proxy شده          |
| `X-Forwarded-Proto` | http یا https بودن request اصلی |

این برای backend خیلی مهم است. مثلاً backend باید بداند request اصلی HTTPS بوده یا HTTP.

---

# نکته مهم درباره `proxy_pass`

این دو config فرق دارند:

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:3000;
}
```

و:

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:3000/;
}
```

فرق subtle ولی مهم است.

## بدون slash آخر

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:3000;
}
```

Request:

```text
/api/users
```

به upstream می‌رود:

```text
/api/users
```

## با slash آخر

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:3000/;
}
```

Request:

```text
/api/users
```

به upstream می‌رود:

```text
/users
```

یعنی prefix `/api/` حذف می‌شود.

این یکی از جاهایی است که خیلی developerها چند ساعت debug می‌کنند.

---

# هفته اول، روز ۴: route کردن چند سرویس

فرض کن دو سرویس داری:

```text
Frontend: localhost:3000
API:      localhost:4000
```

Nginx:

```nginx
server {
    listen 80;
    server_name _;

    location /api/ {
        proxy_pass http://127.0.0.1:4000/;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location / {
        proxy_pass http://127.0.0.1:3000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

معنی:

```text
/api/* → backend API
/*      → frontend
```

این ساختار در پروژه‌های واقعی زیاد استفاده می‌شود.

---

# هفته اول، روز ۵: errorهای رایج

## 502 Bad Gateway

معمولاً یعنی Nginx نتوانسته به upstream وصل شود.

دلایل رایج:

```text
- app خاموش است
- port اشتباه است
- app فقط روی IPv6 گوش می‌دهد
- firewall بسته است
- Docker networking اشتباه است
- upstream crash کرده
```

Debug:

```bash
sudo tail -f /var/log/nginx/error.log
```

تست upstream مستقیم:

```bash
curl http://127.0.0.1:3000
```

اگر این کار نمی‌کند، مشکل از Nginx نیست؛ مشکل از app است.

---

## 404 Not Found

دلایل رایج:

```text
- root اشتباه است
- try_files اشتباه است
- location match اشتباه است
- proxy_pass با slash اشتباه نوشته شده
- app route ندارد
```

Debug:

```bash
curl -i http://localhost/some-path
```

و بررسی access log:

```bash
sudo tail -f /var/log/nginx/access.log
```

---

## 403 Forbidden

دلایل رایج:

```text
- permission فایل/دایرکتوری اشتباه است
- index file وجود ندارد
- autoindex خاموش است
- user اجرای Nginx به فایل دسترسی ندارد
```

بررسی user:

```bash
ps aux | grep nginx
```

بررسی permission:

```bash
ls -la /var/www/nginx-lab
```

---

## 504 Gateway Timeout

یعنی upstream دیر جواب داده.

دلایل:

```text
- backend کند است
- query دیتابیس طولانی است
- proxy timeout کوتاه است
- upstream گیر کرده
```

configهای مرتبط:

```nginx
proxy_connect_timeout 5s;
proxy_send_timeout 30s;
proxy_read_timeout 30s;
```

فعلاً فقط معنی پایه را بدان:

| Directive               | معنی                                       |
| ----------------------- | ------------------------------------------ |
| `proxy_connect_timeout` | زمان مجاز برای وصل شدن به upstream         |
| `proxy_send_timeout`    | زمان مجاز برای ارسال request به upstream   |
| `proxy_read_timeout`    | زمان مجاز برای دریافت response از upstream |

---

# هفته دوم: server_name، location matching، logs و load balancing

## روز ۶: `server_name` و virtual hosts

Nginx می‌تواند چند سایت را روی یک سرور هندل کند.

```nginx
server {
    listen 80;
    server_name app.local;

    location / {
        return 200 "App Site\n";
    }
}

server {
    listen 80;
    server_name api.local;

    location / {
        return 200 "API Site\n";
    }
}
```

تست بدون DNS واقعی:

```bash
curl -H "Host: app.local" http://127.0.0.1
curl -H "Host: api.local" http://127.0.0.1
```

نتیجه:

```text
App Site
API Site
```

---

## default server

اگر Host match نشود، Nginx از default server استفاده می‌کند.

```nginx
server {
    listen 80 default_server;
    server_name _;

    return 444;
}
```

`444` یک status خاص Nginx است که connection را بدون response می‌بندد.

برای production معمولاً بهتر است default server رفتار مشخص داشته باشد.

مثلاً:

```nginx
server {
    listen 80 default_server;
    server_name _;

    return 404;
}
```

یا redirect به دامنه اصلی:

```nginx
server {
    listen 80 default_server;
    server_name _;

    return 301 https://example.com$request_uri;
}
```

---

# روز ۷: location matching

این بخش بسیار مهم است.

Nginx چند نوع `location` دارد:

```nginx
location / {}
location = /exact {}
location ^~ /static/ {}
location ~ \.php$ {}
location ~* \.(jpg|png)$ {}
```

## انواع location

| نوع                  | معنی                        |
| -------------------- | --------------------------- |
| `location /`         | prefix match عمومی          |
| `location = /path`   | exact match                 |
| `location ^~ /path/` | prefix match با اولویت بالا |
| `location ~ regex`   | regex case-sensitive        |
| `location ~* regex`  | regex case-insensitive      |

مثال:

```nginx
server {
    listen 80;
    server_name _;

    location = /health {
        return 200 "exact health\n";
    }

    location ^~ /static/ {
        return 200 "static prefix\n";
    }

    location ~ \.jpg$ {
        return 200 "jpg regex\n";
    }

    location / {
        return 200 "default location\n";
    }
}
```

تست:

```bash
curl http://localhost/health
curl http://localhost/static/app.js
curl http://localhost/image.jpg
curl http://localhost/anything
```

## قانون ذهنی ساده

برای فاز ۱ همین را حفظ کن:

```text
Exact match اولویت بالایی دارد.
بعد prefixهای خاص.
بعد regexها.
در نهایت location /.
```

بعداً می‌توانی دقیق‌تر الگوریتم matching را بخوانی.

---

# روز ۸: access log و error log

## access log

هر request موفق یا ناموفق معمولاً وارد access log می‌شود.

```bash
sudo tail -f /var/log/nginx/access.log
```

نمونه:

```text
127.0.0.1 - - [08/Jun/2026:12:10:00 +0000] "GET / HTTP/1.1" 200 123 "-" "curl/8.0"
```

معنی:

```text
client IP
time
method
path
protocol
status
response size
referer
user agent
```

## error log

برای خطاهای داخلی، upstream failure، permission issue و غیره:

```bash
sudo tail -f /var/log/nginx/error.log
```

---

## تعریف log format سفارشی

داخل `http` context:

```nginx
log_format main_ext '$remote_addr - $remote_user [$time_local] '
                    '"$request" $status $body_bytes_sent '
                    '"$http_referer" "$http_user_agent" '
                    'rt=$request_time '
                    'uct=$upstream_connect_time '
                    'uht=$upstream_header_time '
                    'urt=$upstream_response_time '
                    'ua="$upstream_addr"';

access_log /var/log/nginx/access.log main_ext;
```

این‌ها خیلی مهم‌اند:

| Variable                  | معنی                              |
| ------------------------- | --------------------------------- |
| `$request_time`           | کل زمان request از دید Nginx      |
| `$upstream_connect_time`  | زمان اتصال به upstream            |
| `$upstream_header_time`   | زمان تا دریافت header از upstream |
| `$upstream_response_time` | زمان دریافت response از upstream  |
| `$upstream_addr`          | آدرس upstream پاسخ‌دهنده          |

برای debug production، این‌ها طلا هستند.

---

# روز ۹: basic load balancing

سه app ساده اجرا کن.

`server.js` را طوری تغییر بده که port و instance را نشان دهد:

```js
const express = require("express");

const app = express();
const port = process.env.PORT || 3000;
const instance = process.env.INSTANCE || "app";

app.get("/", (req, res) => {
  res.json({
    message: "Hello",
    instance,
    port,
  });
});

app.listen(port, () => {
  console.log(`${instance} listening on port ${port}`);
});
```

اجرا:

```bash
PORT=3001 INSTANCE=app-1 node server.js
PORT=3002 INSTANCE=app-2 node server.js
PORT=3003 INSTANCE=app-3 node server.js
```

Nginx config:

```nginx
upstream node_apps {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
    server 127.0.0.1:3003;
}

server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://node_apps;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

تست:

```bash
for i in {1..10}; do curl -s http://localhost; echo; done
```

باید ببینی درخواست‌ها بین appها پخش می‌شوند.

---

## الگوریتم‌های ساده load balancing

### Round-robin

پیش‌فرض Nginx است:

```nginx
upstream node_apps {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
```

### Weighted

```nginx
upstream node_apps {
    server 127.0.0.1:3001 weight=3;
    server 127.0.0.1:3002 weight=1;
}
```

یعنی app اول تقریباً سهم بیشتری از requestها می‌گیرد.

### least_conn

```nginx
upstream node_apps {
    least_conn;

    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
```

درخواست جدید را به backendی می‌دهد که connection فعال کمتری دارد.

---

# روز ۱۰: basic health/failure behavior

در نسخه open source، health check فعال پیشرفته مثل NGINX Plus نداری، ولی می‌توانی رفتار failure را با پارامترهای upstream کنترل کنی.

مثال:

```nginx
upstream node_apps {
    server 127.0.0.1:3001 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:3002 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:3003 max_fails=3 fail_timeout=10s;
}
```

معنی ساده:

```text
اگر یک upstream چند بار fail شود،
برای مدتی کمتر به آن request داده می‌شود.
```

تمرین:

1. سه app را اجرا کن.
2. request loop بزن.
3. یکی از appها را kill کن.
4. log را ببین.
5. ببین Nginx چطور رفتار می‌کند.

```bash
sudo tail -f /var/log/nginx/error.log
```

---

# هفته سوم: HTTPS، WebSocket، config hygiene و پروژه نهایی

## روز ۱۱: HTTPS پایه

برای local lab می‌توانی self-signed certificate بسازی.

```bash
sudo mkdir -p /etc/nginx/ssl
sudo openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout /etc/nginx/ssl/nginx-lab.key \
  -out /etc/nginx/ssl/nginx-lab.crt
```

Nginx:

```nginx
server {
    listen 80;
    server_name _;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name _;

    ssl_certificate /etc/nginx/ssl/nginx-lab.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx-lab.key;

    location / {
        proxy_pass http://127.0.0.1:3000;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

تست:

```bash
curl -k https://localhost
```

`-k` یعنی certificate self-signed را قبول کن.

برای production واقعی بعداً باید Let’s Encrypt و Certbot یا روش‌های مشابه را یاد بگیری، ولی برای فاز ۱ self-signed کافی است.

---

# روز ۱۲: WebSocket proxy

برای WebSocket باید headerهای upgrade را درست pass کنی.

config پایه:

```nginx
server {
    listen 80;
    server_name _;

    location /socket/ {
        proxy_pass http://127.0.0.1:3000;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

نسخه بهتر با `map` داخل `http` context:

```nginx
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}
```

بعد در server:

```nginx
location /socket/ {
    proxy_pass http://127.0.0.1:3000;

    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;

    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

---

# روز ۱۳: ساختار تمیز config

به‌جای اینکه همه‌چیز را در یک فایل شلوغ بریزی، common config بساز.

مثلاً:

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
```

بعد استفاده:

```nginx
location / {
    proxy_pass http://127.0.0.1:3000;
    include snippets/proxy-headers.conf;
}
```

برای SSL هم:

```text
/etc/nginx/snippets/ssl-lab.conf
```

```nginx
ssl_certificate /etc/nginx/ssl/nginx-lab.crt;
ssl_certificate_key /etc/nginx/ssl/nginx-lab.key;
```

استفاده:

```nginx
server {
    listen 443 ssl;
    server_name _;

    include snippets/ssl-lab.conf;

    location / {
        proxy_pass http://127.0.0.1:3000;
        include snippets/proxy-headers.conf;
    }
}
```

این عادت از همین اول مهم است. config کثیف در production دردسر جدی می‌شود.

---

# روز ۱۴: پروژه نهایی فاز ۱

در پایان فاز ۱ یک lab کامل بساز.

## معماری پروژه

```text
Browser
  ↓
Nginx :80 / :443
  ↓
Route decision
  ├── /              → Frontend app :3000
  ├── /api/          → API app :4000
  ├── /static/       → Static files from disk
  ├── /uploads/      → Uploaded files from disk
  └── /health        → Nginx direct response
```

## config پیشنهادی پروژه نهایی

```nginx
upstream frontend_app {
    server 127.0.0.1:3000;
}

upstream api_app {
    server 127.0.0.1:4000;
}

server {
    listen 80;
    server_name _;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name _;

    ssl_certificate /etc/nginx/ssl/nginx-lab.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx-lab.key;

    access_log /var/log/nginx/nginx-lab.access.log;
    error_log /var/log/nginx/nginx-lab.error.log;

    location = /health {
        access_log off;
        return 200 "ok\n";
    }

    location /static/ {
        root /var/www/nginx-lab;
        expires 7d;
        add_header Cache-Control "public";
    }

    location /uploads/ {
        alias /var/www/uploads/;
        try_files $uri =404;
    }

    location /api/ {
        proxy_pass http://api_app/;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 5s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
    }

    location / {
        proxy_pass http://frontend_app;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

# checklist فاز ۱

در پایان فاز ۱ باید بتوانی این‌ها را انجام بدهی:

```text
[ ] نصب Nginx
[ ] start/stop/reload کردن سرویس
[ ] تست config با nginx -t
[ ] دیدن config کامل با nginx -T
[ ] ساخت server block
[ ] تعریف server_name
[ ] static file serving
[ ] تفاوت root و alias
[ ] نوشتن location ساده
[ ] فهم location matching پایه
[ ] reverse proxy به app
[ ] تنظیم proxy headers
[ ] فهم proxy_pass با slash و بدون slash
[ ] route کردن /api و /
[ ] basic upstream
[ ] basic load balancing
[ ] خواندن access.log
[ ] خواندن error.log
[ ] debug کردن 502
[ ] debug کردن 403
[ ] debug کردن 404
[ ] debug کردن 504
[ ] ساخت HTTPS self-signed
[ ] redirect HTTP به HTTPS
[ ] WebSocket proxy
[ ] ساخت snippet برای config مشترک
[ ] ساخت lab نهایی
```

---

# سؤال‌هایی که باید بتوانی جواب بدهی

اگر واقعاً فاز ۱ را خوب خوانده باشی، باید بتوانی به این‌ها جواب بدهی:

## مفهومی

* Nginx چه فرقی با application server دارد؟
* Reverse proxy یعنی چه؟
* چرا backend را مستقیم روی اینترنت expose نمی‌کنیم؟
* `server` block چیست؟
* `location` چیست؟
* `upstream` چیست؟
* تفاوت `root` و `alias` چیست؟
* تفاوت reload و restart چیست؟
* چرا باید قبل reload کردن `nginx -t` بگیریم؟

## عملی

* چطور یک app روی port 3000 را پشت Nginx بگذارم؟
* چطور `/api/` را به backend و `/` را به frontend بفرستم؟
* چطور چند backend را load balance کنم؟
* چطور بفهمم 502 از Nginx است یا app؟
* چطور بفهمم request به کدام upstream رفته؟
* چطور static file را cache کنم؟
* چطور HTTP را به HTTPS redirect کنم؟

## خطاها

* 502 یعنی چه؟
* 403 یعنی چه؟
* 404 ممکن است از Nginx باشد یا app؟
* 504 یعنی چه؟
* اگر `nginx -t` fail شد چه کار کنم؟
* اگر reload کردم و سایت بالا نیامد از کجا شروع کنم؟

---

# برنامه روزانه پیشنهادی فاز ۱

## روز ۱

* نصب Nginx
* شناخت مسیرهای اصلی
* `systemctl`
* `nginx -t`
* `nginx -T`

## روز ۲

* ساخت static site
* `root`
* `try_files`
* `index`
* access log

## روز ۳

* `location`
* `root` vs `alias`
* cache header برای static files

## روز ۴

* ساخت Node.js app ساده
* reverse proxy
* `proxy_pass`

## روز ۵

* proxy headers
* `X-Forwarded-For`
* `X-Real-IP`
* `X-Forwarded-Proto`

## روز ۶

* route کردن چند سرویس
* `/api/`
* `/`
* تفاوت slash در `proxy_pass`

## روز ۷

* error handling
* debug 502، 403، 404، 504

## روز ۸

* `server_name`
* virtual hosts
* default server

## روز ۹

* location matching
* exact, prefix, regex

## روز ۱۰

* custom log format
* upstream timing variables

## روز ۱۱

* upstream
* basic load balancing
* round-robin
* weight
* least_conn

## روز ۱۲

* failure behavior
* kill کردن upstream
* بررسی error log

## روز ۱۳

* HTTPS self-signed
* redirect HTTP به HTTPS

## روز ۱۴

* WebSocket proxy
* snippetها
* config hygiene

## روز ۱۵

* ساخت پروژه نهایی
* مستندسازی config
* نوشتن گزارش کوتاه

---

# تمرین نهایی فاز ۱

یک فایل Markdown برای خودت بساز و به این سؤال‌ها جواب بده:

```md
# Nginx Phase 1 Report

## Architecture

Describe your lab architecture.

## Config Files

List all config files you created.

## Routes

| Path | Destination |
|---|---|
| / | Frontend |
| /api/ | API |
| /static/ | Static files |
| /uploads/ | Uploaded files |
| /health | Nginx direct response |

## Errors I Tested

### 502

Cause:
Fix:

### 403

Cause:
Fix:

### 404

Cause:
Fix:

### 504

Cause:
Fix:

## Load Balancing Result

Describe how requests were distributed.

## HTTPS Result

Describe your HTTP to HTTPS redirect.

## Lessons Learned

Write 10 things you learned.
```

این گزارش خیلی مهم است. چون فقط «خواندن» کافی نیست. باید بتوانی چیزی که فهمیدی را توضیح بدهی. وقتی بتوانی کانفیگت را برای یک نفر دیگر توضیح بدهی، تازه واقعاً یاد گرفته‌ای.
