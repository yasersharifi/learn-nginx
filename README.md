# مسیر مطالعه Nginx در سطح دکترای کامپیوتر

اگر می‌خواهی Nginx را در سطح بسیار عمیق و نزدیک به نگاه یک دکترای کامپیوتر بخوانی، نباید آن را فقط به‌عنوان یک وب‌سرور یا ابزار reverse proxy ببینی. باید Nginx را به‌عنوان یک نمونه واقعی از سیستم‌های high-performance، event-driven، network server و production infrastructure مطالعه کنی.

مسیر درست مطالعه شامل سه لایه اصلی است:

1. استفاده عملی و Production Configuration
2. معماری داخلی، سورس‌کد و module system
3. مفاهیم علمی پشت آن: سیستم‌عامل، شبکه، concurrency، performance، caching، security و distributed systems

---

## مدت زمان پیشنهادی

| سطح هدف                       | مدت زمان واقع‌بینانه |
| ----------------------------- | -------------------: |
| استفاده حرفه‌ای در پروژه‌ها   |           ۱ تا ۲ ماه |
| سطح Production / DevOps قوی   |           ۳ تا ۶ ماه |
| درک عمیق معماری و Performance |          ۶ تا ۱۲ ماه |
| سطح پژوهشی / PhD-like         |         ۱۲ تا ۱۸ ماه |

اگر روزی ۱ تا ۲ ساعت مطالعه و تمرین داشته باشی، مسیر جدی حدود **۹ تا ۱۲ ماه** زمان می‌برد. اگر فقط چند ساعت در هفته وقت بگذاری، این مسیر احتمالاً به **۱۸ ماه** نزدیک می‌شود.

---

# فاز ۱: پایه عملی Nginx

**مدت زمان:** ۲ تا ۳ هفته

در این فاز باید بفهمی Nginx دقیقاً چه کارهایی انجام می‌دهد:

* Web Server
* Reverse Proxy
* Load Balancer
* Static File Server
* HTTP Cache
* SSL/TLS Termination
* TCP/UDP Proxy
* Gateway جلوی application serverها

## موضوعات اصلی

* ساختار فایل `nginx.conf`
* contextها:

  * `main`
  * `events`
  * `http`
  * `server`
  * `location`
  * `upstream`
* directiveها
* `proxy_pass`
* static file serving
* access log و error log
* reload، restart و graceful shutdown
* تفاوت stable و mainline
* basic HTTPS setup
* WebSocket proxying

## تمرین‌های عملی

* یک Node.js یا Next.js app را پشت Nginx قرار بده.
* HTTP را به HTTPS redirect کن.
* یک static directory سرو کن.
* چند upstream تعریف کن.
* load balancing ساده انجام بده.
* WebSocket را از طریق Nginx proxy کن.
* access log و error log را بررسی کن.
* یک rate limit ساده تعریف کن.

## خروجی این فاز

بعد از این فاز باید بتوانی یک اپلیکیشن واقعی را پشت Nginx deploy کنی و basic production config بنویسی.

---

# فاز ۲: Production Operations

**مدت زمان:** ۴ تا ۶ هفته

اینجا باید از سطح «بلدم کانفیگ کنم» به سطح «می‌توانم سیستم پایدار production بسازم» برسی.

## موضوعات اصلی

* Reverse Proxy
* Load Balancing
* Health Check concept
* SSL/TLS Termination
* HTTP/2
* HTTP/3
* gzip و brotli concept
* caching
* buffering
* timeoutها
* upload limits
* rate limiting
* connection limiting
* structured logging
* monitoring
* zero-downtime reload
* blue/green و canary در سطح proxy

## Moduleهای مهم

* `ngx_http_proxy_module`
* `ngx_http_upstream_module`
* `ngx_http_ssl_module`
* `ngx_http_gzip_module`
* `ngx_http_limit_req_module`
* `ngx_http_limit_conn_module`
* `ngx_http_realip_module`
* `ngx_http_v2_module`
* `ngx_http_v3_module`
* `ngx_stream_core_module`

## تمرین Production Lab

یک lab شبیه این بساز:

```text
Client
  ↓
Nginx
  ↓
App 1 / App 2 / App 3
  ↓
Redis / Database
```

بعد این سناریوها را تست کن:

* یکی از appها را خاموش کن.
* latency مصنوعی به upstream اضافه کن.
* request burst بفرست.
* timeoutها را اشتباه تنظیم کن و نتیجه را ببین.
* cache را روشن کن و hit/miss را اندازه بگیر.
* rate limiting را تست کن.
* log format سفارشی بساز.
* errorهای 502، 503 و 504 را عمداً تولید کن.

## خروجی این فاز

