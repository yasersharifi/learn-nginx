---
title: "20. DNS و بررسی دامنه"
description: "20. DNS و بررسی دامنه"
---

# 20. DNS و بررسی دامنه

### گرفتن IP یک دامنه

```bash
nslookup example.com
```

یا:

```bash
dig example.com
```

### بررسی رکوردهای خاص

```bash
dig example.com A
```

```bash
dig example.com MX
```

```bash
dig example.com TXT
```

برای ایمیل و SPF/DKIM/DMARC بسیار کاربردی است:

```bash
dig example.com TXT
```

---
