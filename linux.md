<div dir="rtl" align="right">

# آنچه از لینوکس باید بدانم

راهنمای کاربردی لینوکس برای یک **Fullstack Developer**

این داکیومنت برای کسی نوشته شده که با توسعه فرانت‌اند، بک‌اند، دیتابیس، API، Docker، Git، SSH، سرور و دیپلوی سروکار دارد. هدف این نیست که ادمین لینوکس شوید؛ هدف این است که در محیط توسعه و سرور production گم نشوید، بتوانید خطاها را پیدا کنید، لاگ‌ها را بخوانید، سرویس‌ها را بررسی کنید و با اعتمادبه‌نفس کارهای روزمره را انجام دهید.

---

<details>
<summary><strong>📑 فهرست مطالب</strong> — <em>کلیک برای باز / بسته کردن</em></summary>

| # | بخش |
| ---: | --- |
| 1 | [1. مسیرها و ساختار فایل‌سیستم لینوکس](#1-مسیرها-و-ساختار-فایلسیستم-لینوکس) |
| 2 | [2. جابه‌جایی در ترمینال](#2-جابهجایی-در-ترمینال) |
| 3 | [3. دیدن فایل‌ها و پوشه‌ها](#3-دیدن-فایلها-و-پوشهها) |
| 4 | [4. ساخت، کپی، انتقال و حذف فایل‌ها](#4-ساخت،-کپی،-انتقال-و-حذف-فایلها) |
| 5 | [5. خواندن فایل‌ها](#5-خواندن-فایلها) |
| 6 | [6. جستجو داخل فایل‌ها](#6-جستجو-داخل-فایلها) |
| 7 | [7. پیدا کردن فایل‌ها](#7-پیدا-کردن-فایلها) |
| 8 | [8. ویرایش فایل‌ها در ترمینال](#8-ویرایش-فایلها-در-ترمینال) |
| 9 | [9. مجوزها و مالکیت فایل‌ها](#9-مجوزها-و-مالکیت-فایلها) |
| 10 | [10. sudo و کاربر root](#10-sudo-و-کاربر-root) |
| 11 | [11. مدیریت پکیج‌ها](#11-مدیریت-پکیجها) |
| 12 | [12. پروسس‌ها و منابع سیستم](#12-پروسسها-و-منابع-سیستم) |
| 13 | [13. فضای دیسک و حافظه](#13-فضای-دیسک-و-حافظه) |
| 14 | [14. متغیرهای محیطی](#14-متغیرهای-محیطی) |
| 15 | [15. Pipe و Redirect](#15-pipe-و-redirect) |
| 16 | [16. کار با archive و فایل‌های فشرده](#16-کار-با-archive-و-فایلهای-فشرده) |
| 17 | [17. SSH برای اتصال به سرور](#17-ssh-برای-اتصال-به-سرور) |
| 18 | [18. rsync برای sync فایل‌ها](#18-rsync-برای-sync-فایلها) |
| 19 | [19. شبکه و پورت‌ها](#19-شبکه-و-پورتها) |
| 20 | [20. DNS و بررسی دامنه](#20-dns-و-بررسی-دامنه) |
| 21 | [21. systemd و مدیریت سرویس‌ها](#21-systemd-و-مدیریت-سرویسها) |
| 22 | [22. خواندن لاگ سرویس‌ها با journalctl](#22-خواندن-لاگ-سرویسها-با-journalctl) |
| 23 | [23. Nginx برای فول‌استک دولوپر](#23-nginx-برای-فولاستک-دولوپر) |
| 24 | [24. Git در لینوکس](#24-git-در-لینوکس) |
| 25 | [25. Node.js و npm روی لینوکس](#25-nodejs-و-npm-روی-لینوکس) |
| 26 | [26. PM2 برای اجرای Node.js در سرور](#26-pm2-برای-اجرای-nodejs-در-سرور) |
| 27 | [27. Docker برای فول‌استک دولوپر](#27-docker-برای-فولاستک-دولوپر) |
| 28 | [28. Docker Compose](#28-docker-compose) |
| 29 | [29. PostgreSQL و MySQL از ترمینال](#29-postgresql-و-mysql-از-ترمینال) |
| 30 | [30. Cron Job](#30-cron-job) |
| 31 | [31. Firewall ساده با UFW](#31-firewall-ساده-با-ufw) |
| 32 | [32. مانیتورینگ سریع production issue](#32-مانیتورینگ-سریع-production-issue) |
| 33 | [33. کامندهای خیلی مهم برای دیباگ سریع](#33-کامندهای-خیلی-مهم-برای-دیباگ-سریع) |
| 34 | [34. چند alias مفید](#34-چند-alias-مفید) |
| 35 | [35. اسکریپت ساده deploy](#35-اسکریپت-ساده-deploy) |
| 36 | [36. امنیت پایه‌ای که باید بدانید](#36-امنیت-پایهای-که-باید-بدانید) |
| 37 | [37. چک‌لیست روزمره فول‌استک دولوپر](#37-چکلیست-روزمره-فولاستک-دولوپر) |
| 38 | [38. تمرین پیشنهادی](#38-تمرین-پیشنهادی) |
| 39 | [39. حداقل کامندهایی که باید حفظ باشید](#39-حداقل-کامندهایی-که-باید-حفظ-باشید) |
| 40 | [40. جمع‌بندی](#40-جمعبندی) |

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم)

</details>

---

## 1. مسیرها و ساختار فایل‌سیستم لینوکس

<details>
<summary>1. مسیرها و ساختار فایل‌سیستم لینوکس</summary>

در لینوکس همه چیز از ریشه شروع می‌شود:

```bash
/
```

مسیرهای مهم:

| مسیر | کاربرد |
|---|---|
| `/home` | فایل‌های کاربران |
| `/root` | خانه کاربر root |
| `/etc` | فایل‌های کانفیگ سیستم و سرویس‌ها |
| `/var` | لاگ‌ها، کش‌ها، دیتای متغیر |
| `/var/log` | لاگ‌های سیستم و سرویس‌ها |
| `/usr` | برنامه‌ها و کتابخانه‌های نصب‌شده |
| `/bin` و `/sbin` | کامندهای پایه سیستم |
| `/tmp` | فایل‌های موقت |
| `/opt` | نرم‌افزارهای third-party |
| `/srv` | داده‌های سرویس‌ها، گاهی برای اپلیکیشن‌ها |

مثال:

```bash
cd /var/log
ls
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [بعدی →](#2-جابهجایی-در-ترمینال)

</div>


---

## 2. جابه‌جایی در ترمینال

<details>
<summary>2. جابه‌جایی در ترمینال</summary>

### دیدن مسیر فعلی

```bash
pwd
```

مثال خروجی:

```bash
/home/ubuntu/app
```

### رفتن به یک مسیر

```bash
cd /path/to/directory
```

مثال:

```bash
cd /var/www/my-app
```

### برگشتن به مسیر خانه

```bash
cd ~
```

### برگشتن یک پوشه عقب‌تر

```bash
cd ..
```

### برگشتن به مسیر قبلی

```bash
cd -
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#1-مسیرها-و-ساختار-فایلسیستم-لینوکس) · [بعدی →](#3-دیدن-فایلها-و-پوشهها)

</div>


---

## 3. دیدن فایل‌ها و پوشه‌ها

<details>
<summary>3. دیدن فایل‌ها و پوشه‌ها</summary>

### لیست ساده

```bash
ls
```

### لیست کامل با جزئیات

```bash
ls -la
```

خروجی نمونه:

```bash
drwxr-xr-x  5 ubuntu ubuntu 4096 Jun  8 10:20 .
drwxr-xr-x  3 ubuntu ubuntu 4096 Jun  8 09:50 ..
-rw-r--r--  1 ubuntu ubuntu  220 Jun  8 10:00 package.json
```

معنی بخش اول:

```bash
-rw-r--r--
```

یعنی:

- `-` فایل معمولی است
- `d` یعنی directory
- `r` یعنی read
- `w` یعنی write
- `x` یعنی execute

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#2-جابهجایی-در-ترمینال) · [بعدی →](#4-ساخت،-کپی،-انتقال-و-حذف-فایلها)

</div>


---

## 4. ساخت، کپی، انتقال و حذف فایل‌ها

<details>
<summary>4. ساخت، کپی، انتقال و حذف فایل‌ها</summary>

### ساخت پوشه

```bash
mkdir logs
```

ساخت مسیر چندمرحله‌ای:

```bash
mkdir -p apps/api/logs
```

### ساخت فایل خالی

```bash
touch .env
```

### کپی فایل

```bash
cp .env.example .env
```

### کپی پوشه

```bash
cp -r source-folder target-folder
```

### انتقال یا تغییر نام

```bash
mv old-name.txt new-name.txt
```

مثال انتقال:

```bash
mv build /var/www/my-app
```

### حذف فایل

```bash
rm file.txt
```

### حذف پوشه

```bash
rm -r folder-name
```

### حذف اجباری و خطرناک

```bash
rm -rf folder-name
```

> مراقب `rm -rf` باشید. اشتباه زدن مسیر می‌تواند کل پروژه یا حتی سیستم را حذف کند.

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#3-دیدن-فایلها-و-پوشهها) · [بعدی →](#5-خواندن-فایلها)

</div>


---

## 5. خواندن فایل‌ها

<details>
<summary>5. خواندن فایل‌ها</summary>

### نمایش کل فایل

```bash
cat package.json
```

### خواندن صفحه‌به‌صفحه

```bash
less app.log
```

در `less`:

| کلید | کاربرد |
|---|---|
| `q` | خروج |
| `/text` | جستجو |
| `n` | نتیجه بعدی |
| `Shift + G` | رفتن به آخر فایل |

### دیدن ابتدای فایل

```bash
head app.log
```

مثال با تعداد خط:

```bash
head -n 50 app.log
```

### دیدن انتهای فایل

```bash
tail app.log
```

### دنبال کردن لاگ زنده

```bash
tail -f app.log
```

برای production خیلی مهم است:

```bash
tail -f /var/log/nginx/error.log
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#4-ساخت،-کپی،-انتقال-و-حذف-فایلها) · [بعدی →](#6-جستجو-داخل-فایلها)

</div>


---

## 6. جستجو داخل فایل‌ها

<details>
<summary>6. جستجو داخل فایل‌ها</summary>

### جستجو با grep

```bash
grep "ERROR" app.log
```

### جستجوی case-insensitive

```bash
grep -i "error" app.log
```

### نمایش شماره خط

```bash
grep -n "DATABASE_URL" .env
```

### جستجوی recursive در کل پروژه

```bash
grep -R "TODO" .
```

### جستجو با حذف node_modules

```bash
grep -R "API_URL" . --exclude-dir=node_modules
```

مثال واقعی:

```bash
grep -R "NEXT_PUBLIC_API_URL" . --exclude-dir=node_modules --exclude-dir=.next
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#5-خواندن-فایلها) · [بعدی →](#7-پیدا-کردن-فایلها)

</div>


---

## 7. پیدا کردن فایل‌ها

<details>
<summary>7. پیدا کردن فایل‌ها</summary>

### پیدا کردن فایل با نام

```bash
find . -name "package.json"
```

### پیدا کردن فایل‌های env

```bash
find . -name ".env*"
```

### پیدا کردن فایل‌های بزرگ

```bash
find . -type f -size +100M
```

### پیدا کردن فایل‌های تغییرکرده در ۲۴ ساعت گذشته

```bash
find . -type f -mtime -1
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#6-جستجو-داخل-فایلها) · [بعدی →](#8-ویرایش-فایلها-در-ترمینال)

</div>


---

## 8. ویرایش فایل‌ها در ترمینال

<details>
<summary>8. ویرایش فایل‌ها در ترمینال</summary>

### nano ساده‌تر است

```bash
nano .env
```

کلیدهای مهم nano:

| کلید | کاربرد |
|---|---|
| `Ctrl + O` | ذخیره |
| `Enter` | تایید ذخیره |
| `Ctrl + X` | خروج |

### vim حرفه‌ای‌تر است

```bash
vim nginx.conf
```

حداقل چیزهایی که باید از vim بدانید:

| دستور | کاربرد |
|---|---|
| `i` | ورود به حالت ویرایش |
| `Esc` | خروج از حالت ویرایش |
| `:w` | ذخیره |
| `:q` | خروج |
| `:wq` | ذخیره و خروج |
| `:q!` | خروج بدون ذخیره |

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#7-پیدا-کردن-فایلها) · [بعدی →](#9-مجوزها-و-مالکیت-فایلها)

</div>


---

## 9. مجوزها و مالکیت فایل‌ها

<details>
<summary>9. مجوزها و مالکیت فایل‌ها</summary>

### دیدن مجوزها

```bash
ls -la
```

نمونه:

```bash
-rwxr-xr-x 1 ubuntu ubuntu deploy.sh
```

### قابل اجرا کردن یک فایل

```bash
chmod +x deploy.sh
```

بعد اجرا:

```bash
./deploy.sh
```

### تغییر مجوز عددی

```bash
chmod 644 file.txt
chmod 755 script.sh
```

معنی رایج:

| مجوز | کاربرد |
|---|---|
| `644` | فایل عادی: owner می‌نویسد، بقیه فقط می‌خوانند |
| `755` | اسکریپت یا پوشه قابل اجرا |
| `600` | فایل حساس مثل private key |

### تغییر مالک فایل

```bash
sudo chown ubuntu:ubuntu app.log
```

برای کل پوشه:

```bash
sudo chown -R ubuntu:ubuntu /var/www/my-app
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#8-ویرایش-فایلها-در-ترمینال) · [بعدی →](#10-sudo-و-کاربر-root)

</div>


---

## 10. sudo و کاربر root

<details>
<summary>10. sudo و کاربر root</summary>

بعضی کارها نیاز به دسترسی admin دارند:

```bash
sudo systemctl restart nginx
```

ورود به shell با دسترسی root:

```bash
sudo -i
```

برگشت:

```bash
exit
```

> با root فقط وقتی کار کنید که لازم است. اشتباه در root گران تمام می‌شود.

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#9-مجوزها-و-مالکیت-فایلها) · [بعدی →](#11-مدیریت-پکیجها)

</div>


---

## 11. مدیریت پکیج‌ها

<details>
<summary>11. مدیریت پکیج‌ها</summary>

روی Ubuntu/Debian معمولاً از `apt` استفاده می‌شود.

### آپدیت لیست پکیج‌ها

```bash
sudo apt update
```

### آپگرید پکیج‌ها

```bash
sudo apt upgrade
```

### نصب پکیج

```bash
sudo apt install nginx
```

### حذف پکیج

```bash
sudo apt remove nginx
```

### دیدن نسخه برنامه

```bash
node -v
npm -v
git --version
nginx -v
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#10-sudo-و-کاربر-root) · [بعدی →](#12-پروسسها-و-منابع-سیستم)

</div>


---

## 12. پروسس‌ها و منابع سیستم

<details>
<summary>12. پروسس‌ها و منابع سیستم</summary>

### دیدن پروسس‌ها

```bash
ps aux
```

### جستجوی یک پروسس

```bash
ps aux | grep node
```

### مانیتور زنده سیستم

```bash
top
```

اگر نصب باشد، `htop` بهتر است:

```bash
htop
```

### کشتن پروسس با PID

```bash
kill 12345
```

اگر بسته نشد:

```bash
kill -9 12345
```

### کشتن پروسس بر اساس نام

```bash
pkill node
```

> در production با `pkill` خیلی محتاط باشید. ممکن است چند سرویس Node.js را با هم ببندید.

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#11-مدیریت-پکیجها) · [بعدی →](#13-فضای-دیسک-و-حافظه)

</div>


---

## 13. فضای دیسک و حافظه

<details>
<summary>13. فضای دیسک و حافظه</summary>

### دیدن فضای دیسک

```bash
df -h
```

### دیدن حجم پوشه‌ها

```bash
du -sh *
```

### پیدا کردن پوشه‌های سنگین

```bash
du -h --max-depth=1 | sort -h
```

### دیدن RAM

```bash
free -h
```

مثال کاربردی:

```bash
du -sh node_modules .next dist build logs
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#12-پروسسها-و-منابع-سیستم) · [بعدی →](#14-متغیرهای-محیطی)

</div>


---

## 14. متغیرهای محیطی

<details>
<summary>14. متغیرهای محیطی</summary>

### دیدن envهای فعلی

```bash
env
```

### جستجوی یک env

```bash
env | grep NODE_ENV
```

### تعریف موقت env

```bash
export NODE_ENV=production
```

### اجرای دستور با env خاص

```bash
NODE_ENV=production npm start
```

### فایل `.env`

نمونه:

```env
NODE_ENV=production
PORT=3000
DATABASE_URL=postgresql://user:pass@localhost:5432/app
JWT_SECRET=super-secret
```

> فایل `.env` را معمولاً نباید commit کنید.

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#13-فضای-دیسک-و-حافظه) · [بعدی →](#15-pipe-و-redirect)

</div>


---

## 15. Pipe و Redirect

<details>
<summary>15. Pipe و Redirect</summary>

### ارسال خروجی یک دستور به دستور بعدی

```bash
ps aux | grep node
```

### ذخیره خروجی در فایل

```bash
ls -la > files.txt
```

### اضافه کردن خروجی به آخر فایل

```bash
echo "Deploy started" >> deploy.log
```

### ذخیره خطاها همزمان با خروجی

```bash
npm run build > build.log 2>&1
```

### دیدن خروجی و ذخیره همزمان

```bash
npm run build 2>&1 | tee build.log
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#14-متغیرهای-محیطی) · [بعدی →](#16-کار-با-archive-و-فایلهای-فشرده)

</div>


---

## 16. کار با archive و فایل‌های فشرده

<details>
<summary>16. کار با archive و فایل‌های فشرده</summary>

### فشرده‌سازی با tar.gz

```bash
tar -czvf app.tar.gz app/
```

### باز کردن tar.gz

```bash
tar -xzvf app.tar.gz
```

### zip کردن

```bash
zip -r app.zip app/
```

### unzip کردن

```bash
unzip app.zip
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#15-pipe-و-redirect) · [بعدی →](#17-ssh-برای-اتصال-به-سرور)

</div>


---

## 17. SSH برای اتصال به سرور

<details>
<summary>17. SSH برای اتصال به سرور</summary>

### اتصال ساده

```bash
ssh ubuntu@SERVER_IP
```

### اتصال با private key

```bash
ssh -i ~/.ssh/my-key.pem ubuntu@SERVER_IP
```

### تنظیم permission کلید

```bash
chmod 600 ~/.ssh/my-key.pem
```

### کپی فایل به سرور با scp

```bash
scp ./app.tar.gz ubuntu@SERVER_IP:/home/ubuntu/
```

### کپی فایل از سرور به سیستم خودتان

```bash
scp ubuntu@SERVER_IP:/var/log/nginx/error.log ./error.log
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#16-کار-با-archive-و-فایلهای-فشرده) · [بعدی →](#18-rsync-برای-sync-فایلها)

</div>


---

## 18. rsync برای sync فایل‌ها

<details>
<summary>18. rsync برای sync فایل‌ها</summary>

`rsync` برای deploy ساده یا sync فایل‌ها بهتر از `scp` است.

```bash
rsync -avz ./dist/ ubuntu@SERVER_IP:/var/www/my-app/
```

حذف فایل‌هایی که در source دیگر وجود ندارند:

```bash
rsync -avz --delete ./dist/ ubuntu@SERVER_IP:/var/www/my-app/
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#17-ssh-برای-اتصال-به-سرور) · [بعدی →](#19-شبکه-و-پورتها)

</div>


---

## 19. شبکه و پورت‌ها

<details>
<summary>19. شبکه و پورت‌ها</summary>

### دیدن IP سیستم

```bash
ip addr
```

### تست اتصال اینترنت یا سرور

```bash
ping google.com
```

### تست HTTP با curl

```bash
curl http://localhost:3000
```

### دیدن response header

```bash
curl -I https://example.com
```

### ارسال درخواست POST

```bash
curl -X POST http://localhost:3000/api/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"secret"}'
```

### دیدن پورت‌های باز

```bash
ss -tulpn
```

### بررسی اینکه چه چیزی روی پورت 3000 اجراست

```bash
sudo lsof -i :3000
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#18-rsync-برای-sync-فایلها) · [بعدی →](#20-dns-و-بررسی-دامنه)

</div>


---

## 20. DNS و بررسی دامنه

<details>
<summary>20. DNS و بررسی دامنه</summary>

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

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#19-شبکه-و-پورتها) · [بعدی →](#21-systemd-و-مدیریت-سرویسها)

</div>


---

## 21. systemd و مدیریت سرویس‌ها

<details>
<summary>21. systemd و مدیریت سرویس‌ها</summary>

بسیاری از سرویس‌ها در لینوکس با `systemd` مدیریت می‌شوند.

### وضعیت سرویس

```bash
sudo systemctl status nginx
```

### شروع سرویس

```bash
sudo systemctl start nginx
```

### توقف سرویس

```bash
sudo systemctl stop nginx
```

### ری‌استارت سرویس

```bash
sudo systemctl restart nginx
```

### reload بدون قطع کامل

```bash
sudo systemctl reload nginx
```

### فعال کردن اجرا بعد از reboot

```bash
sudo systemctl enable nginx
```

### غیرفعال کردن اجرا بعد از reboot

```bash
sudo systemctl disable nginx
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#20-dns-و-بررسی-دامنه) · [بعدی →](#22-خواندن-لاگ-سرویسها-با-journalctl)

</div>


---

## 22. خواندن لاگ سرویس‌ها با journalctl

<details>
<summary>22. خواندن لاگ سرویس‌ها با journalctl</summary>

### لاگ یک سرویس

```bash
sudo journalctl -u nginx
```

### لاگ زنده

```bash
sudo journalctl -u nginx -f
```

### لاگ از boot فعلی

```bash
sudo journalctl -u nginx -b
```

### دیدن آخرین ۱۰۰ خط

```bash
sudo journalctl -u nginx -n 100
```

مثال برای سرویس Node.js:

```bash
sudo journalctl -u my-api -f
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#21-systemd-و-مدیریت-سرویسها) · [بعدی →](#23-nginx-برای-فولاستک-دولوپر)

</div>


---

## 23. Nginx برای فول‌استک دولوپر

<details>
<summary>23. Nginx برای فول‌استک دولوپر</summary>

Nginx معمولاً برای reverse proxy، static files و SSL termination استفاده می‌شود.

### تست کانفیگ Nginx

```bash
sudo nginx -t
```

### reload کردن Nginx

```bash
sudo systemctl reload nginx
```

### مسیرهای مهم Nginx

```bash
/etc/nginx/nginx.conf
/etc/nginx/sites-available/
/etc/nginx/sites-enabled/
/var/log/nginx/access.log
/var/log/nginx/error.log
```

### نمونه reverse proxy برای Node.js

```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

بعد از تغییر کانفیگ:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#22-خواندن-لاگ-سرویسها-با-journalctl) · [بعدی →](#24-git-در-لینوکس)

</div>


---

## 24. Git در لینوکس

<details>
<summary>24. Git در لینوکس</summary>

### وضعیت repo

```bash
git status
```

### گرفتن آخرین تغییرات

```bash
git pull
```

### دیدن branchها

```bash
git branch
```

### تغییر branch

```bash
git checkout main
```

یا جدیدتر:

```bash
git switch main
```

### دیدن remoteها

```bash
git remote -v
```

### دیدن لاگ خلاصه

```bash
git log --oneline --graph --decorate --all
```

### stash کردن تغییرات

```bash
git stash
```

### برگرداندن stash

```bash
git stash pop
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#23-nginx-برای-فولاستک-دولوپر) · [بعدی →](#25-nodejs-و-npm-روی-لینوکس)

</div>


---

## 25. Node.js و npm روی لینوکس

<details>
<summary>25. Node.js و npm روی لینوکس</summary>

### دیدن نسخه‌ها

```bash
node -v
npm -v
pnpm -v
```

### نصب dependency

```bash
npm install
```

یا:

```bash
pnpm install
```

### build گرفتن

```bash
npm run build
```

یا:

```bash
pnpm build
```

### اجرای production

```bash
npm start
```

### مشکل رایج permission در npm

اگر با `EACCES` مواجه شدید، کورکورانه `sudo npm install -g` نزنید. بهتر است Node را با `nvm` مدیریت کنید.

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#24-git-در-لینوکس) · [بعدی →](#26-pm2-برای-اجرای-nodejs-در-سرور)

</div>


---

## 26. PM2 برای اجرای Node.js در سرور

<details>
<summary>26. PM2 برای اجرای Node.js در سرور</summary>

PM2 برای نگه داشتن اپلیکیشن Node.js در background استفاده می‌شود.

### نصب

```bash
npm install -g pm2
```

### اجرای اپ

```bash
pm2 start npm --name my-app -- start
```

### لیست پروسس‌ها

```bash
pm2 list
```

### دیدن لاگ‌ها

```bash
pm2 logs my-app
```

### ری‌استارت

```bash
pm2 restart my-app
```

### توقف

```bash
pm2 stop my-app
```

### اجرای خودکار بعد از reboot

```bash
pm2 startup
pm2 save
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#25-nodejs-و-npm-روی-لینوکس) · [بعدی →](#27-docker-برای-فولاستک-دولوپر)

</div>


---

## 27. Docker برای فول‌استک دولوپر

<details>
<summary>27. Docker برای فول‌استک دولوپر</summary>

### دیدن containerها

```bash
docker ps
```

همه containerها:

```bash
docker ps -a
```

### دیدن imageها

```bash
docker images
```

### اجرای container

```bash
docker run -p 3000:3000 my-app
```

### توقف container

```bash
docker stop CONTAINER_ID
```

### حذف container

```bash
docker rm CONTAINER_ID
```

### حذف image

```bash
docker rmi IMAGE_ID
```

### دیدن لاگ container

```bash
docker logs CONTAINER_ID
```

لاگ زنده:

```bash
docker logs -f CONTAINER_ID
```

### ورود به shell داخل container

```bash
docker exec -it CONTAINER_ID sh
```

یا اگر bash موجود باشد:

```bash
docker exec -it CONTAINER_ID bash
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#26-pm2-برای-اجرای-nodejs-در-سرور) · [بعدی →](#28-docker-compose)

</div>


---

## 28. Docker Compose

<details>
<summary>28. Docker Compose</summary>

### بالا آوردن سرویس‌ها

```bash
docker compose up
```

در background:

```bash
docker compose up -d
```

### توقف سرویس‌ها

```bash
docker compose down
```

### build مجدد

```bash
docker compose up -d --build
```

### دیدن لاگ‌ها

```bash
docker compose logs
```

لاگ یک سرویس:

```bash
docker compose logs -f api
```

### اجرای دستور داخل سرویس

```bash
docker compose exec api sh
```

مثال برای دیتابیس:

```bash
docker compose exec postgres psql -U postgres
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#27-docker-برای-فولاستک-دولوپر) · [بعدی →](#29-postgresql-و-mysql-از-ترمینال)

</div>


---

## 29. PostgreSQL و MySQL از ترمینال

<details>
<summary>29. PostgreSQL و MySQL از ترمینال</summary>

### اتصال به PostgreSQL

```bash
psql -h localhost -U postgres -d mydb
```

### چند دستور مهم psql

```sql
\l
\c mydb
\dt
\d users
\q
```

### گرفتن backup از PostgreSQL

```bash
pg_dump -h localhost -U postgres mydb > backup.sql
```

### restore کردن PostgreSQL

```bash
psql -h localhost -U postgres mydb < backup.sql
```

### اتصال به MySQL

```bash
mysql -h localhost -u root -p
```

### backup از MySQL

```bash
mysqldump -u root -p mydb > backup.sql
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#28-docker-compose) · [بعدی →](#30-cron-job)

</div>


---

## 30. Cron Job

<details>
<summary>30. Cron Job</summary>

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

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#29-postgresql-و-mysql-از-ترمینال) · [بعدی →](#31-firewall-ساده-با-ufw)

</div>


---

## 31. Firewall ساده با UFW

<details>
<summary>31. Firewall ساده با UFW</summary>

### وضعیت firewall

```bash
sudo ufw status
```

### اجازه SSH

```bash
sudo ufw allow ssh
```

### اجازه HTTP و HTTPS

```bash
sudo ufw allow 80
sudo ufw allow 443
```

### فعال کردن firewall

```bash
sudo ufw enable
```

### حذف rule

```bash
sudo ufw delete allow 3000
```

> قبل از فعال کردن firewall مطمئن شوید SSH باز است، وگرنه ممکن است دسترسی به سرور را از دست بدهید.

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#30-cron-job) · [بعدی →](#32-مانیتورینگ-سریع-production-issue)

</div>


---

## 32. مانیتورینگ سریع production issue

<details>
<summary>32. مانیتورینگ سریع production issue</summary>

وقتی اپلیکیشن روی سرور مشکل دارد، این ترتیب معمولاً خوب جواب می‌دهد:

### 1. وضعیت سرویس

```bash
sudo systemctl status my-api
```

یا اگر PM2 است:

```bash
pm2 list
```

### 2. لاگ سرویس

```bash
sudo journalctl -u my-api -n 100
```

یا:

```bash
pm2 logs my-api
```

### 3. بررسی پورت

```bash
sudo lsof -i :3000
```

### 4. تست local

```bash
curl http://localhost:3000/health
```

### 5. تست از بیرون با دامنه

```bash
curl -I https://example.com
```

### 6. بررسی Nginx

```bash
sudo nginx -t
sudo systemctl status nginx
sudo tail -f /var/log/nginx/error.log
```

### 7. بررسی منابع

```bash
df -h
free -h
top
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#31-firewall-ساده-با-ufw) · [بعدی →](#33-کامندهای-خیلی-مهم-برای-دیباگ-سریع)

</div>


---

## 33. کامندهای خیلی مهم برای دیباگ سریع

<details>
<summary>33. کامندهای خیلی مهم برای دیباگ سریع</summary>

### چه چیزی روی این پورت است؟

```bash
sudo lsof -i :3000
```

### چرا build fail شده؟

```bash
npm run build 2>&1 | tee build.log
```

بعد:

```bash
grep -i "error" build.log
```

### آیا API بالا است؟

```bash
curl -I http://localhost:3000
```

### آیا DNS درست است؟

```bash
dig example.com
```

### آیا SSL کار می‌کند؟

```bash
curl -Iv https://example.com
```

### آخرین لاگ‌های سرویس چیست؟

```bash
sudo journalctl -u my-api -n 100 --no-pager
```

### فضای سرور پر شده؟

```bash
df -h
```

### چه پوشه‌ای فضا را خورده؟

```bash
du -h --max-depth=1 /var | sort -h
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#32-مانیتورینگ-سریع-production-issue) · [بعدی →](#34-چند-alias-مفید)

</div>


---

## 34. چند alias مفید

<details>
<summary>34. چند alias مفید</summary>

می‌توانید aliasها را در فایل زیر بگذارید:

```bash
nano ~/.bashrc
```

نمونه:

```bash
alias ll='ls -la'
alias gs='git status'
alias gp='git pull'
alias dps='docker ps'
alias dcup='docker compose up -d'
alias dclogs='docker compose logs -f'
alias ports='sudo ss -tulpn'
```

بعد از تغییر:

```bash
source ~/.bashrc
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#33-کامندهای-خیلی-مهم-برای-دیباگ-سریع) · [بعدی →](#35-اسکریپت-ساده-deploy)

</div>


---

## 35. اسکریپت ساده deploy

<details>
<summary>35. اسکریپت ساده deploy</summary>

نمونه `deploy.sh`:

```bash
#!/usr/bin/env bash
set -e

echo "Pull latest code"
git pull

echo "Install dependencies"
pnpm install

echo "Build app"
pnpm build

echo "Restart service"
pm2 restart my-app

echo "Deploy completed"
```

قابل اجرا کردن:

```bash
chmod +x deploy.sh
```

اجرا:

```bash
./deploy.sh
```

نکته مهم:

```bash
set -e
```

باعث می‌شود اگر یک دستور fail شد، اسکریپت ادامه پیدا نکند.

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#34-چند-alias-مفید) · [بعدی →](#36-امنیت-پایهای-که-باید-بدانید)

</div>


---

## 36. امنیت پایه‌ای که باید بدانید

<details>
<summary>36. امنیت پایه‌ای که باید بدانید</summary>

### فایل‌های حساس را public نکنید

مراقب این فایل‌ها باشید:

```bash
.env
id_rsa
*.pem
backup.sql
```

### permission کلید SSH

```bash
chmod 600 ~/.ssh/id_rsa
```

### لاگ‌ها ممکن است secret داشته باشند

هیچ‌وقت کورکورانه کل لاگ production را share نکنید.

### از root برای اپلیکیشن استفاده نکنید

اپلیکیشن را با کاربر معمولی اجرا کنید، نه root.

### پورت دیتابیس را عمومی باز نکنید

PostgreSQL/MySQL معمولاً نباید مستقیماً روی اینترنت باز باشند.

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#35-اسکریپت-ساده-deploy) · [بعدی →](#37-چکلیست-روزمره-فولاستک-دولوپر)

</div>


---

## 37. چک‌لیست روزمره فول‌استک دولوپر

<details>
<summary>37. چک‌لیست روزمره فول‌استک دولوپر</summary>

### روی پروژه local/server

```bash
pwd
ls -la
git status
git pull
pnpm install
pnpm build
pnpm start
```

### روی سرور

```bash
df -h
free -h
sudo systemctl status nginx
sudo nginx -t
pm2 list
pm2 logs my-app
curl -I http://localhost:3000
curl -I https://example.com
```

### برای Docker

```bash
docker ps
docker compose ps
docker compose logs -f
docker compose up -d --build
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#36-امنیت-پایهای-که-باید-بدانید) · [بعدی →](#38-تمرین-پیشنهادی)

</div>


---

## 38. تمرین پیشنهادی

<details>
<summary>38. تمرین پیشنهادی</summary>

برای مسلط شدن، این تمرین‌ها را انجام دهید:

1. یک پوشه بسازید.
2. داخل آن چند فایل بسازید.
3. با `grep` داخل فایل‌ها جستجو کنید.
4. یک اسکریپت bash ساده بنویسید.
5. آن را با `chmod +x` قابل اجرا کنید.
6. یک اپ Node.js را روی پورت 3000 اجرا کنید.
7. با `curl` آن را تست کنید.
8. با `lsof` ببینید چه چیزی روی پورت 3000 است.
9. لاگ ساختگی بسازید و با `tail -f` آن را دنبال کنید.
10. همین اپ را با Docker اجرا کنید.

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#37-چکلیست-روزمره-فولاستک-دولوپر) · [بعدی →](#39-حداقل-کامندهایی-که-باید-حفظ-باشید)

</div>


---

## 39. حداقل کامندهایی که باید حفظ باشید

<details>
<summary>39. حداقل کامندهایی که باید حفظ باشید</summary>

```bash
pwd
cd
ls -la
mkdir -p
touch
cp
mv
rm -rf
cat
less
head
tail -f
grep -R
find
chmod
chown
sudo
apt update
apt install
ps aux
top
df -h
du -sh
free -h
env
export
curl
ping
ss -tulpn
lsof -i
ssh
scp
rsync
git status
git pull
systemctl status
journalctl -u
docker ps
docker logs
docker compose up -d
docker compose logs -f
```

---

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#38-تمرین-پیشنهادی) · [بعدی →](#40-جمعبندی)

</div>


---

## 40. جمع‌بندی

<details>
<summary>40. جمع‌بندی</summary>

برای یک Fullstack Developer، لینوکس یعنی توانایی انجام این کارها:

- حرکت در فایل‌سیستم
- خواندن و ویرایش فایل‌های کانفیگ
- فهمیدن permissionها
- اجرای سرویس‌ها
- خواندن لاگ‌ها
- دیباگ پورت و شبکه
- اتصال به سرور با SSH
- مدیریت Node.js، Docker و دیتابیس
- فهمیدن مشکل production بدون حدس زدن

لازم نیست همه چیز را حفظ باشید. مهم این است که بدانید چه ابزاری برای چه مشکلی وجود دارد و در لحظه بحران، مسیر دیباگ را گم نکنید.

</details>


<div align="center">

[↑ بالا](#آنچه-از-لینوکس-باید-بدانم) · [← قبلی](#39-حداقل-کامندهایی-که-باید-حفظ-باشید)

</div>


</div>
