---
title: "29. PostgreSQL و MySQL از ترمینال"
description: "29. PostgreSQL و MySQL از ترمینال"
---

# 29. PostgreSQL و MySQL از ترمینال

### اتصال به PostgreSQL

```bash
psql -h localhost -U postgres -d mydb
```

### چند دستور مهم psql

```sql
\l
\c mydb
\dt
\d users
\q
```

### گرفتن backup از PostgreSQL

```bash
pg_dump -h localhost -U postgres mydb > backup.sql
```

### restore کردن PostgreSQL

```bash
psql -h localhost -U postgres mydb < backup.sql
```

### اتصال به MySQL

```bash
mysql -h localhost -u root -p
```

### backup از MySQL

```bash
mysqldump -u root -p mydb > backup.sql
```

---
