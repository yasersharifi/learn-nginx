# سؤالات Git: Pull، Fast-Forward، Merge و Rebase

۲۰ سناریو با جواب.

---

## خلاصه

- `git pull` = fetch + merge یا rebase با remote
- local فقط عقب است → fast-forward
- local و remote هر دو commit جدید دارند → divergent
- divergent → merge یا rebase
- merge تاریخچه واقعی را نگه می‌دارد؛ rebase history را خطی می‌کند ولی commitها را عوض می‌کند
- `--ff-only` فقط fast-forward؛ وگرنه خطا

### مقایسه

| مفهوم | یعنی چی؟ | commit جدید؟ | کاربرد |
| --- | --- | :---: | --- |
| **Fast-forward** | branch جلو می‌رود | نه | local فقط عقب است |
| **Merge** | دو مسیر با merge commit | بله | branch مشترک تیم |
| **Rebase** | commitهای local روی remote دوباره چیده می‌شوند | بله (hash جدید) | branch شخصی / PR |
| **ff-only** | فقط fast-forward | نه | جلوگیری از merge ناخواسته |

### انتخاب سریع

- branch شخصی → `rebase`
- branch مشترک → `merge`
- نمی‌خواهی Git خودش merge کند → `ff-only`
- local فقط عقب است → fast-forward
- هر دو طرف commit دارند → divergent

### دستورات

```bash
git pull --rebase
git pull --no-rebase
git pull --ff-only

git fetch origin
git rebase origin/main
git merge origin/main

git rebase --continue
git rebase --abort
git push --force-with-lease
```

---

## 1. سناریو: لوکال فقط عقب است

### جواب

اگر branch لوکال فقط از remote عقب باشد و commit جدیدی در لوکال نداشته باشی، Git معمولاً **fast-forward** انجام می‌دهد.

یعنی commit جدیدی ساخته نمی‌شود و فقط pointer branch جلو می‌رود.

```txt
قبل:

local:  A---B
remote: A---B---C

بعد:

local:  A---B---C
```

---

## 2. سناریو: انتخاب بهترین update

### جواب

بهترین حالت اینجا **fast-forward** است.

چون local هیچ commit اضافه‌ای ندارد و فقط باید خودش را به remote برساند.

```bash
git pull
```

یا برای سخت‌گیرانه‌تر بودن:

```bash
git pull --ff-only
```

---

## 3. سناریو: local و remote هر دو تغییر دارند

### جواب

این وضعیت **divergent branches** است.

یعنی local و remote از یک نقطه مشترک جدا شده‌اند و هرکدام commitهایی دارند که دیگری ندارد.

```txt
local فقط D را دارد.
remote فقط C را دارد.
```

در این حالت fast-forward ممکن نیست و باید بین **merge** و **rebase** تصمیم بگیری.

---

## 4. سناریو: branch شخصی برای Pull Request

### جواب

برای branch شخصی، معمولاً `rebase` مناسب‌تر است:

```bash
git pull --rebase
```

یا دقیق‌تر:

```bash
git fetch origin
git rebase origin/main
```

چون rebase commitهای تو را روی آخرین نسخه remote می‌چیند و history خطی‌تر می‌ماند.

---

## 5. سناریو: branch مشترک تیمی

### جواب

در branch مشترک تیمی معمولاً **merge** امن‌تر است.

```bash
git pull --no-rebase
```

یا:

```bash
git fetch origin
git merge origin/develop
```

دلیلش این است که merge تاریخچه را بازنویسی نمی‌کند، ولی rebase commitها را دوباره می‌سازد و ممکن است برای بقیه مشکل ایجاد کند.

---

## 6. سناریو: فقط fast-forward مجاز باشد

### جواب

```bash
git pull --ff-only
```

فقط وقتی fast-forward ممکن است pull می‌کند؛ اگر divergent باشند خطا می‌دهد. برای جلوگیری از merge ناخواسته مفید است.

---

## 7. سناریو: تنظیم دائمی fast-forward only

### جواب

```bash
git config --global pull.ff only
```

بعد از این، `git pull` فقط وقتی موفق می‌شود که fast-forward ممکن باشد.

اگر branchها divergent باشند، Git خطا می‌دهد و تو باید آگاهانه تصمیم بگیری:

```bash
git pull --rebase
```

یا:

```bash
git pull --no-rebase
```

---

## 8. سناریو: خطای divergent branches

