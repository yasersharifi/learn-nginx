---
title: "Config نمونه lab فاز ۳"
description: "Config نمونه lab فاز ۳"
---

# Config نمونه lab فاز ۳

```nginx id="hqqps3"
worker_processes auto;
worker_rlimit_nofile 65535;

events {
    worker_connections 4096;
}

http {
    sendfile on;

    log_format perf_json escape=json
    '{'
      '"time":"$time_iso8601",'
      '"remote_addr":"$remote_addr",'
      '"method":"$request_method",'
      '"uri":"$request_uri",'
      '"status":$status,'
      '"request_time":$request_time,'
      '"upstream_time":"$upstream_response_time",'
      '"upstream_addr":"$upstream_addr",'
      '"upstream_status":"$upstream_status",'
      '"bytes":$body_bytes_sent,'
      '"request_id":"$request_id"'
    '}';

    upstream app_backend {
        least_conn;

        server 127.0.0.1:4001 max_fails=3 fail_timeout=10s;
        server 127.0.0.1:4002 max_fails=3 fail_timeout=10s;

        keepalive 32;
    }

    server {
        listen 80;
        server_name _;

        access_log /var/log/nginx/phase3.access.log perf_json;
        error_log /var/log/nginx/phase3.error.log warn;

        location = /nginx-health {
            access_log off;
            return 200 "ok\n";
        }

        location /static/ {
            root /var/www/phase3;
            try_files $uri =404;
            expires 7d;
        }

        location /api/ {
            proxy_pass http://app_backend/;

            proxy_http_version 1.1;
            proxy_set_header Connection "";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Request-ID $request_id;

            proxy_connect_timeout 5s;
            proxy_send_timeout 30s;
            proxy_read_timeout 30s;
        }

        location /stream/ {
            proxy_pass http://app_backend/stream/;

            proxy_http_version 1.1;
            proxy_set_header Connection "";
            proxy_set_header Host $host;

            proxy_buffering off;
            proxy_read_timeout 300s;
        }
    }
}
```

---
