# راهنمای ویرایش

## ساختار مخزن

```text
learn-nginx/
├── README.md                 ← صفحه اصلی GitHub
├── HOW-TO-EDIT.md            ← همین فایل
├── content/                  ← همهٔ markdownهای محتوا
│   ├── introduction.md
│   ├── nginx/
│   │   ├── phase1.md
│   │   ├── phase2.md
│   │   └── phase3-network.md
│   ├── linux/
│   │   ├── linux.md
│   │   └── grep.md
│   └── git/
│       ├── rebase-fast-forward.md
│       ├── head-guide.md
│       └── rebase-questions.md
├── assets/images/
├── book.toml
├── theme/custom.css
└── scripts/
    ├── prepare-mdbook.py
    └── build-book.sh
```

فایل‌های `src/` و `book/` خودکار ساخته می‌شوند — **دستی edit نکن.**

---

## افزودن یا تغییر محتوا

1. فایل را در `content/` ویرایش کن.
2. build:

```bash
./scripts/build-book.sh
```

3. `book/index.html` را در مرورگر چک کن.

---

## فصل جدید

1. فایل `.md` در `content/` بساز (مثلاً `content/git/my-topic.md`).
2. در `scripts/prepare-mdbook.py` به `SOURCES` اضافه کن:

```python
("git/my-topic.md", "git/my-topic.md", True),  # True = فارسی/RTL
```

3. لینک را در `write_summary()` و `content/introduction.md` بگذار.
4. لینک را در `README.md` (root) هم اضافه کن.
5. `./scripts/build-book.sh`

---

## قوانین نوشتن

- متن ساده و مستقیم — مثل یادداشت برای خودت.
- کد در بلوک markdown با زبان مشخص:

````markdown
```bash
nginx -t
```
````

- از calloutهای `[!NOTE]` استفاده نکن.
- wrapper HTML مثل `<div dir="rtl">` لازم نیست.
- تصاویر در `assets/images/`:

```markdown
![توضیح](../../assets/images/my-diagram.png)
```

از داخل `content/nginx/` مسیر نسبی به assets: `../../assets/images/...`

---

## mdBook

**GitHub Pages:** https://yasersharifi.github.io/learn-nginx/

Deploy خودکار با push به `main` (workflow: `.github/workflows/pages.yml`).

اولین بار: repo → **Settings → Pages → Source: GitHub Actions**.

```bash
python3 scripts/prepare-mdbook.py
./scripts/build-book.sh
./.bin/mdbook serve                 # localhost:3000 (بهتر از file://)
```

`book.toml` برای GitHub Pages با `site-url = "/learn-nginx/"` تنظیم شده.

---

## چک‌لیست قبل از commit

- [ ] تغییرات فقط در `content/`، `assets/`، `theme/`، `scripts/`، `book.toml`، `README.md`
- [ ] `./scripts/build-book.sh` بدون خطا
- [ ] یک صفحه فارسی و یک بلوک کد در `book/index.html` درست است
