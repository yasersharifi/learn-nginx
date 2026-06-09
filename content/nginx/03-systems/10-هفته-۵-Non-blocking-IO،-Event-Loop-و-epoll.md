---
title: "هفته ۵: Non-blocking I/O، Event Loop و epoll"
description: "هفته ۵: Non-blocking I/O، Event Loop و epoll"
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
