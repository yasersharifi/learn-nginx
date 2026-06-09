---
title: grep
sidebar_label: grep
className: en-doc
---

# grep

`grep` متن را داخل فایل یا خروجی دستور پیدا می‌کند. برای log، کد و pipe خیلی کاربرد دارد.

نام از این می‌آید:

```bash
g/re/p
```

یعنی: جستجوی regex در کل فایل و چاپ خطوط match.

---

## Basic Usage

```bash
grep "error" app.log
```

هر خطی که `error` داشته باشد چاپ می‌شود.

---

## Common Examples

### Search for text in a file

```bash
grep "TODO" src/index.ts
```

### Search recursively in a directory

```bash
grep -r "useEffect" src/
```

### Case-insensitive search

```bash
grep -i "error" app.log
```

### Show line numbers

```bash
grep -n "failed" app.log
```

### Invert match

```bash
grep -v "debug" app.log
```

خطوطی که `debug` ندارند.

### Search command output

```bash
ps aux | grep nginx
```

---

## Useful Options

| Option | Meaning |
| --- | --- |
| `-r` | Recursive |
| `-i` | Case insensitive |
| `-n` | Line numbers |
| `-v` | Invert match |
| `-c` | Count matches |
| `-l` | Only filenames |
| `-w` | Whole word |

---

## Developer Example

```bash
grep -r "function login" .
```

کل پروژه را برای `function login` می‌گردد.

---

## Alternative: ripgrep

روی پروژه‌های بزرگ `rg` معمولاً سریع‌تر است:

```bash
rg "useEffect" src
```

`grep` هنوز روی اکثر Linux/macOS به‌صورت پیش‌فرض هست.

---

## Summary

- پیدا کردن متن در فایل
- grep روی log
- grep در سورس
- فیلتر خروجی pipe
