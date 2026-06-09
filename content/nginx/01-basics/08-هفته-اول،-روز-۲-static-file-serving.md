---
title: "هفته اول، روز ۲: static file serving"
description: "هفته اول، روز ۲: static file serving"
---

# هفته اول، روز ۲: static file serving

حالا باید static serving را درست بفهمی.

ساختار بساز:

```bash
sudo mkdir -p /var/www/nginx-lab/assets
echo "<h1>Home</h1>" | sudo tee /var/www/nginx-lab/index.html
echo "<h1>About</h1>" | sudo tee /var/www/nginx-lab/about.html
echo "body { font-family: sans-serif; }" | sudo tee /var/www/nginx-lab/assets/style.css
```

config:

```nginx
server {
    listen 80;
    server_name _;

    root /var/www/nginx-lab;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location /assets/ {
        expires 7d;
        add_header Cache-Control "public";
    }
}
```

تست:

```bash
curl -I http://localhost/assets/style.css
```

باید headerهای cache را ببینی.

---

## تفاوت `root` و `alias`

این یکی از مهم‌ترین دام‌های Nginx است.

### با root

```nginx
location /images/ {
    root /var/www/app;
}
```

Request:

```text
/images/a.png
```

File path:

```text
/var/www/app/images/a.png
```

### با alias

```nginx
location /images/ {
    alias /data/uploads/;
}
```

Request:

```text
/images/a.png
```

File path:

```text
/data/uploads/a.png
```

پس:

```text
root مسیر URL را به مسیر filesystem اضافه می‌کند.
alias مسیر location را جایگزین می‌کند.
```

اشتباه در `alias` یکی از دلیل‌های رایج 404 و حتی مشکل امنیتی است.

---
