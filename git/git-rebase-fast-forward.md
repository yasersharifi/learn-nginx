<div dir="rtl" align="right">

# راهنمای ساده Git Pull، Fast-Forward، Merge و Rebase

این داکیومنت برای توضیح ساده و عملی چند مفهوم مهم در Git نوشته شده است:

- `git pull`
- `fast-forward`
- `merge`
- `rebase`
- خطای `divergent branches`
- انتخاب بهترین روش برای کار روزمره

---

<details>
<summary><strong>📑 فهرست مطالب</strong> — <em>کلیک برای باز / بسته کردن</em></summary>

| # | بخش |
| ---: | --- |
| 1 | [1. git pull چیست؟](#1-git-pull-چیست؟) |
| 2 | [2. Fast-Forward یعنی چی؟](#2-fast-forward-یعنی-چی؟) |
| 3 | [3. وقتی Fast-Forward ممکن نیست](#3-وقتی-fast-forward-ممکن-نیست) |
| 4 | [4. Merge چیست؟](#4-merge-چیست؟) |
| 5 | [5. Rebase چیست؟](#5-rebase-چیست؟) |
| 6 | [6. خطای divergent branches یعنی چی؟](#6-خطای-divergent-branches-یعنی-چی؟) |
| 7 | [7. تنظیم پیش‌فرض Git برای pull](#7-تنظیم-پیشفرض-git-برای-pull) |
| 8 | [8. کدام گزینه بهتر است؟](#8-کدام-گزینه-بهتر-است؟) |
| 9 | [9. دستورهای کاربردی روزمره](#9-دستورهای-کاربردی-روزمره) |
| 10 | [10. اگر هنگام Rebase conflict پیش آمد](#10-اگر-هنگام-rebase-conflict-پیش-آمد) |
| 11 | [11. اگر بعد از Rebase نتوانستی Push کنی](#11-اگر-بعد-از-rebase-نتوانستی-push-کنی) |
| 12 | [12. جمع‌بندی سریع](#12-جمعبندی-سریع) |

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase)

</details>

---

## 1. git pull چیست؟

<details>
<summary>1. git pull چیست؟</summary>

دستور `git pull` یعنی:

> آخرین تغییرات branch ریموت را بگیر و با branch لوکال من یکی کن.

در واقع `git pull` ترکیبی از دو کار است:

```bash
git fetch
git merge
```

یا اگر با rebase استفاده شود:

```bash
git fetch
git rebase
```

پس وقتی می‌زنی:

```bash
git pull
```

Git اول تغییرات remote را می‌گیرد، بعد باید تصمیم بگیرد چطور آن‌ها را با تغییرات local یکی کند.

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [بعدی →](#2-fast-forward-یعنی-چی؟)

</div>


---

## 2. Fast-Forward یعنی چی؟

<details>
<summary>2. Fast-Forward یعنی چی؟</summary>

`fast-forward` ساده‌ترین حالت آپدیت شدن branch است.

فرض کن branch لوکال تو اینجاست:

```txt
local:  A---B
```

ولی روی remote یک commit جدید آمده:

```txt
remote: A---B---C
```

تو روی لوکال commit جدیدی نداده‌ای. فقط عقب‌تر از remote هستی.

در این حالت Git فقط اشاره‌گر branch تو را جلو می‌برد:

```txt
local:  A---B---C
```

این می‌شود **fast-forward**.

یعنی:

> Git هیچ commit جدیدی نمی‌سازد؛ فقط branch را جلو می‌برد.

### ویژگی‌های Fast-Forward

- history تمیز می‌ماند.
- merge commit ساخته نمی‌شود.
- معمولاً conflict ندارد.
- فقط وقتی ممکن است که branch لوکال از remote جدا نشده باشد.

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#1-git-pull-چیست؟) · [بعدی →](#3-وقتی-fast-forward-ممکن-نیست)

</div>


---

## 3. وقتی Fast-Forward ممکن نیست

<details>
<summary>3. وقتی Fast-Forward ممکن نیست</summary>

گاهی هم تو روی branch لوکال commit داده‌ای، هم remote commit جدید دارد.

مثلاً:

```txt
local:  A---B---D
remote: A---B---C
```

اینجا branchها از هم جدا شده‌اند.

به این حالت می‌گویند:

```txt
divergent branches
```

یعنی:

> لوکال و ریموت هر دو تغییراتی دارند که طرف مقابل ندارد.

در این حالت Git نمی‌تواند فقط branch را جلو ببرد. پس باید یکی از این دو کار را انجام دهد:

1. `merge`
2. `rebase`

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#2-fast-forward-یعنی-چی؟) · [بعدی →](#4-merge-چیست؟)

</div>


---

## 4. Merge چیست؟

<details>
<summary>4. Merge چیست؟</summary>

`merge` یعنی Git دو مسیر جداشده را با یک commit جدید یکی کند.

مثلاً:

```txt
local:  A---B---D
remote: A---B---C
```

اگر merge انجام شود:

```bash
git pull --no-rebase
```

یا:

```bash
git merge origin/main
```

نتیجه چیزی شبیه این می‌شود:

```txt
A---B---D---M
     \---C---/
```

اینجا `M` یک **merge commit** است.

یعنی Git می‌گوید:

> دو مسیر جدا بودند؛ من آن‌ها را با یک commit جدید ترکیب کردم.

### مزیت Merge

- history واقعی پروژه حفظ می‌شود.
- برای branchهای مشترک و تیمی امن‌تر است.
- commitهای قبلی بازنویسی نمی‌شوند.

### عیب Merge

- history ممکن است شلوغ‌تر شود.
- merge commitهای زیاد می‌توانند خواندن تاریخچه را سخت‌تر کنند.

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#3-وقتی-fast-forward-ممکن-نیست) · [بعدی →](#5-rebase-چیست؟)

</div>


---

## 5. Rebase چیست؟

<details>
<summary>5. Rebase چیست؟</summary>

`rebase` یعنی Git commitهای لوکال تو را برمی‌دارد و دوباره روی آخرین وضعیت remote می‌چیند.

همان حالت قبل را در نظر بگیر:

```txt
local:  A---B---D
remote: A---B---C
```

اگر rebase بزنی:

```bash
git pull --rebase
```

Git commit `D` را موقتاً برمی‌دارد، branch را تا `C` جلو می‌برد، بعد `D` را دوباره روی `C` اعمال می‌کند:

```txt
A---B---C---D'
```

دقت کن `D` تبدیل به `D'` شده است.

چرا؟

چون Git یک commit جدید ساخته است. محتوای آن ممکن است همان باشد، ولی hash آن عوض شده است.

### مزیت Rebase

- history خطی و تمیز می‌ماند.
- برای Pull Requestها معمولاً خواناتر است.
- commitهای فیچر روی آخرین نسخه‌ی branch اصلی قرار می‌گیرند.

### عیب Rebase

- history را بازنویسی می‌کند.
- روی branchهای مشترک ممکن است برای بقیه دردسر درست کند.
- بعد از rebase ممکن است برای push نیاز به `--force-with-lease` داشته باشی.

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#4-merge-چیست؟) · [بعدی →](#6-خطای-divergent-branches-یعنی-چی؟)

</div>


---

## 6. خطای divergent branches یعنی چی؟

<details>
<summary>6. خطای divergent branches یعنی چی؟</summary>

ممکن است موقع `git pull` این خطا را ببینی:

```txt
hint: You have divergent branches and need to specify how to reconcile them.
fatal: Need to specify how to reconcile divergent branches.
```

یعنی:

> هم branch لوکال تو commit جدید دارد، هم branch ریموت. Git نمی‌داند باید merge کند یا rebase.

برای حل آن باید یکی از این‌ها را انتخاب کنی.

### راه‌حل با Rebase

```bash
git pull --rebase
```

یا دقیق‌تر:

```bash
git fetch origin
git rebase origin/main
```

اگر branch اصلی پروژه `master` است:

```bash
git fetch origin
git rebase origin/master
```

### راه‌حل با Merge

```bash
git pull --no-rebase
```

یا:

```bash
git fetch origin
git merge origin/main
```

### راه‌حل با Fast-Forward Only

```bash
git pull --ff-only
```

این یعنی:

> فقط اگر fast-forward ممکن بود pull کن. اگر branchها جدا شده‌اند، خطا بده.

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#5-rebase-چیست؟) · [بعدی →](#7-تنظیم-پیشفرض-git-برای-pull)

</div>


---

## 7. تنظیم پیش‌فرض Git برای pull

<details>
<summary>7. تنظیم پیش‌فرض Git برای pull</summary>

Git از تو می‌خواهد مشخص کنی که پیش‌فرض pull چه باشد.

### پیش‌فرض روی Merge

```bash
git config --global pull.rebase false
```

یعنی `git pull` به صورت پیش‌فرض merge کند.

### پیش‌فرض روی Rebase

```bash
git config --global pull.rebase true
```

یعنی `git pull` به صورت پیش‌فرض rebase کند.

### پیش‌فرض روی Fast-Forward Only

```bash
git config --global pull.ff only
```

یعنی فقط وقتی pull انجام شود که fast-forward ممکن باشد.

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#6-خطای-divergent-branches-یعنی-چی؟) · [بعدی →](#8-کدام-گزینه-بهتر-است؟)

</div>


---

## 8. کدام گزینه بهتر است؟

<details>
<summary>8. کدام گزینه بهتر است؟</summary>

جواب بستگی به نوع کار دارد.

### برای branch شخصی

اگر فقط خودت روی branch کار می‌کنی، معمولاً این بهتر است:

```bash
git pull --rebase
```

یا تنظیم دائمی:

```bash
git config --global pull.rebase true
```

چون history تمیزتر و خطی‌تر می‌ماند.

---

### برای branch مشترک تیمی

اگر چند نفر روی یک branch کار می‌کنند، معمولاً merge امن‌تر است:

```bash
git pull --no-rebase
```

چون rebase تاریخچه را بازنویسی می‌کند و ممکن است برای بقیه مشکل بسازد.

---

### برای جلوگیری از اشتباه

اگر نمی‌خواهی Git خودش تصمیم بگیرد و می‌خواهی فقط حالت امن fast-forward را قبول کند:

```bash
git config --global pull.ff only
```

در این حالت اگر branchها divergent باشند، Git خطا می‌دهد و تو باید آگاهانه تصمیم بگیری merge می‌خواهی یا rebase.

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#7-تنظیم-پیشفرض-git-برای-pull) · [بعدی →](#9-دستورهای-کاربردی-روزمره)

</div>


---

## 9. دستورهای کاربردی روزمره

<details>
<summary>9. دستورهای کاربردی روزمره</summary>

### دیدن branch فعلی

```bash
git branch --show-current
```

### دیدن branchهای remote

```bash
git branch -r
```

### گرفتن تغییرات remote بدون ترکیب کردن

```bash
git fetch origin
```

### rebase کردن branch فعلی روی main

```bash
git rebase origin/main
```

### rebase کردن branch فعلی روی master

```bash
git rebase origin/master
```

### pull با rebase

```bash
git pull --rebase
```

### pull با merge

```bash
git pull --no-rebase
```

### pull فقط در حالت fast-forward

```bash
git pull --ff-only
```

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#8-کدام-گزینه-بهتر-است؟) · [بعدی →](#10-اگر-هنگام-rebase-conflict-پیش-آمد)

</div>


---

## 10. اگر هنگام Rebase conflict پیش آمد

<details>
<summary>10. اگر هنگام Rebase conflict پیش آمد</summary>

وقتی conflict رخ می‌دهد، Git rebase را متوقف می‌کند.

اول فایل‌های conflictدار را باز کن و مشکل را حل کن.

بعد:

```bash
git add .
git rebase --continue
```

اگر خواستی کل rebase را لغو کنی:

```bash
git rebase --abort
```

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#9-دستورهای-کاربردی-روزمره) · [بعدی →](#11-اگر-بعد-از-rebase-نتوانستی-push-کنی)

</div>


---

## 11. اگر بعد از Rebase نتوانستی Push کنی

<details>
<summary>11. اگر بعد از Rebase نتوانستی Push کنی</summary>

چون rebase تاریخچه را بازنویسی می‌کند، ممکن است push معمولی رد شود.

در این حالت، برای branch شخصی خودت از این استفاده کن:

```bash
git push --force-with-lease
```

از این کمتر استفاده کن:

```bash
git push --force
```

چون `--force-with-lease` امن‌تر است. اگر کسی قبل از تو چیزی push کرده باشد، جلوی overwrite شدن کار او را می‌گیرد.

---

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#10-اگر-هنگام-rebase-conflict-پیش-آمد) · [بعدی →](#12-جمعبندی-سریع)

</div>


---

## 12. جمع‌بندی سریع

<details>
<summary>12. جمع‌بندی سریع</summary>

```txt
fast-forward = فقط جلو بردن branch، بدون commit جدید
merge        = ترکیب دو مسیر با یک merge commit
rebase       = چیدن commitهای تو روی آخرین نسخه remote
ff-only      = فقط fast-forward را قبول کن؛ اگر نشد، خطا بده
```

پیشنهاد عملی:

```txt
branch شخصی      -> rebase
branch مشترک     -> merge
احتیاط کامل      -> ff-only
```

برای اکثر کارهای شخصی و Pull Requestها:

```bash
git pull --rebase
```

برای جلوگیری از merge ناخواسته:

```bash
git pull --ff-only
```

</details>


<div align="center">

[↑ بالا](#راهنمای-ساده-git-pull،-fast-forward،-merge-و-rebase) · [← قبلی](#11-اگر-بعد-از-rebase-نتوانستی-push-کنی)

</div>


</div>
