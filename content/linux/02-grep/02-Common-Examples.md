---
title: "Common Examples"
description: "Common Examples"
---

# Common Examples

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
