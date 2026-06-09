---
title: "25. Node.js و npm روی لینوکس"
description: "25. Node.js و npm روی لینوکس"
---

# 25. Node.js و npm روی لینوکس

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
