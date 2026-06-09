---
title: "34. چند alias مفید"
description: "34. چند alias مفید"
---

# 34. چند alias مفید

می‌توانید aliasها را در فایل زیر بگذارید:

```bash
nano ~/.bashrc
```

نمونه:

```bash
alias ll='ls -la'
alias gs='git status'
alias gp='git pull'
alias dps='docker ps'
alias dcup='docker compose up -d'
alias dclogs='docker compose logs -f'
alias ports='sudo ss -tulpn'
```

بعد از تغییر:

```bash
source ~/.bashrc
```

---
