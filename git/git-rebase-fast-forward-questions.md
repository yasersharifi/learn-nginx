
```txt
git pull یعنی fetch + ترکیب تغییرات remote با local.

اگر local فقط عقب باشد، fast-forward انجام می‌شود.
اگر local و remote هر دو commit جدید داشته باشند، branchها divergent شده‌اند.
در divergent branches باید بین merge و rebase انتخاب کنیم.

merge تاریخچه واقعی را حفظ می‌کند ولی ممکن است history را شلوغ کند.
rebase history را خطی و تمیز می‌کند ولی commitها را بازنویسی می‌کند.
ff-only فقط fast-forward را قبول می‌کند و در حالت divergent خطا می‌دهد.
```

### جدول مقایسه‌ای

| مفهوم        | یعنی چی؟                                       | commit جدید می‌سازد؟ | بهترین کاربرد             |
| ------------ | ---------------------------------------------- | -------------------: | ------------------------- |
| Fast-forward | فقط branch جلو می‌رود                          |                   نه | وقتی local فقط عقب است    |
| Merge        | دو مسیر با merge commit یکی می‌شوند            |                  بله | branch مشترک تیمی         |
| Rebase       | commitهای local روی remote دوباره چیده می‌شوند |    بله، با hash جدید | branch شخصی / PR          |
| ff-only      | فقط fast-forward را قبول می‌کند                |                   نه | جلوگیری از merge ناخواسته |

### قانون تصمیم‌گیری

```txt
اگر branch شخصی است → rebase
اگر branch مشترک تیمی است → merge
اگر نمی‌خواهی Git تصمیم بگیرد → ff-only
اگر local فقط عقب است → fast-forward
اگر local و remote هر دو تغییر دارند → divergent branches
```

### دستورات اصلی

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



#  سؤال های سناریومحور Git Pull، Fast-Forward، Merge و Rebase با جواب

---

## 1. سناریو: لوکال فقط عقب است

روی branch شخصی خودت کار می‌کنی. هنوز هیچ commit لوکالی نداده‌ای. یکی از هم‌تیمی‌ها روی remote یک commit جدید push کرده. حالا می‌خواهی branch خودت را آپدیت کنی.

اگر `git pull` بزنی چه اتفاقی می‌افتد؟

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

وضعیت این است:

```txt
local:  A---B
remote: A---B---C
```

تو فقط از remote عقب هستی.

بهترین نوع update اینجا چیست؟

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

وضعیت این است:

```txt
local:  A---B---D
remote: A---B---C
```

تو هم commit داری، remote هم commit جدید دارد.

این وضعیت چه نامی دارد؟

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

روی branch شخصی برای یک Pull Request کار می‌کنی. می‌خواهی history تمیز و خطی بماند. remote branch اصلی هم آپدیت شده.

کدام دستور مناسب‌تر است؟

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

روی branch مشترک `develop` کار می‌کنی و چند نفر دیگر هم مستقیم روی همین branch commit می‌زنند. branch تو و remote هر دو تغییرات جدید دارند.

برای کمتر دردسر درست کردن برای بقیه، merge بهتر است یا rebase؟

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

می‌خواهی Git فقط وقتی pull کند که branch تو فقط عقب‌تر از remote باشد. اگر branchها divergent بودند، می‌خواهی خطا بدهد و کاری نکند.

کدام دستور مناسب است؟

### جواب

دستور مناسب:

```bash
git pull --ff-only
```

یعنی:

> فقط اگر fast-forward ممکن بود pull کن؛ اگر branchها divergent بودند، خطا بده.

این گزینه برای جلوگیری از merge ناخواسته خیلی خوب است.

---

## 7. سناریو: تنظیم دائمی fast-forward only

می‌خواهی این رفتار را برای همیشه تنظیم کنی که `git pull` فقط در حالت fast-forward مجاز باشد.

کدام config را می‌زنی؟

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

بعد از اجرای `git pull` این خطا را می‌بینی:

```txt
fatal: Need to specify how to reconcile divergent branches.
```

این خطا از نظر مفهومی یعنی چه؟

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

روی branch شخصی rebase انجام داده‌ای. بعد از آن وقتی `git push` می‌زنی، Git push را reject می‌کند.

چرا این اتفاق افتاده؟

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

همان سناریوی قبل: branch شخصی است و مطمئنی کسی دیگر روی آن کار نمی‌کند. بعد از rebase باید push کنی.

کدام دستور امن‌تر از `git push --force` است؟

### جواب

دستور بهتر و امن‌تر:

```bash
git push --force-with-lease
```

این از `--force` امن‌تر است، چون اگر کسی قبل از تو روی remote چیزی push کرده باشد، Git اجازه نمی‌دهد کار او را overwrite کنی.

