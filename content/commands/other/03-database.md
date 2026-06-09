---
title: "دیتابیس"
description: "psql، mysql، pg_dump — اتصال و backup"
---

# دیتابیس

## PostgreSQL

| دستور | کاربرد |
| --- | --- |
| `psql -h localhost -U postgres -d mydb` | اتصال |
| `\l` | لیست database |
| `\c mydb` | سوئیچ database |
| `\dt` | لیست جدول |
| `\d users` | schema جدول |
| `\q` | خروج |
| `pg_dump -h localhost -U postgres mydb > b.sql` | backup |
| `psql -h localhost -U postgres mydb < b.sql` | restore |

## MySQL

| دستور | کاربرد |
| --- | --- |
| `mysql -h localhost -u root -p` | اتصال |
| `SHOW DATABASES;` | لیست |
| `USE mydb;` | انتخاب |
| `SHOW TABLES;` | جدول‌ها |
| `mysqldump -u root -p mydb > b.sql` | backup |
| `mysql -u root -p mydb < b.sql` | restore |

```bash
# داخل Docker
docker compose exec postgres psql -U postgres -d mydb
docker compose exec mysql mysql -u root -p
```
