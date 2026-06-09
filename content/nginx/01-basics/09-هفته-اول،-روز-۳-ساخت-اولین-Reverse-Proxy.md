---
title: "هفته اول، روز ۳: ساخت اولین Reverse Proxy"
description: "هفته اول، روز ۳: ساخت اولین Reverse Proxy"
---

# هفته اول، روز ۳: ساخت اولین Reverse Proxy

حالا یک app ساده Node.js بساز.

```bash
mkdir ~/nginx-node-lab
cd ~/nginx-node-lab
npm init -y
npm install express
```

فایل `server.js`:

```js
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.json({
    message: "Hello from Node app",
    host: req.headers.host,
    forwardedFor: req.headers["x-forwarded-for"],
    realIp: req.headers["x-real-ip"],
  });
});

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

app.listen(3000, () => {
  console.log("App listening on port 3000");
});
```

اجرا:

```bash
node server.js
```

حالا Nginx config:

```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000;
    }
}
```

تست:

```bash
curl http://localhost
```

باید JSON از Node ببینی.

---
