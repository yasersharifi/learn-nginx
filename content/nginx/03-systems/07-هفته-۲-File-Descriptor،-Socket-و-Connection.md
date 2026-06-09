---
title: "هفته ۲: File Descriptor، Socket و Connection"
description: "هفته ۲: File Descriptor، Socket و Connection"
---

# هفته ۲: File Descriptor، Socket و Connection

## هدف هفته ۲

در پایان این هفته باید بفهمی:

- file descriptor چیست؟
- socket چیست؟
- connection چیست؟
- چرا connectionها file descriptor مصرف می‌کنند؟
- `worker_connections` یعنی چه؟
- چرا `ulimit` برای Nginx مهم است؟
- چرا یک reverse proxy برای هر client ممکن است بیشتر از یک fd مصرف کند؟

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
Client socket ← TCP connection ← Server socket
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
Client ← Nginx
Nginx ← Upstream
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
