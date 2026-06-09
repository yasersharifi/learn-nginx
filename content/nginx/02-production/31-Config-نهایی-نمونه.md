---
title: "Config نهایی نمونه"
description: "Config نهایی نمونه"
---

# Config نهایی نمونه

## `/etc/nginx/snippets/proxy-headers.conf`

```nginx
proxy_http_version 1.1;

proxy_set_header Connection "";
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Forwarded-Host $host;
proxy_set_header X-Forwarded-Port $server_port;
proxy_set_header X-Request-ID $request_id;
```

---

## `/etc/nginx/snippets/proxy-timeouts.conf`

```nginx
proxy_connect_timeout 5s;
proxy_send_timeout 30s;
proxy_read_timeout 30s;
send_timeout 30s;
```

---

## `/etc/nginx/snippets/security-headers.conf`

```nginx
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header X-XSS-Protection "0" always;
```

برای HTTPS production بعد از اطمینان:

```nginx
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
```

---

## `/etc/nginx/snippets/ssl-params.conf`

```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_prefer_server_ciphers off;

ssl_session_cache shared:SSL:10m;
ssl_session_timeout 1d;
ssl_session_tickets off;
```

---

## بخش‌هایی در `http` context

داخل `/etc/nginx/nginx.conf` در context `http`:

```nginx
log_format production_json escape=json
'{'
  '"time":"$time_iso8601",'
  '"remote_addr":"$remote_addr",'
  '"request_method":"$request_method",'
  '"request_uri":"$request_uri",'
  '"status":$status,'
  '"body_bytes_sent":$body_bytes_sent,'
  '"request_time":$request_time,'
  '"upstream_addr":"$upstream_addr",'
  '"upstream_status":"$upstream_status",'
  '"upstream_response_time":"$upstream_response_time",'
  '"http_referer":"$http_referer",'
  '"http_user_agent":"$http_user_agent",'
  '"request_id":"$request_id"'
'}';

limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
limit_conn_zone $binary_remote_addr zone=conn_limit:10m;

proxy_cache_path /var/cache/nginx/app_cache
    levels=1:2
    keys_zone=app_cache:10m
    max_size=1g
    inactive=60m
    use_temp_path=off;

gzip on;
gzip_comp_level 5;
gzip_min_length 1024;
gzip_types
    text/plain
    text/css
    application/json
    application/javascript
    application/xml
    image/svg+xml;

upstream frontend_app {
    server 127.0.0.1:3000 max_fails=3 fail_timeout=10s;
    keepalive 16;
}

upstream api_backend {
    least_conn;

    server 127.0.0.1:4001 max_fails=3 fail_timeout=10s;
    server 127.0.0.1:4002 max_fails=3 fail_timeout=10s;

    keepalive 32;
}
```

---

## `/etc/nginx/sites-available/app.conf`

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com www.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    include snippets/ssl-params.conf;

    access_log /var/log/nginx/app.access.log production_json;
    error_log /var/log/nginx/app.error.log warn;

    include snippets/security-headers.conf;

    client_max_body_size 20m;

    limit_conn conn_limit 20;

    location = /nginx-health {
        access_log off;
        return 200 "ok\n";
    }

    location = /api-50x.json {
        internal;
        default_type application/json;
        return 503 '{"error":"service_unavailable","message":"Service temporarily unavailable","request_id":"$request_id"}';
    }

    location /assets/ {
        root /var/www/app;

        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /uploads/ {
        alias /var/www/uploads/;
        try_files $uri =404;

        expires 7d;
        add_header Cache-Control "public";
    }

    location /api/public/ {
        limit_req zone=api_limit burst=20 nodelay;
        limit_req_status 429;

        proxy_pass http://api_backend/;

        proxy_cache app_cache;
        proxy_cache_valid 200 10m;
        proxy_cache_valid 404 1m;
        proxy_cache_bypass $http_authorization;
        proxy_no_cache $http_authorization;
        proxy_cache_key "$scheme$request_method$host$request_uri";

        add_header X-Cache-Status $upstream_cache_status always;

        proxy_intercept_errors on;
        error_page 502 503 504 = /api-50x.json;

        proxy_next_upstream error timeout http_502 http_503 http_504;
        proxy_next_upstream_tries 2;
        proxy_next_upstream_timeout 10s;

        include snippets/proxy-headers.conf;
        include snippets/proxy-timeouts.conf;
    }

    location /api/ {
        limit_req zone=api_limit burst=20 nodelay;
        limit_req_status 429;

        proxy_pass http://api_backend/;

        proxy_intercept_errors on;
        error_page 502 503 504 = /api-50x.json;

        proxy_next_upstream error timeout http_502 http_503 http_504;
        proxy_next_upstream_tries 2;
        proxy_next_upstream_timeout 10s;

        include snippets/proxy-headers.conf;
        include snippets/proxy-timeouts.conf;
    }

    location / {
        proxy_pass http://frontend_app;

        include snippets/proxy-headers.conf;
        include snippets/proxy-timeouts.conf;
    }
}
```

---
