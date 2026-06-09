# مسیر یادگیری Nginx

یادداشت‌های شخصی برای یادگیری Nginx، Linux و Git — از نصب و reverse proxy تا شبکه و production.

| # | فصل | زمان تقریبی |
| ---: | --- | --- |
| 1 | [فاز ۱: پایه عملی Nginx](nginx/phase1.md) | ۲–۳ هفته |
| 2 | [فاز ۲: Production Operations](nginx/phase2.md) | ۴–۶ هفته |
| 3 | [فاز ۳: شبکه و سیستم‌عامل](nginx/phase3-network.md) | ۲–۳ ماه |
| 4 | [Linux برای توسعه‌دهنده](linux/linux.md) | — |
| 5 | [grep](linux/grep.md) | — |
| 6 | [Git Pull و Fast-Forward](git/rebase-fast-forward.md) | — |
| 7 | [HEAD در Git](git/head-guide.md) | — |
| 8 | [سؤالات Git (Pull / Rebase)](git/rebase-questions.md) | — |

---

## خواندن به‌صورت کتاب

```bash
./scripts/build-book.sh
```

بعد `book/index.html` را در مرورگر باز کن. متن فارسی راست‌چین است؛ کدها چپ‌چین.

---

## ساختار

1. کانفیگ عملی و production
2. معماری داخلی و moduleها
3. شبکه، OS و performance

---

## زمان‌بندی (تقریبی)

| هدف | زمان |
| --- | ---: |
| استفاده در پروژه | ۱–۲ ماه |
| production / DevOps | ۳–۶ ماه |
| معماری و performance | ۶–۱۲ ماه |
| سطح پژوهشی | ۱۲–۱۸ ماه |

---

## روش کار

```text
بخوان → کانفیگ کن → خراب کن → تست بگیر → log ببین → توضیح بده → درست کن
```

برای هر موضوع: مستندات رسمی، یک config کوچک، عمداً یک چیز را اشتباه کن، log و metric را چک کن، بعد config را بهتر کن.

---

راهنمای ویرایش: [HOW-TO-EDIT.md](../HOW-TO-EDIT.md)
