---
title: "هفته ۱۰: strace و tcpdump در Debug واقعی"
description: "هفته ۱۰: strace و tcpdump در Debug واقعی"
---

# هفته ۱۰: strace و tcpdump در Debug واقعی

## سناریو ۱: 502

Backend خاموش:

```bash id="8bmmwt"
curl -i http://localhost/api/test
```

بررسی:

```bash id="y5ndt6"
sudo tail -f /var/log/nginx/error.log
ss -tan | grep 4000
```

سؤال:

```text id="mtg7bv"
آیا Nginx اصلاً توانسته به upstream connect کند؟
```

---

## سناریو ۲: 504

Backend کند:

```js id="8pht74"
app.get("/slow", async (req, res) => {
  await new Promise(resolve => setTimeout(resolve, 60000));
  res.json({ ok: true });
});
```

Nginx timeout:

```nginx id="4vigrz"
proxy_read_timeout 10s;
```

تست:

```bash id="l5sovg"
curl -i http://localhost/api/slow
```

بررسی:

```bash id="5wofeb"
sudo tail -f /var/log/nginx/error.log
```

---

## سناریو ۳: client کند

فایل بزرگ:

```bash id="znubkb"
curl --limit-rate 10k http://localhost/big.bin -o /tmp/big.bin
```

همزمان connectionها را ببین:

```bash id="03zyvi"
ss -tan | grep ':80'
```

buffering و sendfile را بررسی کن.

---
