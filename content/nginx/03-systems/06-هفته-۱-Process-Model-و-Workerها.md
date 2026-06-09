---
title: "هفته ۱: Process Model و Workerها"
description: "هفته ۱: Process Model و Workerها"
---

# هفته ۱: Process Model و Workerها

## هدف هفته ۱

در پایان این هفته باید بتوانی توضیح بدهی:

- process چیست؟
- thread چیست؟
- master process در Nginx چه می‌کند؟
- worker process در Nginx چه می‌کند؟
- چرا Nginx معمولاً process-based است، نه thread-per-request؟
- چرا `worker_processes auto` معمولاً انتخاب خوبی است؟
- چرا زیاد کردن worker همیشه performance را بهتر نمی‌کند؟

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
request 1 ← process 1
request 2 ← process 2
request 3 ← process 3
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
request 1 ← thread 1
request 2 ← thread 2
request 3 ← thread 3
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