باید بتوانی یک Nginx config production-grade بسازی و درباره tradeoffهای آن توضیح بدهی.

---

# فاز ۳: شبکه و سیستم‌عامل

**مدت زمان:** ۲ تا ۳ ماه

بدون درک سیستم‌عامل و شبکه، Nginx را عمیق نمی‌فهمی. Nginx روی مفاهیم Linux networking، socket، event loop و non-blocking I/O ساخته شده است.

## Networking

موضوعاتی که باید بخوانی:

* TCP handshake
* TCP keep-alive
* congestion control
* socket backlog
* SYN queue
* accept queue
* TLS handshake
* HTTP/1.1
* HTTP/2 multiplexing
* HTTP/3 و QUIC
* DNS
* proxy headers
* `X-Forwarded-For`
* `X-Real-IP`
* PROXY protocol
* connection reuse
* head-of-line blocking

## Linux / OS

موضوعاتی که باید بخوانی:

* process model
* file descriptors
* sockets
* blocking vs non-blocking I/O
* `select`
* `poll`
* `epoll`
* event loop
* zero-copy concept
* `sendfile`
* memory allocation
* page cache
* kernel tuning
* `ulimit`
* systemd
* cgroups
* container networking

## ابزارهای مهم

* `ss`
* `netstat`
* `lsof`
* `strace`
* `perf`
* `tcpdump`
* `wireshark`
* `wrk`
* `k6`
* `ab`
* `hey`

## تمرین‌ها

* تعداد connectionها را بالا ببر.
* file descriptor limit را بشکن.
* backlog را تغییر بده و اثر آن را ببین.
* با `tcpdump` ترافیک HTTP و TLS را بررسی کن.
* با `strace` system callهای Nginx را ببین.
* با `perf` bottleneck را پیدا کن.
* با `wrk` یا `k6` benchmark بگیر.

## خروجی این فاز

باید بتوانی توضیح بدهی چرا Nginx با workerهای کم می‌تواند connectionهای زیاد را مدیریت کند.

---

# فاز ۴: معماری داخلی Nginx

**مدت زمان:** ۲ تا ۳ ماه

در این فاز وارد هسته واقعی Nginx می‌شوی.

## موضوعات اصلی

* master process
* worker process
* event loop
* accept mutex
* request lifecycle
* phase handlerها
* memory pool
* module system
* upstream mechanism
* config parsing
* logging internals
* shared memory zones
* cache manager
* cache loader
* dynamic modules

## مسیر پیشنهادی خواندن سورس‌کد

```text
src/core/
src/event/
src/http/
src/http/modules/
src/http/ngx_http_request.c
src/http/ngx_http_core_module.c
src/http/ngx_http_upstream.c
src/os/unix/
```

## تمرین‌ها

* Nginx را از سورس build کن.
* debug log را فعال کن.
* یک worker process را با `gdb` یا `lldb` inspect کن.
* request lifecycle را با debug log دنبال کن.
* یک module ساده بنویس که header سفارشی اضافه کند.
* یک handler ساده بنویس که response ثابت برگرداند.
* مسیر اجرای یک request را از accept تا response trace کن.

## خروجی این فاز

باید بتوانی توضیح بدهی یک request در Nginx از لحظه accept شدن تا ارسال response چه مسیری را طی می‌کند.

---

# فاز ۵: Performance Engineering

**مدت زمان:** ۲ ماه

در این مرحله باید یاد بگیری چرا یک کانفیگ سریع یا کند است.

## موضوعات اصلی

* latency vs throughput
* p50, p95, p99, p999
* tail latency
* queueing theory
* Little’s Law
* head-of-line blocking
* buffering tradeoff
* cache hit ratio
* connection reuse
* TLS cost
* upstream saturation
* kernel/network tuning
* NUMA basics
* CPU affinity
* worker count
* open file cache
* `sendfile`
* `TCP_NODELAY`
* `TCP_CORK`

## Benchmark Matrix پیشنهادی

| سناریو              | متریک اصلی          |
| ------------------- | ------------------- |
| static file serving | throughput          |
| reverse proxy       | p95 latency         |
| TLS on/off          | CPU cost            |
| cache on/off        | hit ratio           |
| gzip on/off         | CPU vs bandwidth    |
| upstream slow       | queue behavior      |
| rate limit          | rejection behavior  |
| HTTP/1.1 vs HTTP/2  | multiplexing impact |
| HTTP/2 vs HTTP/3    | latency impact      |

## ابزارها

* `wrk`
* `k6`
* `vegeta`
* `perf`
* FlameGraph
* eBPF
* `bpftrace`
* Prometheus
* Grafana
* OpenTelemetry

## تمرین‌ها