---

## 11. سناریو: conflict وسط rebase

وسط rebase conflict پیش آمده. فایل‌های conflictدار را باز کرده‌ای و conflictها را حل کرده‌ای.

بعد از حل conflict باید چه دو دستور اصلی بزنی؟

### جواب

اول فایل‌های حل‌شده را stage می‌کنی:

```bash
git add .
```

بعد rebase را ادامه می‌دهی:

```bash
git rebase --continue
```

یعنی:

```bash
git add .
git rebase --continue
```

---

## 12. سناریو: لغو کامل rebase

وسط rebase conflict پیش آمده ولی فهمیدی مسیر اشتباه بوده و می‌خواهی کل rebase را لغو کنی.

کدام دستور را می‌زنی؟

### جواب

```bash
git rebase --abort
```

این دستور rebase را لغو می‌کند و branch را به وضعیت قبل از شروع rebase برمی‌گرداند.

---

## 13. سناریو: pull همیشه با rebase باشد

روی branch شخصی کار می‌کنی. دوست داری هر بار `git pull` می‌زنی، به جای merge، rebase انجام شود.

کدام config مناسب است؟

### جواب

```bash
git config --global pull.rebase true
```

بعد از این، `git pull` به صورت پیش‌فرض مثل این رفتار می‌کند:

```bash
git pull --rebase
```

این تنظیم برای کسانی که بیشتر روی branchهای شخصی و Pull Request کار می‌کنند مفید است.

---

## 14. سناریو: تیم history واقعی mergeها را می‌خواهد

روی پروژه‌ای کار می‌کنی که history واقعی mergeها برای تیم مهم است. نمی‌خواهند commitها بازنویسی شوند.

برای `git pull` کدام تنظیم پیش‌فرض منطقی‌تر است؟

### جواب

تنظیم پیش‌فرض روی merge منطقی‌تر است:

```bash
git config --global pull.rebase false
```

یعنی `git pull` به صورت پیش‌فرض merge انجام می‌دهد، نه rebase.

این انتخاب برای branchهای مشترک تیمی امن‌تر است.

---

## 15. سناریو: نتیجه merge

وضعیت این است:

```txt
A---B---D
     \---C
```

بعد از merge چه چیزی به history اضافه می‌شود؟

### جواب

بعد از merge یک **merge commit** جدید ساخته می‌شود.

مثلاً:

```txt
A---B---D---M
     \---C---/
```

Commit `M` نشان می‌دهد که دو مسیر جداشده دوباره با هم ترکیب شده‌اند.

---

## 16. سناریو: نتیجه rebase

وضعیت این است:

```txt
local:  A---B---D
remote: A---B---C
```

بعد از rebase، history تقریباً به چه شکلی می‌شود؟

### جواب

بعد از rebase، commit لوکال تو روی آخرین commit ریموت دوباره اعمال می‌شود:

```txt
A---B---C---D'
```

Commit `D` به `D'` تبدیل می‌شود، چون Git آن را دوباره ساخته است.

---

## 17. سناریو: تغییر hash بعد از rebase

بعد از rebase می‌بینی commit قبلی تو که hash مشخصی داشت، حالا hash جدید دارد.

آیا این طبیعی است؟ چرا؟

### جواب

بله، طبیعی است.

چون rebase commitهای تو را دوباره روی base جدید می‌سازد. وقتی parent commit تغییر کند، hash commit هم تغییر می‌کند.

یعنی حتی اگر محتوای تغییرات یکی باشد، commit جدید محسوب می‌شود.

---

## 18. سناریو: گرفتن remote بدون ترکیب

می‌خواهی فقط آخرین تغییرات remote را ببینی یا بگیری، ولی هنوز نمی‌خواهی با branch فعلی‌ات ترکیب شوند.

کدام دستور را می‌زنی؟

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

روی branch `feature/login` هستی و می‌خواهی آن را روی آخرین وضعیت `origin/main` بنشانی، بدون اینکه pull مستقیم بزنی.

کدام دو دستور مناسب است؟

### جواب

اول تغییرات remote را می‌گیری:

```bash
git fetch origin
```

بعد branch فعلی را روی `origin/main` rebase می‌کنی:

```bash
git rebase origin/main
```

پس کاملش می‌شود:

```bash
git fetch origin
git rebase origin/main
```

---

## 20. سناریو: توصیه اشتباه درباره rebase

هم‌تیمی‌ات می‌گوید:

> برای اینکه history تمیز باشد، همیشه روی branch مشترک تیمی rebase بزن.

آیا این توصیه همیشه درست است؟ چرا؟

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

قانون عملی:

```txt
branch شخصی  -> rebase
branch مشترک -> merge
احتیاط کامل  -> ff-only
```

```
```

