---
title: "Node و PM2"
description: "npm، node، pm2 — اجرای اپ Node روی سرور"
---

# Node و PM2

## npm / node

| دستور | کاربرد |
| --- | --- |
| `node -v` | نسخه Node |
| `npm -v` | نسخه npm |
| `npm install` | نصب dependency |
| `npm ci` | نصب از lock (CI) |
| `npm run build` | build |
| `npm start` | اجرای production |
| `NODE_ENV=production npm start` | با env |
| `npx tsc --noEmit` | typecheck بدون نصب global |

## PM2

| دستور | کاربرد |
| --- | --- |
| `npm install -g pm2` | نصب |
| `pm2 start npm --name api -- start` | اجرای اپ |
| `pm2 start server.js --name api` | اجرای فایل |
| `pm2 list` | لیست |
| `pm2 logs api` | log |
| `pm2 logs api --lines 100` | ۱۰۰ خط |
| `pm2 restart api` | ری‌استارت |
| `pm2 stop api` | توقف |
| `pm2 delete api` | حذف از PM2 |
| `pm2 monit` | مانیتور زنده |
| `pm2 startup` | autostart بعد از boot |
| `pm2 save` | ذخیره لیست |

```bash
pm2 start ecosystem.config.js
pm2 reload api    # zero-downtime cluster
```
