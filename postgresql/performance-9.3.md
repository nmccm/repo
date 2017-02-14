# PostgreSQL performance 

## Database Backup & Restore

linux shell command (backup)

```linux
# PGPASSWORD={password} pg_dump {database name} -U {user} -h localhost > {filename}.dump
```

linux shell command (restore)

```linux
# PGPASSWORD={password} psql -U {user} -h localhost < sql/schema.sql
```



