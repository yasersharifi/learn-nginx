<div dir="rtl" align="right">

# سؤال‌های سناریومحور Git Pull، Fast-Forward، Merge و Rebase

**۲۰ سناریو با جواب** — Pull · Rebase · Merge · ff-only

---

> [!NOTE]
> **خلاصه سریع**
>
> - `git pull` یعنی fetch + ترکیب تغییرات remote با local.
> - اگر local فقط عقب باشد، fast-forward انجام می‌شود.
> - اگر local و remote هر دو commit جدید داشته باشند، branchها divergent شده‌اند.
> - در divergent branches باید بین merge و rebase انتخاب کنیم.
> - merge تاریخچه واقعی را حفظ می‌کند ولی ممکن است history را شلوغ کند.
> - rebase history را خطی و تمیز می‌کند ولی commitها را بازنویسی می‌کند.
> - ff-only فقط fast-forward را قبول می‌کند و در حالت divergent خطا می‌دهد.

### جدول مقایسه‌ای

| مفهوم | یعنی چی؟ | commit جدید می‌سازد؟ | بهترین کاربرد |
| --- | --- | :---: | --- |
| **Fast-forward** | فقط branch جلو می‌رود | نه | وقتی local فقط عقب است |
| **Merge** | دو مسیر با merge commit یکی می‌شوند | بله | branch مشترک تیمی |
| **Rebase** | commitهای local روی remote دوباره چیده می‌شوند | بله، با hash جدید | branch شخصی / PR |
| **ff-only** | فقط fast-forward را قبول می‌کند | نه | جلوگیری از merge ناخواسته |

> [!IMPORTANT]
> **قانون تصمیم‌گیری**
>
> - اگر **branch شخصی** است → `rebase`
> - اگر **branch مشترک تیمی** است → `merge`
> - اگر **نمی‌خواهی Git تصمیم بگیرد** → `ff-only`
> - اگر **local فقط عقب است** → fast-forward
> - اگر **local و remote هر دو تغییر دارند** → divergent branches

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

## فهرست سؤالات

