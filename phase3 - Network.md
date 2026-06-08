# فاز ۳: شبکه و سیستم‌عامل برای فهم عمیق Nginx

در فاز ۱ یاد گرفتی Nginx را نصب و کانفیگ کنی.
در فاز ۲ یاد گرفتی Nginx را production-like استفاده کنی: reverse proxy، timeout، buffering، caching، rate limit، HTTPS، logs و failure handling.

اما اگر می‌خواهی Nginx را عمیق بفهمی، باید وارد لایه زیرین شوی:

* Linux
* TCP/IP
* sockets
* process model
* file descriptors
* non-blocking I/O
* event loop
* epoll
* TLS
* HTTP/1.1
* HTTP/2
* HTTP/3 و QUIC
* kernel limits
* benchmarking
* tracing و debugging

Nginx بدون این مفاهیم فقط مجموعه‌ای از directiveهاست. با این مفاهیم، Nginx تبدیل می‌شود به یک نمونه واقعی از high-performance network server.

---

# هدف فاز ۳

بعد از فاز ۳ باید بتوانی:

* توضیح بدهی چرا Nginx با workerهای کم connection زیاد را مدیریت می‌کند.
* فرق process، thread، connection و request را بفهمی.
* TCP connection lifecycle را توضیح بدهی.
* بفهمی `worker_connections` دقیقاً چه چیزی را محدود می‌کند.
* با ابزارهای Linux مثل `ss`, `lsof`, `strace`, `tcpdump`, `perf` و `wrk` کار کنی.
* بفهمی `epoll` چرا برای Nginx مهم است.
* تفاوت blocking و non-blocking I/O را بفهمی.
* مشکل‌های performance را با داده debug کنی، نه با حدس.
* بفهمی چرا timeout، keepalive، backlog، file descriptor و kernel tuning روی Nginx اثر دارند.
* بفهمی HTTP/1.1، HTTP/2 و HTTP/3 چه تفاوتی برای reverse proxy دارند.

مدت پیشنهادی: **۲ تا ۳ ماه**

اگر روزی ۱ تا ۲ ساعت وقت بگذاری، این فاز حدود **۸۰ تا ۱۲۰ ساعت** کار جدی می‌خواهد.

---

# پیش‌نیازهای فاز ۳

قبل از ورود به این فاز باید این‌ها را بلد باشی:

```text id="dyul91"
[ ] نصب و اجرای Nginx
[ ] server block
[ ] location
[ ] reverse proxy
[ ] upstream
[ ] proxy headers
[ ] timeoutها
[ ] buffering
[ ] caching پایه
[ ] rate limiting
[ ] access log و error log
[ ] basic load balancing
[ ] HTTPS پایه
[ ] debug خطاهای 502، 503، 504
```

اگر هنوز این موارد برایت مبهم‌اند، فاز ۱ و ۲ را کامل‌تر تمرین کن. فاز ۳ تئوری‌تر است، ولی باید روی lab واقعی اجرا شود.

---

# تصویر ذهنی فاز ۳

Nginx در ظاهر یک config file دارد، اما در عمل روی این لایه‌ها سوار است:

```text id="fy4a31"
HTTP / HTTPS
  ↓
TLS
  ↓
TCP
  ↓
Socket API
  ↓
Linux Kernel
  ↓
NIC / Network
```

از سمت process هم:

```text id="y3g83o"
Nginx Master Process
  ↓
Worker Processes
  ↓
Event Loop
  ↓
epoll
  ↓
Non-blocking sockets
  ↓
Client and upstream connections
```

فاز ۳ یعنی فهمیدن این دو تصویر.

---

# ساختار کلی فاز ۳

این فاز را به ۸ بخش تقسیم می‌کنیم:

```text id="07x0fb"
هفته ۱: مدل process و worker در Linux و Nginx
هفته ۲: file descriptor، socket و connection
هفته ۳: TCP/IP و connection lifecycle
هفته ۴: HTTP/1.1، keepalive و reverse proxy behavior
هفته ۵: non-blocking I/O، event loop و epoll
هفته ۶: TLS، HTTP/2 و HTTP/3 concept
هفته ۷: Linux limits، kernel tuning و observability
هفته ۸ تا ۱۲: benchmarking، tracing، debugging و پروژه نهایی
```

---

# هفته ۱: Process Model و Workerها

## هدف هفته ۱

در پایان این هفته باید بتوانی توضیح بدهی:

* process چیست؟
* thread چیست؟
* master process در Nginx چه می‌کند؟
* worker process در Nginx چه می‌کند؟
* چرا Nginx معمولاً process-based است، نه thread-per-request؟
* چرا `worker_processes auto` معمولاً انتخاب خوبی است؟
* چرا زیاد کردن worker همیشه performance را بهتر نمی‌کند؟

---

## روز ۱: Process چیست؟

در Linux، هر برنامه در حال اجرا معمولاً یک یا چند process دارد.

برای دیدن processهای Nginx:

```bash id="r1arwz"
ps aux | grep nginx
```

خروجی معمولاً چیزی شبیه این است:

