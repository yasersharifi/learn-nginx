# Phase 1 - Basic
___

### Nginx
- Cache
- Load Balancer
- Reverse Proxy
- Web server
- TCP/UDP proxy

___

### Read
- Official Nginx Beginner’s Guide
- ساختار فایل کانفیگ
- server
- location
- upstream
- proxy_pass
- static file serving
- logging
- reload / restart / graceful shutdown
- تفاوت mainline و stable
___

### Practice
- یک Next.js یا Node.js app را پشت Nginx بگذار.
- HTTP را به HTTPS تبدیل کن.
- WebSocket proxy کن.
- چند upstream تعریف کن.
- access log و error log را تحلیل کن.
- rate limit ساده بگذار.

___

# Phase 2 - Production Operation

- reverse proxy
- load balancing
- health check concept
- SSL/TLS termination
- HTTP/2 و HTTP/3
- gzip / brotli concept
- caching
- buffering
- timeoutها
- upload limits
- rate limiting
- connection limiting
- observability
- structured logs
- blue/green و canary در سطح proxy

___

### Practice

یک mini production lab بساز:

```shell
Client
  ↓
Nginx
  ↓
App 1 / App 2 / App 3
  ↓
Redis / DB
```

بعد این‌ها را تست کن:

- یکی از appها را kill کن.
- latency مصنوعی اضافه کن.
- request burst بفرست.
- timeoutها را بد تنظیم کن و نتیجه را ببین.
- cache را روشن کن و hit/miss را اندازه بگیر.
- log format سفارشی بساز.
- rate limiting را تست کن.