| # | سناریو |
| ---: | --- |
| 1 | [لوکال فقط عقب است](#user-content-1-سناریو-لوکال-فقط-عقب-است) |
| 2 | [انتخاب بهترین update](#user-content-2-سناریو-انتخاب-بهترین-update) |
| 3 | [local و remote هر دو تغییر دارند](#user-content-3-سناریو-local-و-remote-هر-دو-تغییر-دارند) |
| 4 | [branch شخصی برای Pull Request](#user-content-4-سناریو-branch-شخصی-برای-pull-request) |
| 5 | [branch مشترک تیمی](#user-content-5-سناریو-branch-مشترک-تیمی) |
| 6 | [فقط fast-forward مجاز باشد](#user-content-6-سناریو-فقط-fast-forward-مجاز-باشد) |
| 7 | [تنظیم دائمی fast-forward only](#user-content-7-سناریو-تنظیم-دائمی-fast-forward-only) |
| 8 | [خطای divergent branches](#user-content-8-سناریو-خطای-divergent-branches) |
| 9 | [push بعد از rebase reject می‌شود](#user-content-9-سناریو-push-بعد-از-rebase-reject-میشود) |
| 10 | [push امن بعد از rebase](#user-content-10-سناریو-push-امن-بعد-از-rebase) |
| 11 | [conflict وسط rebase](#user-content-11-سناریو-conflict-وسط-rebase) |
| 12 | [لغو کامل rebase](#user-content-12-سناریو-لغو-کامل-rebase) |
| 13 | [pull همیشه با rebase باشد](#user-content-13-سناریو-pull-همیشه-با-rebase-باشد) |
| 14 | [تیم history واقعی mergeها را می‌خواهد](#user-content-14-سناریو-تیم-history-واقعی-mergeها-را-میخواهد) |
| 15 | [نتیجه merge](#user-content-15-سناریو-نتیجه-merge) |
| 16 | [نتیجه rebase](#user-content-16-سناریو-نتیجه-rebase) |
| 17 | [تغییر hash بعد از rebase](#user-content-17-سناریو-تغییر-hash-بعد-از-rebase) |
| 18 | [گرفتن remote بدون ترکیب](#user-content-18-سناریو-گرفتن-remote-بدون-ترکیب) |
| 19 | [rebase دستی روی origin/main](#user-content-19-سناریو-rebase-دستی-روی-originmain) |
| 20 | [توصیه اشتباه درباره rebase](#user-content-20-سناریو-توصیه-اشتباه-درباره-rebase) |

---

## 1. سناریو: لوکال فقط عقب است

<details>
<summary>روی branch شخصی کار می‌کنی، هنوز commit لوکالی نداده‌ای. هم‌تیمی روی remote push کرده. <code>git pull</code> چه می‌کند؟</summary>

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

</details>

---

## 2. سناریو: انتخاب بهترین update

<details>
<summary>وضعیت: local روی A---B و remote روی A---B---C. بهترین نوع update چیست؟</summary>

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

</details>

---

## 3. سناریو: local و remote هر دو تغییر دارند

<details>
<summary>local: A---B---D و remote: A---B---C. این وضعیت چه نامی دارد؟</summary>

### جواب

این وضعیت **divergent branches** است.

یعنی local و remote از یک نقطه مشترک جدا شده‌اند و هرکدام commitهایی دارند که دیگری ندارد.

```txt
local فقط D را دارد.
remote فقط C را دارد.
```

در این حالت fast-forward ممکن نیست و باید بین **merge** و **rebase** تصمیم بگیری.

</details>

---

## 4. سناریو: branch شخصی برای Pull Request

<details>
<summary>روی branch شخصی برای PR کار می‌کنی. می‌خواهی history تمیز بماند. remote هم آپدیت شده. کدام دستور مناسب‌تر است؟</summary>

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

</details>

---

## 5. سناریو: branch مشترک تیمی

<details>
<summary>روی branch مشترک <code>develop</code> کار می‌کنی. branch تو و remote هر دو تغییر دارند. merge بهتر است یا rebase؟</summary>

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

</details>

---

## 6. سناریو: فقط fast-forward مجاز باشد

<details>
<summary>می‌خواهی Git فقط وقتی pull کند که branch عقب‌تر از remote باشد. اگر divergent بودند، خطا بدهد.</summary>

### جواب

```bash
git pull --ff-only
```

> [!TIP]
> فقط اگر fast-forward ممکن بود pull کن؛ اگر branchها divergent بودند، خطا بده.

این گزینه برای جلوگیری از merge ناخواسته خیلی خوب است.

</details>

---

## 7. سناریو: تنظیم دائمی fast-forward only

<details>
<summary>می‌خواهی برای همیشه <code>git pull</code> فقط در حالت fast-forward مجاز باشد. کدام config؟</summary>

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

</details>

---

## 8. سناریو: خطای divergent branches

<details>
<summary>بعد از <code>git pull</code> این خطا را می‌بینی: <code>fatal: Need to specify how to reconcile divergent branches.</code></summary>

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

</details>

---

## 9. سناریو: push بعد از rebase reject می‌شود

<details>
<summary>روی branch شخصی rebase انجام داده‌ای. <code>git push</code> reject می‌شود. چرا؟</summary>

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

</details>

---

## 10. سناریو: push امن بعد از rebase

<details>
<summary>branch شخصی است و مطمئنی کسی دیگر روی آن کار نمی‌کند. کدام دستور امن‌تر از <code>git push --force</code> است؟</summary>

### جواب

```bash
git push --force-with-lease
```

این از `--force` امن‌تر است، چون اگر کسی قبل از تو روی remote چیزی push کرده باشد، Git اجازه نمی‌دهد کار او را overwrite کنی.

</details>

---

## 11. سناریو: conflict وسط rebase

<details>
<summary>وسط rebase conflict پیش آمده. conflictها را حل کرده‌ای. بعد از حل conflict چه دو دستور بزنی؟</summary>

### جواب

```bash
git add .
git rebase --continue
```

</details>

---

## 12. سناریو: لغو کامل rebase

<details>
<summary>وسط rebase conflict پیش آمده ولی می‌خواهی کل rebase را لغو کنی.</summary>

### جواب

```bash
git rebase --abort
```

این دستور rebase را لغو می‌کند و branch را به وضعیت قبل از شروع rebase برمی‌گرداند.

</details>

---

## 13. سناریو: pull همیشه با rebase باشد

<details>
<summary>می‌خواهی هر بار <code>git pull</code> به جای merge، rebase انجام شود. کدام config؟</summary>

### جواب

```bash
git config --global pull.rebase true
```

بعد از این، `git pull` به صورت پیش‌فرض مثل `git pull --rebase` رفتار می‌کند.

این تنظیم برای کسانی که بیشتر روی branchهای شخصی و Pull Request کار می‌کنند مفید است.

</details>

---

## 14. سناریو: تیم history واقعی mergeها را می‌خواهد

<details>
<summary>تیم history واقعی mergeها را می‌خواهد و نمی‌خواهد commitها بازنویسی شوند. تنظیم پیش‌فرض <code>git pull</code> چیست؟</summary>

### جواب

```bash
git config --global pull.rebase false
```

یعنی `git pull` به صورت پیش‌فرض merge انجام می‌دهد، نه rebase.

این انتخاب برای branchهای مشترک تیمی امن‌تر است.

</details>

---

## 15. سناریو: نتیجه merge

<details>
<summary>وضعیت: A---B---D و \---C. بعد از merge چه چیزی به history اضافه می‌شود؟</summary>

### جواب

بعد از merge یک **merge commit** جدید ساخته می‌شود.

```txt
A---B---D---M
     \---C---/
```

Commit `M` نشان می‌دهد که دو مسیر جداشده دوباره با هم ترکیب شده‌اند.

</details>

---

## 16. سناریو: نتیجه rebase

<details>
<summary>local: A---B---D و remote: A---B---C. بعد از rebase، history به چه شکلی می‌شود؟</summary>

### جواب

```txt
A---B---C---D'
```

Commit `D` به `D'` تبدیل می‌شود، چون Git آن را دوباره ساخته است.

</details>

---

## 17. سناریو: تغییر hash بعد از rebase

<details>
<summary>بعد از rebase commit قبلی hash جدید دارد. آیا طبیعی است؟ چرا؟</summary>

### جواب

بله، طبیعی است.

چون rebase commitهای تو را دوباره روی base جدید می‌سازد. وقتی parent commit تغییر کند، hash commit هم تغییر می‌کند.

یعنی حتی اگر محتوای تغییرات یکی باشد، commit جدید محسوب می‌شود.

</details>

---

## 18. سناریو: گرفتن remote بدون ترکیب

<details>
<summary>می‌خواهی فقط آخرین تغییرات remote را بگیری، بدون ترکیب با branch فعلی.</summary>

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

</details>

---

## 19. سناریو: rebase دستی روی origin/main

<details>
<summary>روی <code>feature/login</code> هستی و می‌خواهی آن را روی آخرین <code>origin/main</code> بنشانی، بدون pull مستقیم.</summary>

### جواب

```bash
git fetch origin
git rebase origin/main
```

</details>

---

## 20. سناریو: توصیه اشتباه درباره rebase

<details>
<summary>هم‌تیمی می‌گوید: «برای history تمیز، همیشه روی branch مشترک تیمی rebase بزن.» آیا درست است؟</summary>

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

> [!IMPORTANT]
> **قانون عملی**
>
> - branch شخصی → rebase
> - branch مشترک → merge
> - احتیاط کامل → ff-only

</details>

</div>