```text id="ojdhng"
root      1001  0.0  nginx: master process /usr/sbin/nginx
www-data  1002  0.1  nginx: worker process
www-data  1003  0.1  nginx: worker process
```

معنی:

```text id="oacy2j"
master process:
- config را می‌خواند
- workerها را مدیریت می‌کند
- reload را کنترل می‌کند
- signalها را مدیریت می‌کند

worker process:
- connectionها را accept می‌کند
- requestها را پردازش می‌کند
- response می‌فرستد
- با upstream صحبت می‌کند
```

---

## تفاوت master و worker

| بخش           | کار اصلی                        |
| ------------- | ------------------------------- |
| master        | مدیریت lifecycle                |
| worker        | انجام کار واقعی network/request |
| cache manager | مدیریت cache                    |
| cache loader  | بارگذاری metadata cache         |

برای مشاهده process tree:

```bash id="9ni77f"
pstree -p | grep nginx
```

یا:

```bash id="oz9kak"
ps -ef --forest | grep nginx
```

---

## روز ۲: worker_processes

Directive مهم:

```nginx id="42v62s"
worker_processes auto;
```

یا:

```nginx id="ivnroe"
worker_processes 4;
```

معنی ساده:

```text id="qoqj8q"
چند worker process برای پردازش requestها اجرا شود.
```

مقدار `auto` معمولاً بر اساس تعداد CPU core تنظیم می‌شود.

برای دیدن CPU coreها:

```bash id="pmyv3c"
nproc
```

یا:

```bash id="s3n7cg"
lscpu
```

## قانون ذهنی

برای Nginx معمولاً:

```text id="td38za"
worker_processes ≈ تعداد CPU core
```

اما این قانون مطلق نیست. اگر workload بیشتر I/O-bound باشد، CPU همیشه bottleneck نیست.

---

## چرا زیاد کردن worker همیشه بهتر نیست؟

اگر worker زیادتر از CPU core باشد:

```text id="zcw2vo"
- context switch بیشتر می‌شود
- cache locality بدتر می‌شود
- lock contention ممکن است بیشتر شود
- debug سخت‌تر می‌شود
```

در Nginx، کیفیت event loop و non-blocking I/O مهم‌تر از زیاد کردن worker است.

---

## تمرین هفته ۱، بخش ۱

`worker_processes` را تغییر بده:

```nginx id="hpiwoj"
worker_processes 1;
```

بعد:

```bash id="4ci8se"
sudo nginx -t
sudo systemctl reload nginx
ps aux | grep nginx
```

بعد مقدار را بگذار:

```nginx id="o4cfb2"
worker_processes auto;
```

دوباره processها را ببین.

---

## روز ۳: signals در Nginx

Nginx با signalها کنترل می‌شود.

دستور reload:

```bash id="y3j3uj"
sudo systemctl reload nginx
```

در پشت صحنه معمولاً signal به master process ارسال می‌شود.

Signalهای مهم:

| Signal | معنی              |
| ------ | ----------------- |
| `HUP`  | reload config     |
| `QUIT` | graceful shutdown |
| `TERM` | fast shutdown     |
| `USR1` | reopen logs       |
| `USR2` | binary upgrade    |

برای دیدن PID master:

```bash id="0h3rap"
cat /run/nginx.pid
```

یا:

```bash id="j5pcc2"
ps aux | grep "nginx: master"
```

ارسال reload دستی:

```bash id="dqunm4"
sudo kill -HUP $(cat /run/nginx.pid)
```

## مفهوم graceful reload

در reload:

```text id="7wvn89"
1. master config جدید را می‌خواند.
2. اگر config معتبر بود، workerهای جدید را اجرا می‌کند.
3. workerهای قدیمی دیگر connection جدید نمی‌گیرند.
4. workerهای قدیمی connectionهای فعلی را تمام می‌کنند.
5. workerهای قدیمی خارج می‌شوند.
```

این برای production حیاتی است.

---

## روز ۴: process، thread و event-driven model

مدل‌های رایج web server:

```text id="0bnxhb"
1. process per request
2. thread per request
3. event-driven non-blocking
```

### process per request

برای هر request یک process جدا:

```text id="9ssth3"
request 1 → process 1
request 2 → process 2
request 3 → process 3
```

مشکل:

```text id="o78cd3"
- سنگین
- memory زیاد
- context switch زیاد
```

### thread per request

برای هر request یک thread:

```text id="7fxyks"
request 1 → thread 1
request 2 → thread 2
request 3 → thread 3
```

بهتر از process، ولی هنوز:

```text id="je84zw"
- thread stack memory دارد
- context switch دارد
- تعداد خیلی زیاد thread مشکل‌ساز است
```

### event-driven non-blocking

چند worker کم، تعداد زیادی connection:

```text id="vdasw8"
worker 1:
  - connection A
  - connection B
  - connection C
  - connection D
```

Nginx معمولاً این مدل را استفاده می‌کند.

---

## روز ۵: چرا Nginx connection زیاد هندل می‌کند؟

چون به‌جای اینکه برای هر connection یک thread جدا بسازد، از event loop و non-blocking socket استفاده می‌کند.

تصویر ساده:

