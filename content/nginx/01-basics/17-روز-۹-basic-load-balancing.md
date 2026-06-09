---
title: "روز ۹: basic load balancing"
description: "روز ۹: basic load balancing"
---

# روز ۹: basic load balancing

سه app ساده اجرا کن.

`server.js` را طوری تغییر بده که port و instance را نشان دهد:

```js
const express = require("express");

const app = express();
const port = process.env.PORT || 3000;
const instance = process.env.INSTANCE || "app";

app.get("/", (req, res) => {
  res.json({
    message: "Hello",
    instance,
    port,
  });
});

app.listen(port, () => {
  console.log(`${instance} listening on port ${port}`);
});
```

اجرا:

```bash
PORT=3001 INSTANCE=app-1 node server.js
PORT=3002 INSTANCE=app-2 node server.js
PORT=3003 INSTANCE=app-3 node server.js
```

Nginx config:

```nginx
upstream node_apps {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
    server 127.0.0.1:3003;
}

server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://node_apps;

        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

تست:

```bash
for i in {1..10}; do curl -s http://localhost; echo; done
```

باید ببینی درخواست‌ها بین appها پخش می‌شوند.

---

## الگوریتم‌های ساده load balancing

### Round-robin

پیش‌فرض Nginx است:

```nginx
upstream node_apps {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
```

### Weighted

```nginx
upstream node_apps {
    server 127.0.0.1:3001 weight=3;
    server 127.0.0.1:3002 weight=1;
}
```

یعنی app اول تقریباً سهم بیشتری از requestها می‌گیرد.

### least_conn

```nginx
upstream node_apps {
    least_conn;

    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
}
```

درخواست جدید را به backendی می‌دهد که connection فعال کمتری دارد.

---
