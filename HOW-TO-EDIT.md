# راهنمای ویرایش

## ساختار

```text
learn-nginx/
├── content/                  ← markdown (منبع اصلی)
├── static/fonts/               ← Vazir، Inter، JetBrains Mono
├── src/css/custom.css          ← RTL، فونت‌ها
├── docusaurus.config.ts        ← تنظیمات (TypeScript)
├── sidebars.ts                 ← sidebar (TypeScript)
├── tsconfig.json
└── package.json
```

خروجی build در `build/` — commit نکن.

---

## ویرایش محتوا

```bash
npm install
npm start          # http://localhost:3000/learn-nginx/
npm run build
npm run typecheck  # بررسی TypeScript
```

---

## فصل جدید

1. فایل `.md` در `content/` بساز.
2. در `sidebars.ts` اضافه کن.
3. لینک در `content/introduction.md` و `README.md`.

Front matter:

```yaml
---
title: عنوان
sidebar_label: برچسب
sidebar_position: 2
---
```

صفحه انگلیسی:

```yaml
---
title: grep
className: en-doc
---
```

لینک بین صفحات (بدون `.md`):

```markdown
[Linux](linux/)
[فاز ۱](nginx/phase1)
```

---

## فارسی (RTL)

سایت با `locale: fa` و `direction: rtl` تنظیم شده:

- `html lang="fa-IR" dir="rtl"`
- برچسب‌های UI فارسی (قبلی / بعدی / کپی / …)
- فونت **Vazir** برای متن فارسی
- sidebar سمت راست، TOC سمت چپ
- کد همیشه LTR

تنظیمات: `docusaurus.config.ts` → `i18n.localeConfigs.fa`  
استایل: `src/css/custom.css`

صفحه انگلیسی: front matter `className: en-doc`

---

## GitHub Pages

https://yasersharifi.github.io/learn-nginx/

Deploy با push به `main` — workflow: `.github/workflows/pages.yml`

---

## چک‌لیست commit

- [ ] `npm run build` بدون خطا
- [ ] `npm run typecheck` بدون خطا