```text id="5tcomf"
Worker process
  ↓
Event loop
  ↓
Check ready events
  ├── client A readable
  ├── client B writable
  ├── upstream C readable
  └── timeout D
```

Worker منتظر یک connection خاص نمی‌ماند. فقط وقتی kernel می‌گوید یک socket آماده read/write است، worker روی آن کار می‌کند.

---

## خروجی هفته ۱

در پایان هفته ۱ باید بتوانی به این سؤال‌ها جواب بدهی:

```text id="zpng94"
[ ] master process چه کار می‌کند؟
[ ] worker process چه کار می‌کند؟
[ ] worker_processes auto یعنی چه؟
[ ] چرا worker زیاد همیشه بهتر نیست؟
[ ] graceful reload چگونه کار می‌کند؟
[ ] تفاوت process-per-request و event-driven چیست؟
[ ] چرا Nginx با thread-per-request طراحی نشده؟
```

---

# هفته ۲: File Descriptor، Socket و Connection

## هدف هفته ۲

در پایان این هفته باید بفهمی:

* file descriptor چیست؟
* socket چیست؟
* connection چیست؟
* چرا connectionها file descriptor مصرف می‌کنند؟
* `worker_connections` یعنی چه؟
* چرا `ulimit` برای Nginx مهم است؟
* چرا یک reverse proxy برای هر client ممکن است بیشتر از یک fd مصرف کند؟

---

## روز ۶: File Descriptor چیست؟

در Linux تقریباً همه چیز file descriptor دارد:

```text id="72wvno"
- فایل باز
- socket
- pipe
- log file
- connection
```

File descriptor یک عدد است که process با آن یک resource باز را مدیریت می‌کند.

برای دیدن fdهای یک process:

اول PID worker را پیدا کن:

```bash id="8v363x"
pgrep -f "nginx: worker"
```

بعد:

```bash id="y6lyqn"
sudo ls -l /proc/<PID>/fd
```

یا تعدادشان:

```bash id="dxnx4m"
sudo ls /proc/<PID>/fd | wc -l
```

---

## روز ۷: ulimit

هر process محدودیت تعداد file descriptor دارد.

دیدن limit فعلی shell:

```bash id="tsocpx"
ulimit -n
```

دیدن limit یک process:

```bash id="z3ve51"
cat /proc/<PID>/limits
```

دنبال این بگرد:

```text id="bhtg9p"
Max open files
```

در Nginx config:

```nginx id="wuqu2f"
worker_rlimit_nofile 65535;
```

اما این تنها کافی نیست. systemd هم ممکن است limit داشته باشد.

برای systemd override:

```bash id="g3950i"
sudo systemctl edit nginx
```

محتوا:

```ini id="ooc7u1"
[Service]
LimitNOFILE=65535
```

بعد:

```bash id="o18hi1"
sudo systemctl daemon-reload
sudo systemctl restart nginx
```

## هشدار

عدد بزرگ بدون فهم bottleneckهای دیگر معجزه نمی‌کند. فقط سقف fd را بالا می‌برد.

---

## روز ۸: Socket چیست؟

Socket endpoint ارتباط شبکه است.

برای دیدن socketها:

```bash id="tqmb8o"
ss -tulpen
```

گزینه‌ها:

| گزینه | معنی      |
| ----- | --------- |
| `-t`  | TCP       |
| `-u`  | UDP       |
| `-l`  | listening |
| `-p`  | process   |
| `-e`  | extended  |
| `-n`  | numeric   |

برای دیدن listening socketهای Nginx:

```bash id="e72xrt"
sudo ss -tulpen | grep nginx
```

نمونه:

```text id="lro5ox"
LISTEN 0 511 0.0.0.0:80 0.0.0.0:* users:(("nginx",pid=1002,fd=6))
```

معنی:

```text id="d4bzxp"
Nginx روی port 80 گوش می‌دهد.
fd=6 یعنی این listening socket یک file descriptor است.
```

---

## روز ۹: Connection چیست؟

یک TCP connection بین client و server ساخته می‌شود.

```text id="agaf6o"
Client socket ← TCP connection → Server socket
```

برای دیدن connectionهای فعال به port 80:

```bash id="lxsozj"
ss -tan sport = :80
```

یا:

```bash id="1jxakf"
ss -tan | grep ':80'
```

Stateهای مهم:

| State        | معنی                                                  |
| ------------ | ----------------------------------------------------- |
| `LISTEN`     | socket آماده قبول connection است                      |
| `SYN-SENT`   | client درخواست connection داده                        |
| `SYN-RECV`   | server SYN گرفته و پاسخ داده                          |
| `ESTAB`      | connection برقرار است                                 |
| `TIME-WAIT`  | connection بسته شده ولی هنوز در kernel نگهداری می‌شود |
| `CLOSE-WAIT` | peer بسته، ولی app هنوز کامل نبسته                    |

---

## روز ۱۰: worker_connections

Directive:

```nginx id="h1rskz"
events {
    worker_connections 1024;
}
```

معنی ساده:

```text id="eeyt8v"
هر worker حداکثر چند connection همزمان می‌تواند مدیریت کند.
```

