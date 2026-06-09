# مسیر یادگیری Nginx

یادداشت‌های شخصی برای یادگیری Nginx، Linux و Git.

| # | فصل | مسیر |
| ---: | --- | --- |
| 1 | [مقدمه](content/introduction.md) | — |
| 2 | [فاز ۱: Nginx عملی](content/nginx/phase1.md) | ۲–۳ هفته |
| 3 | [فاز ۲: Production](content/nginx/phase2.md) | ۴–۶ هفته |
| 4 | [فاز ۳: شبکه و OS](content/nginx/phase3-network.md) | ۲–۳ ماه |
| 5 | [Linux](content/linux/linux.md) | — |
| 6 | [grep](content/linux/grep.md) | — |
| 7 | [Git Pull / Rebase](content/git/rebase-fast-forward.md) | — |
| 8 | [HEAD در Git](content/git/head-guide.md) | — |
| 9 | [سؤالات Git](content/git/rebase-questions.md) | — |

## کتاب (mdBook)

**آنلاین:** https://yasersharifi.github.io/learn-nginx/

**محلی:**

```bash
./scripts/build-book.sh
./.bin/mdbook serve   # http://localhost:3000
```

اولین بار روی GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions** را فعال کن. بعد از هر push به `main`، workflow کتاب را deploy می‌کند.

## ویرایش

همهٔ markdownها داخل [`content/`](content/). راهنما: [HOW-TO-EDIT.md](HOW-TO-EDIT.md)
