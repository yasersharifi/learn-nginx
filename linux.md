# آنچه از لینوکس باید بدانم

راهنمای کاربردی لینوکس برای یک **Fullstack Developer**

این داکیومنت برای کسی نوشته شده که با توسعه فرانت‌اند، بک‌اند، دیتابیس، API، Docker، Git، SSH، سرور و دیپلوی سروکار دارد. هدف این نیست که ادمین لینوکس شوید؛ هدف این است که در محیط توسعه و سرور production گم نشوید، بتوانید خطاها را پیدا کنید، لاگ‌ها را بخوانید، سرویس‌ها را بررسی کنید و با اعتمادبه‌نفس کارهای روزمره را انجام دهید.

---

## 1. مسیرها و ساختار فایل‌سیستم لینوکس

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

## 2. جابه‌جایی در ترمینال

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

## 3. دیدن فایل‌ها و پوشه‌ها

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

## 4. ساخت، کپی، انتقال و حذف فایل‌ها

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

## 5. خواندن فایل‌ها

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

## 6. جستجو داخل فایل‌ها

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

## 7. پیدا کردن فایل‌ها

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

## 8. ویرایش فایل‌ها در ترمینال

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

## 9. مجوزها و مالکیت فایل‌ها

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

## 10. sudo و کاربر root

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

## 11. مدیریت پکیج‌ها

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

## 12. پروسس‌ها و منابع سیستم

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

## 13. فضای دیسک و حافظه

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

## 14. متغیرهای محیطی

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

## 15. Pipe و Redirect

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

## 16. کار با archive و فایل‌های فشرده

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

## 17. SSH برای اتصال به سرور

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

## 18. rsync برای sync فایل‌ها

`rsync` برای deploy ساده یا sync فایل‌ها بهتر از `scp` است.

```bash
rsync -avz ./dist/ ubuntu@SERVER_IP:/var/www/my-app/
```

حذف فایل‌هایی که در source دیگر وجود ندارند:

```bash
rsync -avz --delete ./dist/ ubuntu@SERVER_IP:/var/www/my-app/
```

---

## 19. شبکه و پورت‌ها

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

## 20. DNS و بررسی دامنه

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

## 21. systemd و مدیریت سرویس‌ها

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

## 22. خواندن لاگ سرویس‌ها با journalctl

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

## 23. Nginx برای فول‌استک دولوپر

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

## 24. Git در لینوکس

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

## 25. Node.js و npm روی لینوکس

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

## 26. PM2 برای اجرای Node.js در سرور

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

## 27. Docker برای فول‌استک دولوپر

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

## 28. Docker Compose

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

## 29. PostgreSQL و MySQL از ترمینال

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

## 30. Cron Job

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

## 31. Firewall ساده با UFW

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

## 32. مانیتورینگ سریع production issue

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

## 33. کامندهای خیلی مهم برای دیباگ سریع

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

## 34. چند alias مفید

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

## 35. اسکریپت ساده deploy

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

## 36. امنیت پایه‌ای که باید بدانید

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

## 37. چک‌لیست روزمره فول‌استک دولوپر

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

## 38. تمرین پیشنهادی

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

## 39. حداقل کامندهایی که باید حفظ باشید

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

## 40. جمع‌بندی

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