اما در reverse proxy، هر client request ممکن است حداقل دو connection داشته باشد:

```text id="9wfdfr"
Client → Nginx
Nginx → Upstream
```

پس اگر ۱۰۰۰ client connection داری، ممکن است تقریباً ۲۰۰۰ fd/connection درگیر شود.

## فرمول ذهنی ساده

```text id="584azs"
max_connections ≈ worker_processes × worker_connections
```

اما در reverse proxy واقعی:

```text id="v0vtd0"
ظرفیت واقعی کمتر است
چون upstream connectionها، log files، open files و keepalive هم fd مصرف می‌کنند.
```

---

## تمرین هفته ۲

با `wrk` یا `hey` connection ایجاد کن.

نصب `hey`:

```bash id="3qsmji"
go install github.com/rakyll/hey@latest
```

یا اگر `wrk` داری:

```bash id="mh3z5f"
wrk -t4 -c200 -d30s http://localhost/
```

همزمان fdها را بشمار:

```bash id="2gebn8"
watch -n 1 'for p in $(pgrep -f "nginx: worker"); do echo PID=$p; sudo ls /proc/$p/fd | wc -l; done'
```

همزمان connectionها را ببین:

```bash id="pxoy09"
watch -n 1 'ss -tan | grep ":80" | wc -l'
```

---

## خروجی هفته ۲

باید بتوانی جواب بدهی:

```text id="z7f3gr"
[ ] file descriptor چیست؟
[ ] socket چیست؟
[ ] connection چیست؟
[ ] چرا connectionها fd مصرف می‌کنند؟
[ ] worker_connections دقیقاً چه چیزی را محدود می‌کند؟
[ ] ulimit -n چه ربطی به Nginx دارد؟
[ ] چرا reverse proxy بیشتر از static server fd مصرف می‌کند؟
```

---

# هفته ۳: TCP/IP و Connection Lifecycle

## هدف هفته ۳

در پایان این هفته باید بتوانی:

* TCP handshake را توضیح بدهی.
* تفاوت TCP و UDP را بفهمی.
* stateهای TCP را تشخیص بدهی.
* backlog، SYN queue و accept queue را بفهمی.
* TIME_WAIT را توضیح بدهی.
* بفهمی keepalive چرا مهم است.
* با `tcpdump` connection را ببینی.

---

## روز ۱۱: TCP Handshake

TCP connection با three-way handshake شروع می‌شود:

```text id="5a6ku4"
Client → SYN → Server
Client ← SYN-ACK ← Server
Client → ACK → Server
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
request 1 → TCP handshake → response → close
request 2 → TCP handshake → response → close
request 3 → TCP handshake → response → close
```

با keepalive:

```text id="bl77zd"
TCP handshake
request 1 → response
request 2 → response
request 3 → response
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

# هفته ۵: Non-blocking I/O، Event Loop و epoll

## هدف هفته ۵

این هفته قلب فاز ۳ است.

باید بفهمی:

* blocking I/O چیست.
* non-blocking I/O چیست.
* event loop چیست.
* `select`, `poll`, `epoll` چه تفاوتی دارند.
* چرا Nginx از مدل event-driven استفاده می‌کند.
* چرا این مدل برای connection زیاد مناسب است.

---

## روز ۲۱: Blocking I/O

در مدل blocking:

```text id="sldaqx"
read(socket)
```

اگر داده‌ای آماده نباشد، process/thread همان‌جا می‌ایستد.

تصویر:

```text id="oelgpf"
Thread 1 waits for client A
Thread 2 waits for client B
Thread 3 waits for client C
```

مشکل:

```text id="szv8yr"
برای connection زیاد، thread زیاد لازم داری.
thread زیاد یعنی memory و context switch زیاد.
```

---

## روز ۲۲: Non-blocking I/O

در non-blocking mode:

```text id="af4t55"
read(socket)
```

اگر داده آماده نباشد، kernel فوراً می‌گوید:

```text id="r6taqq"
EAGAIN / EWOULDBLOCK
```

یعنی:

```text id="76u888"
الان داده‌ای نیست؛ بعداً دوباره امتحان کن.
```

پس worker گیر نمی‌کند و می‌تواند سراغ connectionهای دیگر برود.

---

## روز ۲۳: Event Loop

Event loop یعنی process در یک حلقه از kernel می‌پرسد:

```text id="sgysks"
کدام socketها آماده read/write هستند؟
```

تصویر:

```text id="ab1sg9"
while true:
    events = wait_for_ready_events()

    for event in events:
        handle(event)
```

در Nginx:

```text id="tsv3i6"
worker process
  ↓
event loop
  ↓
ready connections
  ↓