* static file serving را benchmark کن.
* reverse proxy را با upstream سریع و کند تست کن.
* cache hit و miss را جداگانه اندازه بگیر.
* اثر gzip را روی CPU و bandwidth بررسی کن.
* TLS termination را با HTTP ساده مقایسه کن.
* p99 latency را زیر بار بالا بررسی کن.
* با flamegraph bottleneck را پیدا کن.

## خروجی این فاز

باید بتوانی یک benchmark report واقعی بنویسی و با داده توضیح بدهی کدام کانفیگ بهتر است.

---

# فاز ۶: Security

**مدت زمان:** ۴ تا ۶ هفته

Nginx معمولاً در edge سیستم قرار می‌گیرد. پس اشتباه امنیتی در این لایه می‌تواند کل سیستم را درگیر کند.

## موضوعات اصلی

* TLS configuration
* certificate chain
* OCSP stapling
* HSTS
* secure headers
* request smuggling
* header spoofing
* real IP handling
* path traversal
* upload limits
* body size limits
* rate limiting
* WAF concept
* mTLS
* `auth_request`
* JWT validation
* CORS
* SSRF risk در reverse proxy
* open proxy misconfiguration

## تمرین‌ها

* TLS config امن بساز.
* HSTS اضافه کن.
* secure headers تعریف کن.
* `X-Forwarded-For` جعلی بفرست و رفتار app را بررسی کن.
* rate limit bypass را تست کن.
* request body بزرگ بفرست.
* slowloris-style behavior را بررسی کن.
* مسیرهای static را برای path traversal تست کن.
* CORS misconfiguration را بررسی کن.

## خروجی این فاز

باید بتوانی Nginx را به‌عنوان edge proxy امن کانفیگ کنی و ریسک‌های اصلی آن را توضیح بدهی.

---

# فاز ۷: سطح پژوهشی / PhD-like

**مدت زمان:** ۳ تا ۶ ماه

اینجا دیگر فقط Nginx نمی‌خوانی. Nginx را به‌عنوان نمونه‌ای از high-performance network serverها و distributed infrastructure مطالعه می‌کنی.

## موضوعات پژوهشی

* event-driven architecture
* async I/O
* kernel bypass
* DPDK concept
* io_uring concept
* QUIC performance
* HTTP/3 tradeoffs
* adaptive load balancing
* cache eviction algorithms
* distributed caching
* admission control
* overload control
* autoscaling feedback loops
* tail latency reduction
* formal modeling of proxy behavior

## پروژه‌های پژوهشی پیشنهادی

یکی از این پروژه‌ها را انتخاب کن:

1. مقایسه Nginx، Envoy و HAProxy از نظر latency و architecture
2. طراحی adaptive load balancer module برای Nginx
3. تحلیل cache eviction در Nginx با workload واقعی
4. بررسی اثر HTTP/2 و HTTP/3 روی tail latency
5. ساخت observability layer برای Nginx با eBPF
6. نوشتن custom module برای admission control
7. طراحی benchmark suite برای reverse proxyها
8. بررسی failure modeهای Nginx در معماری microservices

## خروجی این فاز

باید یک پروژه قابل انتشار داشته باشی؛ مثلاً:

* GitHub repository
* benchmark report
* technical blog series
* conference-style writeup
* custom Nginx module
* observability dashboard

---

# منابع پیشنهادی

## منابع اصلی Nginx

1. Official Nginx Documentation
2. NGINX Admin Guide
3. NGINX Development Guide
4. Official Nginx Source Code
5. NGINX Cookbook
6. Nginx High Performance
7. Mastering NGINX

## منابع شبکه

1. Computer Networking: A Top-Down Approach
2. UNIX Network Programming — W. Richard Stevens
3. High Performance Browser Networking
4. TCP/IP Illustrated

## منابع سیستم‌عامل

1. The Linux Programming Interface — Michael Kerrisk
2. Operating Systems: Three Easy Pieces
3. Computer Systems: A Programmer’s Perspective
4. Systems Performance — Brendan Gregg

## منابع Performance

1. Systems Performance — Brendan Gregg
2. BPF Performance Tools — Brendan Gregg
3. Site Reliability Engineering — Google
4. Designing Data-Intensive Applications

## منابع امنیت

1. OWASP Cheat Sheets
2. Mozilla TLS Configuration Guide
3. Web Security Academy
4. NGINX security advisories
5. RFCهای مرتبط با HTTP، TLS و QUIC

---

# برنامه ۱۲ ماهه پیشنهادی

## ماه ۱: Nginx عملی

* beginner guide
* basic config
* reverse proxy
* static file serving
* HTTPS
* logs
* upstream
* basic load balancing

**خروجی:** deploy یک اپ واقعی پشت Nginx.

---

## ماه ۲: Production Proxy

