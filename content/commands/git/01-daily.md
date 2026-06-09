---
title: "کار روزمره"
description: "git status، add، commit، push، pull — دستورات پرتکرار"
---

# کار روزمره

| دستور | کاربرد |
| --- | --- |
| `git status` | وضعیت working tree |
| `git diff` | تغییرات unstaged |
| `git diff --staged` | تغییرات staged |
| `git add file` | stage فایل |
| `git add .` | stage همه |
| `git commit -m "msg"` | commit |
| `git push` | ارسال به remote |
| `git pull` | دریافت + merge/rebase |
| `git pull --rebase` | pull با rebase |
| `git pull --ff-only` | فقط fast-forward |
| `git fetch origin` | دریافت بدون merge |
| `git log --oneline -10` | ۱۰ commit آخر |
| `git log --oneline --graph --all` | نمودار branchها |

## branch

| دستور | کاربرد |
| --- | --- |
| `git branch` | لیست local |
| `git branch -a` | local + remote |
| `git switch main` | رفتن به branch |
| `git switch -c feature/x` | branch جدید |
| `git checkout -b feature/x` | روش قدیمی |
| `git merge main` | merge به branch فعلی |
| `git rebase origin/main` | rebase روی main |

## stash و بازگردانی

| دستور | کاربرد |
| --- | --- |
| `git stash` | ذخیره موقت تغییرات |
| `git stash pop` | برگرداندن |
| `git stash list` | لیست stashها |
| `git restore file` | بازگردانی فایل |
| `git reset HEAD~1` | حذف آخرین commit (soft mixed) |

```bash
git push --force-with-lease   # بعد از rebase روی branch شخصی
```