read/write/process
```

---

## روز ۲۴: select و poll

روش‌های قدیمی‌تر:

```text id="ruvqy7"
select
poll
```

مشکل:

```text id="ga5bdl"
با تعداد fd زیاد، inefficient می‌شوند.
هر بار باید لیست زیادی از fdها بررسی شود.
```

برای connection زیاد، این مدل‌ها محدودیت دارند.

---

## روز ۲۵: epoll

در Linux، `epoll` برای تعداد زیاد fd مناسب‌تر است.

تصویر ساده:

```text id="678tq6"
Nginx fdها را به epoll معرفی می‌کند.
Kernel وقتی event آماده شد خبر می‌دهد.
Nginx فقط eventهای آماده را پردازش می‌کند.
```

مزیت:

```text id="uwn6z9"
- مناسب connection زیاد
- overhead کمتر نسبت به select/poll
- پایه مدل event-driven Nginx روی Linux
```

برای دیدن system callها:

```bash id="2v514u"
sudo strace -p <NGINX_WORKER_PID>
```

احتمالاً چیزهایی مثل این می‌بینی:

```text id="sby4af"
epoll_wait(...)
accept4(...)
recvfrom(...)
sendfile(...)
writev(...)
```

برای خروج از strace:

```text id="gvn68b"
Ctrl + C
```

---

## روز ۲۶: strace روی Nginx

یک worker PID پیدا کن:

```bash id="c38mi8"
pgrep -f "nginx: worker"
```

روی یکی attach کن:

```bash id="n2d41t"
sudo strace -p <PID>
```

در terminal دیگر request بزن:

```bash id="n3z5la"
curl http://localhost/
```

خروجی را ببین.

برای محدود کردن system callها:

```bash id="sj6byh"
sudo strace -p <PID> -e trace=network
```

یا:

```bash id="vz1xgh"
sudo strace -p <PID> -e trace=epoll_wait,accept4,recvfrom,sendto,read,write
```

---

## روز ۲۷: sendfile و static files

برای static file serving، Nginx می‌تواند از `sendfile` استفاده کند.

داخل `http`:

```nginx id="tn0e5f"
sendfile on;
```

مفهوم:

```text id="430alw"
فایل از disk/page cache به socket ارسال می‌شود
بدون copy اضافی به user space
```

این می‌تواند برای static files مفید باشد.

## تست concept با strace

یک فایل static بزرگ بساز:

```bash id="jhk3qv"
sudo dd if=/dev/zero of=/var/www/html/big.bin bs=1M count=100
```

Nginx config با static serving.

بعد:

```bash id="kx6azc"
sudo strace -p <PID> -e trace=sendfile,read,write
```

در terminal دیگر:

```bash id="ckzxr9"
curl http://localhost/big.bin -o /dev/null
```

دنبال `sendfile(...)` بگرد.

---

## خروجی هفته ۵

باید بتوانی جواب بدهی:

```text id="7syzfl"
[ ] blocking I/O چیست؟
[ ] non-blocking I/O چیست؟
[ ] EAGAIN یعنی چه؟
[ ] event loop چیست؟
[ ] select/poll چه محدودیتی دارند؟
[ ] epoll چه مزیتی دارد؟
[ ] Nginx چرا با connection زیاد خوب کار می‌کند؟
[ ] sendfile چه کاری انجام می‌دهد؟
```

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

# هفته ۸ تا ۱۲: Benchmarking، Tracing و Debugging

این بخش فاز ۳ را عملی و جدی می‌کند. اگر فقط تا هفته ۷ بخوانی ولی benchmark و tracing انجام ندهی، فهمت ناقص می‌ماند.

---

# هفته ۸: Benchmarking پایه

## ابزارهای پیشنهادی

```text id="rg7lrl"
wrk
hey
ab
k6
vegeta
```

برای شروع `wrk` کافی است.

نصب روی Ubuntu:

```bash id="c8d8lf"
sudo apt install wrk
```

تست ساده:

```bash id="gswqbf"
wrk -t4 -c100 -d30s http://localhost/
```

معنی:

| گزینه   | معنی                 |
| ------- | -------------------- |
| `-t4`   | چهار thread برای wrk |
| `-c100` | صد connection همزمان |
| `-d30s` | مدت تست ۳۰ ثانیه     |

خروجی‌هایی که مهم‌اند:

```text id="8kulib"
Requests/sec
Latency avg
Latency max
Transfer/sec
Socket errors
Non-2xx/3xx responses
```

---

## سناریوهای benchmark

### ۱. Static file

```bash id="powdd3"
wrk -t4 -c100 -d30s http://localhost/static/app.js
```

### ۲. Reverse proxy به app سریع

```bash id="u0cmre"
wrk -t4 -c100 -d30s http://localhost/api/fast
```

### ۳. Reverse proxy به app کند

```bash id="x5jido"
wrk -t4 -c100 -d30s http://localhost/api/slow
```

### ۴. HTTPS

```bash id="zno5cf"
wrk -t4 -c100 -d30s https://localhost/
```

### ۵. Keepalive off/on

با keepalive تنظیمات را مقایسه کن.

---

## قانون benchmark

یک benchmark بد، از benchmark نگرفتن بدتر است.

باید ثابت نگه داری:

```text id="0x6sua"
- hardware
- config
- app version
- endpoint
- concurrency
- duration
- network path
```

---

# هفته ۹: Latency و Percentileها

Average کافی نیست.

فرض کن:

```text id="idsb5o"
۹۹ request در 20ms جواب می‌دهند
۱ request در 3000ms جواب می‌دهد
```

میانگین ممکن است قابل قبول باشد، ولی کاربرانی که request کند گرفته‌اند تجربه بدی دارند.

متریک‌های مهم:

| Metric | معنی                                 |
| ------ | ------------------------------------ |
| p50    | نصف requestها سریع‌تر از این مقدارند |
| p95    | ۹۵٪ requestها سریع‌تر از این مقدارند |
| p99    | ۹۹٪ requestها سریع‌تر از این مقدارند |
| max    | بدترین request                       |

## چرا p99 مهم است؟

چون production با average اداره نمی‌شود. tail latency روی تجربه کاربر و reliability اثر جدی دارد.

---

## wrk با latency

```bash id="unxmvo"
wrk -t4 -c100 -d30s --latency http://localhost/
```

به این بخش دقت کن:

```text id="8we852"
Latency Distribution
  50%
  75%
  90%
  99%
