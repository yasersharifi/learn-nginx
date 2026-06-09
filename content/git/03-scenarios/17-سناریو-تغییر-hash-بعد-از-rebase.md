---
title: "17. سناریو: تغییر hash بعد از rebase"
description: "17. سناریو: تغییر hash بعد از rebase"
---

# 17. سناریو: تغییر hash بعد از rebase

### جواب

بله، طبیعی است.

چون rebase commitهای تو را دوباره روی base جدید می‌سازد. وقتی parent commit تغییر کند، hash commit هم تغییر می‌کند.

یعنی حتی اگر محتوای تغییرات یکی باشد، commit جدید محسوب می‌شود.

---