### جواب

یعنی local و remote هر دو commitهایی دارند که طرف مقابل ندارد.

Git نمی‌داند باید این دو مسیر را با **merge** یکی کند یا با **rebase**.

برای حلش باید یکی را مشخص کنی:

```bash
git pull --rebase
```

یا:

```bash
git pull --no-rebase
```

یا اگر فقط fast-forward را قبول داری:

```bash
git pull --ff-only
```

---

## 9. سناریو: push بعد از rebase reject می‌شود

### جواب

چون `rebase` تاریخچه را بازنویسی می‌کند.

Commit قبلی تو مثلاً `D` بوده، اما بعد از rebase تبدیل شده به commit جدیدی مثل `D'`.

حتی اگر محتوای commit یکی باشد، hash آن تغییر کرده است.

```txt
قبل:

A---B---D

بعد از rebase:

A---B---C---D'
```

پس remote هنوز commit قدیمی را می‌شناسد، ولی local commit جدیدی دارد. به همین دلیل push معمولی ممکن است reject شود.

---

## 10. سناریو: push امن بعد از rebase

### جواب

```bash
git push --force-with-lease
```

این از `--force` امن‌تر است، چون اگر کسی قبل از تو روی remote چیزی push کرده باشد، Git اجازه نمی‌دهد کار او را overwrite کنی.

---

## 11. سناریو: conflict وسط rebase

### جواب

```bash
git add .
git rebase --continue
```

---

## 12. سناریو: لغو کامل rebase

### جواب

```bash
git rebase --abort
```

این دستور rebase را لغو می‌کند و branch را به وضعیت قبل از شروع rebase برمی‌گرداند.

---

## 13. سناریو: pull همیشه با rebase باشد

### جواب

```bash
git config --global pull.rebase true
```

بعد از این، `git pull` به صورت پیش‌فرض مثل `git pull --rebase` رفتار می‌کند.

این تنظیم برای کسانی که بیشتر روی branchهای شخصی و Pull Request کار می‌کنند مفید است.

---

## 14. سناریو: تیم history واقعی mergeها را می‌خواهد

### جواب

```bash
git config --global pull.rebase false
```

یعنی `git pull` به صورت پیش‌فرض merge انجام می‌دهد، نه rebase.

این انتخاب برای branchهای مشترک تیمی امن‌تر است.

---

## 15. سناریو: نتیجه merge

### جواب

بعد از merge یک **merge commit** جدید ساخته می‌شود.

```txt
A---B---D---M
     \---C---/
```

Commit `M` نشان می‌دهد که دو مسیر جداشده دوباره با هم ترکیب شده‌اند.

---

## 16. سناریو: نتیجه rebase

### جواب

```txt
A---B---C---D'
```

Commit `D` به `D'` تبدیل می‌شود، چون Git آن را دوباره ساخته است.

---

## 17. سناریو: تغییر hash بعد از rebase

### جواب

بله، طبیعی است.

چون rebase commitهای تو را دوباره روی base جدید می‌سازد. وقتی parent commit تغییر کند، hash commit هم تغییر می‌کند.

یعنی حتی اگر محتوای تغییرات یکی باشد، commit جدید محسوب می‌شود.

---

## 18. سناریو: گرفتن remote بدون ترکیب

### جواب

```bash
git fetch origin
```

`fetch` تغییرات remote را می‌گیرد، اما آن‌ها را با branch فعلی تو merge یا rebase نمی‌کند.

بعد از fetch می‌توانی تصمیم بگیری:

```bash
git rebase origin/main
```

یا:

```bash
git merge origin/main
```

---

## 19. سناریو: rebase دستی روی origin/main

### جواب

```bash
git fetch origin
git rebase origin/main
```

---

## 20. سناریو: توصیه اشتباه درباره rebase

### جواب

نه، این توصیه همیشه درست نیست.

`rebase` history را بازنویسی می‌کند. اگر branch مشترک باشد و افراد دیگر هم روی همان branch کار کنند، rebase می‌تواند باعث شود commitهای remote و local افراد با هم ناسازگار شوند.

برای branch شخصی:

```bash
git pull --rebase
```

معمولاً خوب است.

برای branch مشترک تیمی:

```bash
git pull --no-rebase
```

معمولاً امن‌تر است.

**خلاصه:** branch شخصی → rebase · branch مشترک → merge · محافظه‌کار → ff-only

---