```

---

# هفته ۱۰: strace و tcpdump در Debug واقعی

## سناریو ۱: 502

Backend خاموش:

```bash id="8bmmwt"
curl -i http://localhost/api/test
```

بررسی:

```bash id="y5ndt6"
sudo tail -f /var/log/nginx/error.log
ss -tan | grep 4000
```

سؤال:

```text id="mtg7bv"
آیا Nginx اصلاً توانسته به upstream connect کند؟
```

---

## سناریو ۲: 504

Backend کند:

```js id="8pht74"
app.get("/slow", async (req, res) => {
  await new Promise(resolve => setTimeout(resolve, 60000));
  res.json({ ok: true });
});
```

Nginx timeout:

```nginx id="4vigrz"
proxy_read_timeout 10s;
```

تست:

```bash id="l5sovg"
curl -i http://localhost/api/slow
```

بررسی:

```bash id="5wofeb"
sudo tail -f /var/log/nginx/error.log
```

---

## سناریو ۳: client کند

فایل بزرگ:

```bash id="znubkb"
curl --limit-rate 10k http://localhost/big.bin -o /tmp/big.bin
```

همزمان connectionها را ببین:

```bash id="03zyvi"
ss -tan | grep ':80'
```

buffering و sendfile را بررسی کن.

---

# هفته ۱۱: perf و CPU Profiling

اگر CPU bottleneck داری، باید بتوانی ببینی CPU کجا مصرف می‌شود.

نصب:

```bash id="5eq6sl"
sudo apt install linux-tools-common linux-tools-generic
```

ضبط profile:

```bash id="ke6nu5"
sudo perf top -p <NGINX_WORKER_PID>
```

یا:

```bash id="rvl8pb"
sudo perf record -p <NGINX_WORKER_PID> -g -- sleep 30
sudo perf report
```

## چه زمانی perf مفید است؟

```text id="rm4j4g"
- TLS CPU بالا
- gzip CPU بالا
- static serving سنگین
- request rate خیلی بالا
- regex locationهای سنگین
```

---

# هفته ۱۲: پروژه نهایی فاز ۳

## معماری lab نهایی

```text id="ice4bl"
Client benchmark tool
  ↓
Nginx
  ├── static files
  ├── reverse proxy
  ├── HTTPS
  ├── keepalive
  ├── buffering on/off
  └── upstream apps
        ├── fast endpoint
        ├── slow endpoint
        ├── streaming endpoint
        └── large response endpoint
```

---

# Config نمونه lab فاز ۳

```nginx id="hqqps3"
worker_processes auto;
worker_rlimit_nofile 65535;

events {
    worker_connections 4096;
}

http {
    sendfile on;

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

    upstream app_backend {
        least_conn;

        server 127.0.0.1:4001 max_fails=3 fail_timeout=10s;
        server 127.0.0.1:4002 max_fails=3 fail_timeout=10s;

        keepalive 32;
    }

    server {
        listen 80;
        server_name _;

        access_log /var/log/nginx/phase3.access.log perf_json;
        error_log /var/log/nginx/phase3.error.log warn;

        location = /nginx-health {
            access_log off;
            return 200 "ok\n";
        }

        location /static/ {
            root /var/www/phase3;
            try_files $uri =404;
            expires 7d;
        }

        location /api/ {
            proxy_pass http://app_backend/;

            proxy_http_version 1.1;
            proxy_set_header Connection "";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Request-ID $request_id;

            proxy_connect_timeout 5s;
            proxy_send_timeout 30s;
            proxy_read_timeout 30s;
        }

        location /stream/ {
            proxy_pass http://app_backend/stream/;

            proxy_http_version 1.1;
            proxy_set_header Connection "";
            proxy_set_header Host $host;

            proxy_buffering off;
            proxy_read_timeout 300s;
        }
    }
}
```

---

# تست‌های نهایی فاز ۳

## ۱. تست processها

```bash id="ac46nl"
ps aux | grep nginx
pstree -p | grep nginx
```

گزارش کن:

```text id="6rwhmb"
Master PID:
Worker PIDs:
Number of workers:
```

---

## ۲. تست file descriptors

```bash id="yb3k2q"
for p in $(pgrep -f "nginx: worker"); do
  echo "PID=$p"
  sudo ls /proc/$p/fd | wc -l