* proxy headers
* buffering
* timeoutها
* WebSocket
* rate limit
* gzip
* upload limit
* logging

**خروجی:** config قابل استفاده در production.

---

## ماه ۳: Caching و Failure Scenarios

* cache
* cache key
* cache purge concept
* stale cache
* upstream failure
* 502/503/504
* retry behavior
* health check concept

**خروجی:** lab با failure simulation.

---

## ماه ۴ و ۵: Linux Networking

* TCP
* TLS
* sockets
* epoll
* file descriptors
* backlog
* kernel tuning
* benchmarking

**خروجی:** توانایی debug کردن مشکل performance با ابزار، نه حدس.

---

## ماه ۶ و ۷: سورس‌کد و معماری داخلی

* build from source
* debug log
* master/worker
* event loop
* request phases
* module system
* memory pool

**خروجی:** توضیح request lifecycle و نوشتن module ساده.

---

## ماه ۸ و ۹: Performance Engineering

* benchmark design
* p95/p99
* flamegraph
* cache experiments
* TLS cost
* upstream saturation
* overload behavior

**خروجی:** benchmark report واقعی.

---

## ماه ۱۰: Security

* TLS hardening
* secure headers
* real IP
* rate limit
* request smuggling basics
* mTLS
* auth_request

**خروجی:** secure edge proxy config.

---

## ماه ۱۱ و ۱۲: پروژه پژوهشی

یکی از این پروژه‌ها را انجام بده:

* مقایسه Nginx / Envoy / HAProxy
* custom module
* eBPF observability
* HTTP/3 latency analysis
* cache eviction analysis
* adaptive load balancing

**خروجی:** پروژه قابل انتشار یا مقاله فنی.

---

# روش مطالعه پیشنهادی

روش درست مطالعه Nginx این است:

```text
Read → Configure → Break → Measure → Debug → Explain → Modify
```

روش اشتباه این است:

```text
Read Docs → Copy Config → Done
```

برای هر موضوع این چرخه را اجرا کن:

1. مستندات رسمی را بخوان.
2. یک config کوچک بساز.
3. عمداً خرابش کن.
4. فشار تست بگیر.
5. log و metric ببین.
6. دلیل رفتار را بنویس.
7. config را بهتر کن.
8. سورس‌کد مربوطه را پیدا کن.

---

# معیار سنجش یادگیری عمیق

وقتی بتوانی به سؤال‌های زیر جواب بدهی، یعنی مسیرت درست است:

* چرا Nginx با workerهای کم می‌تواند connection زیاد هندل کند؟
* فرق buffering روشن و خاموش چیست؟
* `proxy_read_timeout` دقیقاً چه چیزی را کنترل می‌کند؟
* چرا `X-Forwarded-For` می‌تواند خطرناک باشد؟
* چه زمانی cache باعث کندتر شدن سیستم می‌شود؟
* چرا p99 latency ممکن است بد شود ولی میانگین خوب بماند؟
* تفاوت HTTP/2 و HTTP/3 برای reverse proxy چیست؟
* اگر upstream کند شود، Nginx چه رفتاری نشان می‌دهد؟
* چرا `worker_connections` دقیقاً برابر تعداد request همزمان نیست؟
* یک request از accept تا response چه مسیر داخلی‌ای طی می‌کند؟
* کدام moduleها در request processing phase دخالت دارند؟
* چطور یک Nginx module ساده می‌نویسی؟
* چطور با `perf` یا `strace` bottleneck را پیدا می‌کنی؟
* چطور می‌فهمی مشکل از Nginx است یا upstream؟
* چه زمانی افزایش worker process کمکی نمی‌کند؟
* چه زمانی cache layer خطرناک می‌شود؟
* چطور overload را قبل از crash کنترل می‌کنی؟

---

# توصیه نهایی

برای شروع، از سورس‌کد شروع نکن. ابتدا Nginx را در پروژه واقعی استفاده کن.

مسیر پیشنهادی:

```text
ماه ۱: Nginx عملی
ماه ۲: reverse proxy / load balancing / TLS / logs
ماه ۳: caching / rate limit / production failure scenarios
ماه ۴-۵: Linux networking و performance
ماه ۶-۷: سورس‌کد و module system
ماه ۸-۹: benchmark و observability
ماه ۱۰-۱۲: پروژه پژوهشی یا مقایسه Nginx/Envoy/HAProxy
```

اگر این مسیر را جدی بروی، بعد از ۶ ماه از اکثر developerهایی که فقط Nginx config کپی می‌کنند جلوتر هستی. بعد از ۱۲ ماه می‌توانی درباره Nginx مثل یک engineer سطح سیستم صحبت کنی، نه فقط کسی که چند directive حفظ کرده.
