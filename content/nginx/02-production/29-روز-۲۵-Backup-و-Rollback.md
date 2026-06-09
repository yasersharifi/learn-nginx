---
title: "روز ۲۵: Backup و Rollback"
description: "روز ۲۵: Backup و Rollback"
---

# روز ۲۵: Backup و Rollback

قبل از تغییر بزرگ:

```bash
sudo cp /etc/nginx/sites-available/app.conf /etc/nginx/sites-available/app.conf.bak
```

یا بهتر: configها را در Git نگه دار.

ساختار repo:

```text
infra-nginx/
  nginx.conf
  sites-available/
    app.conf
  snippets/
    proxy-headers.conf
    proxy-timeouts.conf
    ssl-params.conf
    security-headers.conf
  README.md
```

## قانون مهم

تغییرات Nginx production نباید دستی و بدون history باشد.

حداقل باید بدانی:

```text
- چه کسی تغییر داد
- چه چیزی تغییر کرد
- چرا تغییر کرد
- چطور rollback کنیم
```

---
