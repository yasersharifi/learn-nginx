---
title: "روز ۲۴: Graceful Reload و Config Safety"
description: "روز ۲۴: Graceful Reload و Config Safety"
---

# روز ۲۴: Graceful Reload و Config Safety

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
