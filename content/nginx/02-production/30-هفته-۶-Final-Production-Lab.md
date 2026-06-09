---
title: "هفته ۶: Final Production Lab"
description: "هفته ۶: Final Production Lab"
---

# هفته ۶: Final Production Lab

در هفته آخر باید همه چیز را ترکیب کنی.

## معماری نهایی

```text
Internet
  ↓
Nginx
  ├── HTTP ← HTTPS redirect
  ├── TLS termination
  ├── HTTP/2
  ├── Security headers
  ├── Rate limiting
  ├── Connection limiting
  ├── Static asset caching
  ├── Proxy cache for public API
  ├── JSON access logs
  ├── Request ID
  ├── Custom error responses
  └── Reverse proxy
        ├── frontend_app
        └── api_backend
```

---
