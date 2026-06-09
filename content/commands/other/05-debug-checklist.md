---
title: "چک‌لیست debug"
description: "ترتیب دستورات وقتی سایت یا API روی سرور down است"
---

# چک‌لیست debug

وقتی production مشکل دارد، این ترتیب معمولاً جواب می‌دهد:

## ۱. سرویس زنده است؟

```bash
sudo systemctl status nginx
pm2 list                    # یا
sudo systemctl status my-api
docker compose ps
```

## ۲. log

```bash
sudo tail -n 100 /var/log/nginx/error.log
sudo journalctl -u my-api -n 100 --no-pager
pm2 logs api --lines 50
docker compose logs --tail=50 api
```

## ۳. پورت و پروسس

```bash
sudo ss -tulpn | grep -E ':80|:443|:3000'
sudo lsof -i :3000
curl -i http://localhost:3000/health
```

## ۴. Nginx

```bash
sudo nginx -t
curl -I http://localhost
curl -I https://example.com
```

## ۵. منابع

```bash
df -h
free -h
top    # یا htop
```

## ۶. DNS و SSL

```bash
dig example.com
curl -Iv https://example.com
```

## ۷. اخیراً چه deploy شد؟

```bash
git log -1 --oneline
sudo nginx -T | head -50
docker compose config
```
