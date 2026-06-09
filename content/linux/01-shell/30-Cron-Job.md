---
title: "30. Cron Job"
description: "30. Cron Job"
---

# 30. Cron Job

Cron برای اجرای زمان‌بندی‌شده commandهاست.

### باز کردن crontab

```bash
crontab -e
```

### دیدن cronهای فعلی

```bash
crontab -l
```

### اجرای اسکریپت هر روز ساعت ۲ صبح

```cron
0 2 * * * /home/ubuntu/scripts/backup.sh
```

### اجرای هر ۵ دقیقه

```cron
*/5 * * * * /home/ubuntu/scripts/check-health.sh
```

نکته مهم: در cron مسیرها و envها محدود هستند. بهتر است مسیر کامل commandها را بنویسید و خروجی را log کنید:

```cron
*/5 * * * * /usr/bin/node /home/ubuntu/app/worker.js >> /home/ubuntu/app/worker.log 2>&1
```

---