done
```

زیر load اجرا کن و قبل/بعد را مقایسه کن.

---

## ۳. تست connectionها

```bash id="uo27ek"
ss -tan | grep ':80' | awk '{print $1}' | sort | uniq -c
```

زیر load ببین چه stateهایی بیشترند.

---

## ۴. تست benchmark

```bash id="dycmkb"
wrk -t4 -c100 -d30s --latency http://localhost/static/big.bin
wrk -t4 -c100 -d30s --latency http://localhost/api/fast
wrk -t4 -c100 -d30s --latency http://localhost/api/slow
```

نتیجه را ثبت کن:

```text id="5qjtmc"
Requests/sec:
p50:
p95:
p99:
Errors:
```

---

## ۵. تست tcpdump

```bash id="z0yx81"
sudo tcpdump -i lo -nn tcp port 80
```

در terminal دیگر:

```bash id="dkq6jk"
curl http://localhost/api/fast
```

در گزارش بنویس:

```text id="z0rnf0"
Did you observe SYN?
Did you observe SYN-ACK?
Did you observe ACK?
Did you observe FIN?
```

---

## ۶. تست strace

```bash id="klt62x"
sudo strace -p <WORKER_PID> -e trace=epoll_wait,accept4,recvfrom,sendto,sendfile
```

در terminal دیگر:

```bash id="wgzcg1"
curl http://localhost/static/big.bin -o /dev/null
curl http://localhost/api/fast
```

در گزارش بنویس:

```text id="ldc8y3"
Observed syscalls:
- epoll_wait:
- accept4:
- recvfrom:
- sendto:
- sendfile:
```

---

# Checklist فاز ۳

در پایان فاز ۳ باید بتوانی این‌ها را انجام بدهی:

```text id="3q5nph"
[ ] processهای Nginx را شناسایی کنم
[ ] master و worker را توضیح بدهم
[ ] graceful reload را توضیح بدهم
[ ] worker_processes را تحلیل کنم
[ ] file descriptorهای worker را ببینم
[ ] ulimit و worker_rlimit_nofile را بفهمم
[ ] socketهای listening را با ss ببینم
[ ] connection stateها را تشخیص بدهم
[ ] TCP handshake را با tcpdump ببینم
[ ] TIME_WAIT را توضیح بدهم
[ ] backlog و somaxconn را بفهمم
[ ] HTTP keep-alive را توضیح بدهم
[ ] upstream keepalive را کانفیگ کنم
[ ] proxy headers را از منظر network توضیح بدهم
[ ] chunked transfer را بفهمم
[ ] buffering را از منظر client کند توضیح بدهم
[ ] blocking و non-blocking I/O را توضیح بدهم
[ ] event loop را توضیح بدهم
[ ] epoll را توضیح بدهم
[ ] strace روی worker بگیرم
[ ] sendfile را مشاهده کنم
[ ] TLS handshake را با openssl بررسی کنم
[ ] HTTP/2 multiplexing را توضیح بدهم
[ ] HTTP/3 و QUIC را conceptually بفهمم
[ ] sysctlهای مهم را مشاهده کنم
[ ] benchmark با wrk بگیرم
[ ] p95 و p99 را تحلیل کنم
[ ] با access log بفهمم upstream کند است یا Nginx
[ ] با perf شروع به CPU profiling کنم
```

---

# سؤال‌هایی که باید بتوانی جواب بدهی

## Process و Worker

* master process در Nginx چه کاری انجام می‌دهد؟
* worker process چه کاری انجام می‌دهد؟
* چرا `worker_processes auto` معمولاً خوب است؟
* چرا زیاد کردن worker همیشه performance را بهتر نمی‌کند؟
* graceful reload چگونه connectionهای فعال را حفظ می‌کند؟

## File Descriptor و Connection

* file descriptor چیست؟
* socket چیست؟
* هر TCP connection چند fd مصرف می‌کند؟
* چرا reverse proxy معمولاً fd بیشتری از static server مصرف می‌کند؟
* `worker_connections` چه چیزی را محدود می‌کند؟
* `ulimit -n` چه ربطی به Nginx دارد؟

## TCP/IP

* three-way handshake چیست؟
* `SYN-RECV` یعنی چه؟
* `TIME-WAIT` چرا وجود دارد؟
* listen backlog چیست؟
* فرق SYN queue و accept queue چیست؟
* keepalive چه مزایا و معایبی دارد؟

## HTTP

* Host header چرا مهم است؟
* `X-Forwarded-For` چرا هم مفید است هم خطرناک؟
* HTTP keep-alive با TCP keepalive چه فرق دارد؟
* chunked transfer چیست؟
* چرا client کند می‌تواند روی upstream اثر بگذارد؟

## Event Loop

* blocking I/O چیست؟
* non-blocking I/O چیست؟
* `EAGAIN` یعنی چه؟
* event loop چیست؟
* `epoll_wait` چه کاری انجام می‌دهد؟
* چرا Nginx برای connection زیاد مناسب است؟

## TLS و HTTP/2

* TLS handshake چه مراحلی دارد؟
* چرا HTTPS از HTTP cost بیشتری دارد؟
* HTTP/2 multiplexing چیست؟
* HTTP/2 چه مشکلی را حل نمی‌کند؟
* HTTP/3 چرا روی UDP ساخته شده؟
* ALPN چیست؟

## Performance

* چرا average latency کافی نیست؟
* p95 و p99 چه معنایی دارند؟
* چطور با `wrk` benchmark می‌گیری؟
* چطور با `strace` system callها را می‌بینی؟
* چطور با `tcpdump` handshake را مشاهده می‌کنی؟
* چه زمانی از `perf` استفاده می‌کنی؟

---

# گزارش نهایی فاز ۳

در پایان فاز ۳ یک فایل Markdown بساز:

```md id="94b79k"
# Nginx Phase 3 Systems Report

