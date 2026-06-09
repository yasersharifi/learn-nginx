<div dir="rtl" align="right">

# HEAD در Git چیست؟

`HEAD` در Git یعنی:

> اشاره‌گر به جایی که الان در repository روی آن ایستاده‌ای.

در حالت عادی، `HEAD` به آخرین commit روی branch فعلی اشاره می‌کند.

مثلاً اگر روی branch `main` باشی:

```txt
main: A---B---C
              ^
             HEAD
```

یعنی وضعیت فعلی پروژه روی commit `C` است.

---

<details>
<summary><strong>📑 فهرست مطالب</strong> — <em>کلیک برای باز / بسته کردن</em></summary>

| # | بخش |
| ---: | --- |
| 1 | [1. HEAD دقیقاً به چه چیزی اشاره می‌کند؟](#1-head-دقیقاً-به-چه-چیزی-اشاره-میکند؟) |
| 2 | [2. دیدن وضعیت HEAD](#2-دیدن-وضعیت-head) |
| 3 | [3. HEAD~1 یعنی چی؟](#3-head1-یعنی-چی؟) |
| 4 | [4. HEAD^ یعنی چی؟](#4-head-یعنی-چی؟) |
| 5 | [5. Detached HEAD چیست؟](#5-detached-head-چیست؟) |
| 6 | [6. خطر Detached HEAD](#6-خطر-detached-head) |
| 7 | [7. برگشتن از Detached HEAD به branch](#7-برگشتن-از-detached-head-به-branch) |
| 8 | [8. کاربردهای رایج HEAD](#8-کاربردهای-رایج-head) |
| 9 | [9. استفاده از HEAD با reset](#9-استفاده-از-head-با-reset) |
| 10 | [10. تفاوت reset soft، mixed و hard](#10-تفاوت-reset-soft،-mixed-و-hard) |
| 11 | [11. جمع‌بندی سریع](#11-جمعبندی-سریع) |
| 12 | [12. پیشنهاد عملی](#12-پیشنهاد-عملی) |

[↑ بالا](#head-در-git-چیست؟)

</details>

---

## 1. HEAD دقیقاً به چه چیزی اشاره می‌کند؟

<details>
<summary>1. HEAD دقیقاً به چه چیزی اشاره می‌کند؟</summary>

در حالت معمول، `HEAD` مستقیم به commit اشاره نمی‌کند؛ بلکه به branch فعلی اشاره می‌کند، و آن branch به آخرین commit خودش اشاره دارد.

مثلاً:

```txt
HEAD -> main -> C
```

یعنی:

- `HEAD` به branch `main` اشاره می‌کند.
- `main` به commit آخر خودش اشاره می‌کند.
- commit آخر در این مثال `C` است.

وقتی commit جدید می‌زنی:

```bash
git commit -m "add nginx config"
```

branch جلو می‌رود و `HEAD` هم همراه آن جلو می‌رود.

قبل:

```txt
main: A---B---C
              ^
             HEAD
```

بعد:

```txt
main: A---B---C---D
                  ^
                 HEAD
```

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [بعدی →](#2-دیدن-وضعیت-head)

</div>


---

## 2. دیدن وضعیت HEAD

<details>
<summary>2. دیدن وضعیت HEAD</summary>

برای دیدن وضعیت فعلی repository:

```bash
git status
```

اگر ببینی:

```txt
On branch main
```

یعنی `HEAD` الان روی branch `main` است.

برای دیدن آخرین commit که `HEAD` به آن اشاره دارد:

```bash
git show HEAD
```

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#1-head-دقیقاً-به-چه-چیزی-اشاره-میکند؟) · [بعدی →](#3-head1-یعنی-چی؟)

</div>


---

## 3. HEAD~1 یعنی چی؟

<details>
<summary>3. HEAD~1 یعنی چی؟</summary>

`HEAD~1` یعنی:

> یک commit قبل از HEAD

مثلاً:

```txt
A---B---C---D
            ^
           HEAD
```

در این حالت:

```txt
HEAD    = D
HEAD~1  = C
HEAD~2  = B
HEAD~3  = A
```

مثال:

```bash
git show HEAD
```

آخرین commit را نشان می‌دهد.

```bash
git show HEAD~1
```

commit قبلی را نشان می‌دهد.

```bash
git show HEAD~2
```

دو commit قبل‌تر را نشان می‌دهد.

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#2-دیدن-وضعیت-head) · [بعدی →](#4-head-یعنی-چی؟)

</div>


---

## 4. HEAD^ یعنی چی؟

<details>
<summary>4. HEAD^ یعنی چی؟</summary>

`HEAD^` هم معمولاً یعنی parent قبلی `HEAD`.

در تاریخچه ساده، این دو تقریباً یکی هستند:

```bash
HEAD^
HEAD~1
```

هر دو یعنی یک commit قبل.

اما در merge commit فرق می‌کنند.

مثلاً:

```txt
A---B---D---M
     \---C---/
```

اینجا `M` یک merge commit است و دو parent دارد.

```bash
HEAD^1
```

یعنی parent اول.

```bash
HEAD^2
```

یعنی parent دوم.

برای کارهای روزمره، معمولاً `HEAD~1` واضح‌تر و کاربردی‌تر است.

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#3-head1-یعنی-چی؟) · [بعدی →](#5-detached-head-چیست؟)

</div>


---

## 5. Detached HEAD چیست؟

<details>
<summary>5. Detached HEAD چیست؟</summary>

`detached HEAD` یعنی:

> `HEAD` دیگر به branch وصل نیست؛ مستقیم روی یک commit خاص ایستاده است.

مثلاً اگر بزنی:

```bash
git checkout a1b2c3d
```

یا:

```bash
git switch --detach a1b2c3d
```

Git ممکن است بگوید:

```txt
You are in 'detached HEAD' state
```

یعنی الان روی یک commit خاص هستی، نه روی یک branch.

مثلاً:

```txt
main: A---B---C---D
          ^
         HEAD
```

اینجا `HEAD` مستقیم روی commit `B` است.

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#4-head-یعنی-چی؟) · [بعدی →](#6-خطر-detached-head)

</div>


---

## 6. خطر Detached HEAD

<details>
<summary>6. خطر Detached HEAD</summary>

اگر در حالت detached HEAD تغییر بدهی و commit بزنی، آن commit روی هیچ branch مشخصی نیست.

یعنی ممکن است بعداً راحت گم شود.

برای جلوگیری از این مشکل، اگر تغییر مهمی دادی، سریع یک branch بساز:

```bash
git switch -c my-new-branch
```

یا با دستور قدیمی‌تر:

```bash
git checkout -b my-new-branch
```

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#5-detached-head-چیست؟) · [بعدی →](#7-برگشتن-از-detached-head-به-branch)

</div>


---

## 7. برگشتن از Detached HEAD به branch

<details>
<summary>7. برگشتن از Detached HEAD به branch</summary>

برای برگشتن به branch اصلی:

```bash
git switch main
```

یا اگر branch اصلی پروژه `master` است:

```bash
git switch master
```

با دستور قدیمی‌تر:

```bash
git checkout main
```

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#6-خطر-detached-head) · [بعدی →](#8-کاربردهای-رایج-head)

</div>


---

## 8. کاربردهای رایج HEAD

<details>
<summary>8. کاربردهای رایج HEAD</summary>

### دیدن آخرین commit

```bash
git show HEAD
```

### دیدن commit قبلی

```bash
git show HEAD~1
```

### دیدن چند commit آخر

```bash
git log --oneline
```

### برگشت دادن یک فایل به وضعیت آخرین commit

```bash
git restore file.txt
```

یا روش قدیمی‌تر:

```bash
git checkout HEAD -- file.txt
```

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#7-برگشتن-از-detached-head-به-branch) · [بعدی →](#9-استفاده-از-head-با-reset)

</div>


---

## 9. استفاده از HEAD با reset

<details>
<summary>9. استفاده از HEAD با reset</summary>

`HEAD` خیلی وقت‌ها با `git reset` استفاده می‌شود.

### حذف آخرین commit ولی نگه داشتن تغییرات در stage

```bash
git reset --soft HEAD~1
```

کاربرد:

> آخرین commit حذف می‌شود، اما تغییرات همچنان staged می‌مانند.

---

### حذف آخرین commit و نگه داشتن تغییرات در working directory

```bash
git reset --mixed HEAD~1
```

یا ساده‌تر:

```bash
git reset HEAD~1
```

کاربرد:

> آخرین commit حذف می‌شود، تغییرات باقی می‌مانند، ولی staged نیستند.

---

### حذف آخرین commit و پاک کردن تغییرات

```bash
git reset --hard HEAD~1
```

هشدار:

> این دستور تغییرات را واقعاً پاک می‌کند. با احتیاط استفاده کن.

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#8-کاربردهای-رایج-head) · [بعدی →](#10-تفاوت-reset-soft،-mixed-و-hard)

</div>


---

## 10. تفاوت reset soft، mixed و hard

<details>
<summary>10. تفاوت reset soft، mixed و hard</summary>

```txt
--soft   = commit حذف می‌شود، تغییرات staged می‌مانند
--mixed  = commit حذف می‌شود، تغییرات unstaged می‌شوند
--hard   = commit و تغییرات هر دو پاک می‌شوند
```

مثلاً اگر آخرین commit اشتباه بوده ولی کد را می‌خواهی نگه داری:

```bash
git reset --soft HEAD~1
```

اگر commit اشتباه بوده و می‌خواهی تغییرات را دوباره بررسی کنی:

```bash
git reset HEAD~1
```

اگر commit و تغییرات هر دو اشتباه بوده‌اند و می‌خواهی کامل حذفشان کنی:

```bash
git reset --hard HEAD~1
```

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#9-استفاده-از-head-با-reset) · [بعدی →](#11-جمعبندی-سریع)

</div>


---

## 11. جمع‌بندی سریع

<details>
<summary>11. جمع‌بندی سریع</summary>

```txt
HEAD          = جایی که الان در Git ایستاده‌ای
HEAD~1        = یک commit قبل از HEAD
HEAD~2        = دو commit قبل از HEAD
HEAD^         = parent قبلی HEAD
HEAD^1        = parent اول، مخصوصاً در merge commit
HEAD^2        = parent دوم، مخصوصاً در merge commit
detached HEAD = وقتی HEAD مستقیم روی commit است، نه روی branch
```

---

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#10-تفاوت-reset-soft،-mixed-و-hard) · [بعدی →](#12-پیشنهاد-عملی)

</div>


---

## 12. پیشنهاد عملی

<details>
<summary>12. پیشنهاد عملی</summary>

برای کار روزمره این‌ها را بلد باشی کافی است:

```bash
git status
git show HEAD
git show HEAD~1
git log --oneline
git reset --soft HEAD~1
git reset HEAD~1
git reset --hard HEAD~1
```

مهم‌ترین نکته:

> `HEAD` یعنی نقطه‌ای که الان Git وضعیت فعلی پروژه را از آن حساب می‌کند.

</details>


<div align="center">

[↑ بالا](#head-در-git-چیست؟) · [← قبلی](#11-جمعبندی-سریع)

</div>


</div>
