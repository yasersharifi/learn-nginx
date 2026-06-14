---
title: مرور بخش‌ها
description: خلاصهٔ کوتاه هر فصل برای مرور سریع قبل از مطالعه یا امتحان
sidebar_position: 3
---

# مرور بخش‌ها

خلاصهٔ یک‌خطی هر قسمت — برای مرور قبل از شروع یا بعد از اتمام فصل.

---

## راهنمای عملیات روزمره

| موضوع | خلاصه |
| --- | --- |
| Nginx | `nginx -t`، reload امن، جدول 502/504/404، workflow debug |
| Linux | `curl`، `ss`، `lsof`، journalctl، grep در log |
| Git | pull/rebase/merge، divergent branches، force-with-lease |
| یکپارچه | چک‌لیست ۵ دقیقه‌ای وقتی سایت down است |

[شروع راهنمای روزمره ←](/daily-guide)

---

## Nginx · فصل ۱ — پایه عملی

| موضوع         | خلاصه                                              |
| ------------- | -------------------------------------------------- |
| جایگاه Nginx  | جلوی اپ؛ web server، reverse proxy، load balancer  |
| نصب و مسیرها  | `systemctl`، `/etc/nginx`، `nginx -t`، `nginx -T`  |
| ساختار config | `main` ← `events` ← `http` ← `server` ← `location` |
| Static        | `root`، `try_files`، تفاوت `root` و `alias`        |
| Reverse proxy | `proxy_pass`، headerها، slash آخر                  |
| چند سرویس     | `/api/` و `/` روی upstreamهای مختلف                |
| خطاهای رایج   | 502، 404، 403، 504 — علت و debug                   |
| Virtual host  | `server_name`، default server                      |
| Location      | exact، prefix، regex                               |
| Log           | access.log، error.log، format سفارشی               |
| Load balance  | `upstream`، round-robin، weight، `least_conn`      |
| HTTPS         | self-signed، redirect HTTP←HTTPS                   |
| WebSocket     | `Upgrade` و `Connection`                           |
| پروژه نهایی   | lab کامل frontend + API + static                   |

[شروع فصل ۱ ←](/category/فصل-۱--پایه-عملی)

---

## Nginx · فصل ۲ — Production

| موضوع          | خلاصه                                       |
| -------------- | ------------------------------------------- |
| ساختار config  | snippets، modular، قابل نگهداری             |
| Timeout        | connect / send / read — endpoint کند vs API |
| Buffering      | on برای API؛ off برای streaming             |
| Upload limit   | `client_max_body_size`، 413                 |
| Error handling | `proxy_intercept_errors`، JSON برای API     |
| Upstream       | `keepalive`، `max_fails`، `least_conn`      |
| Retry          | `proxy_next_upstream` — خطر POST            |
| Cache          | static asset + `proxy_cache`                |
| Rate limit     | `limit_req`، 429                            |
| Security       | headerها، real IP، HSTS با احتیاط           |
| Observability  | JSON log، `$request_id`                     |
| HTTPS واقعی    | Let's Encrypt، HTTP/2                       |

[شروع فصل ۲ ←](/category/فصل-۲--production)

---

## Nginx · فصل ۳ — شبکه و OS

| موضوع           | خلاصه                                |
| --------------- | ------------------------------------ |
| Process model   | master / worker، `worker_processes`  |
| File descriptor | `ulimit`، `worker_connections`       |
| TCP             | handshake، TIME_WAIT، backlog        |
| HTTP            | keep-alive، proxy headers، buffering |
| Event loop      | blocking vs non-blocking، epoll      |
| TLS / HTTP2     | handshake cost، multiplexing         |
| Benchmark       | `wrk`، p95/p99                       |
| Debug           | `strace`، `tcpdump`، `perf`          |

[شروع فصل ۳ ←](/category/فصل-۳--شبکه-و-os)

---

## Linux · خط فرمان

| موضوع       | خلاصه                              |
| ----------- | ---------------------------------- |
| فایل‌سیستم  | `/etc`، `/var/log`، `/home`        |
| فایل و پوشه | `ls`، `cp`، `mv`، `rm`، permission |
| log         | `tail -f`، `grep`، `journalctl`    |
| پروسس       | `ps`، `top`، `kill`، `systemctl`   |
| شبکه        | `curl`، `ss`، `lsof`               |
| deploy      | SSH، `rsync`، PM2، Docker          |

[شروع Linux ←](/category/خط-فرمان)

---

## Linux · grep

| موضوع    | خلاصه                  |
| -------- | ---------------------- |
| پایه     | جستجوی متن در فایل     |
| گزینه‌ها | `-r`، `-i`، `-n`، `-v` |
| pipe     | فیلتر خروجی دستورات    |

[شروع grep ←](/category/grep)

---

## Git

| موضوع           | خلاصه                               |
| --------------- | ----------------------------------- |
| git pull        | fetch + merge یا rebase             |
| fast-forward    | local فقط عقب است؛ بدون commit جدید |
| merge vs rebase | branch مشترک ← merge؛ شخصی ← rebase |
| HEAD            | اشاره‌گر به commit / branch فعلی    |
| سناریوها        | ۲۰ حالت رایج با جواب                |

[شروع Git ←](/category/pull-و-merge)

---

## مرجع دستورات

| فصل | خلاصه |
| --- | --- |
| Linux | مسیر، فایل، grep، پروسس، شبکه، systemd، SSH |
| Docker | image، run، exec، log، volume، network |
| Docker Compose | up/down، build، logs، exec |
| Nginx | systemctl، `nginx -t`، مسیرها، log، debug |
| Git | status، commit، pull، push، branch، stash |
| سایر | curl، PM2، DB، cron، ufw، چک‌لیست debug |

[شروع مرجع دستورات ←](/commands)