## 1. Lab Architecture

Describe your Nginx + upstream architecture.

## 2. Process Model

Master PID:

Worker PIDs:

worker_processes value:

Explanation:

## 3. File Descriptors

Before load:

During load:

After load:

Observation:

## 4. Connections

TCP states observed:

ESTABLISHED count:

TIME_WAIT count:

Observation:

## 5. TCP Handshake

Tool used:

Observed SYN:

Observed SYN-ACK:

Observed ACK:

Notes:

## 6. Keepalive

Client keepalive setting:

Upstream keepalive setting:

Effect observed:

## 7. Buffering

Buffering on result:

Buffering off result:

Slow client test result:

## 8. epoll / strace

Observed syscalls:

- epoll_wait:
- accept4:
- recvfrom:
- sendto:
- sendfile:

Explanation:

## 9. TLS

TLS test command:

Protocol:

Certificate result:

Handshake notes:

## 10. HTTP/2

Enabled:

Test command:

Observed protocol:

Notes:

## 11. Benchmark Results

### Static File

Requests/sec:

p50:

p95:

p99:

Errors:

### Reverse Proxy Fast Endpoint

Requests/sec:

p50:

p95:

p99:

Errors:

### Reverse Proxy Slow Endpoint

Requests/sec:

p50:

p95:

p99:

Errors:

## 12. Bottlenecks Found

List bottlenecks.

## 13. Fixes Applied

List changes.

## 14. Lessons Learned

Write 20 lessons.
```

---

# معیار موفقیت فاز ۳

فاز ۳ را وقتی تمام کرده‌ای که بتوانی این سناریوها را debug کنی:

```text id="jtfhnr"
- تعداد connection زیاد شده و باید بفهمی fd limit نزدیک شده یا نه
- requestها کند شده‌اند و باید بفهمی مشکل از upstream است یا Nginx
- TIME_WAIT زیاد می‌بینی و panic نمی‌کنی
- 504 می‌گیری و می‌توانی TCP/application timeout را جدا کنی
- client کند باعث رفتار عجیب شده و buffering را تحلیل می‌کنی
- static file serving کند است و sendfile/page cache را بررسی می‌کنی
- HTTPS CPU مصرف می‌کند و TLS cost را می‌فهمی
- p99 latency بد است ولی average خوب است و دلیلش را دنبال می‌کنی
- با strace می‌بینی worker واقعاً چه syscallهایی اجرا می‌کند
- با tcpdump می‌توانی handshake و close شدن connection را ببینی
```

---

# منابع پیشنهادی فاز ۳

## Linux و سیستم‌عامل

* The Linux Programming Interface — Michael Kerrisk
* Operating Systems: Three Easy Pieces
* Computer Systems: A Programmer’s Perspective
* Systems Performance — Brendan Gregg

## Network

* Computer Networking: A Top-Down Approach
* TCP/IP Illustrated
* UNIX Network Programming — W. Richard Stevens
* High Performance Browser Networking

## Performance و Debugging

* Systems Performance — Brendan Gregg
* BPF Performance Tools — Brendan Gregg
* man pages:

  * `man socket`
  * `man epoll`
  * `man tcp`
  * `man ss`
  * `man strace`
  * `man tcpdump`

## Nginx

* Nginx official documentation
* Nginx development guide
* Nginx source code
* Nginx architecture articles

---

# توصیه جدی برای فاز ۳

این فاز را فقط با خواندن جلو نبر. اگر دستت به ابزارها نخورد، این مفاهیم در ذهنت واقعی نمی‌شوند.

برای هر مفهوم باید این کار را بکنی:

```text id="3xioq4"
Read → Observe → Break → Measure → Explain
```

مثلاً برای TCP handshake:

```text id="fvaxqp"
Read about handshake
Observe with tcpdump
Break by stopping service
Measure connection states
Explain what happened
```

برای file descriptor:

```text id="t8t7xa"
Read about fd
Observe /proc/<pid>/fd
Increase load
Measure fd count
Explain relation to worker_connections
```

برای epoll:

```text id="2ihzts"
Read about event loop
Observe epoll_wait with strace
Generate traffic
Compare static/proxy behavior
Explain why worker does not block
```

اگر این روش را جدی انجام بدهی، Nginx برایت از یک config file تبدیل می‌شود به یک سیستم واقعی که می‌توانی رفتار آن را از سطح HTTP تا kernel توضیح بدهی.
