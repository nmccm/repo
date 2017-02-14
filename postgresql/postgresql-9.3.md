# PostgreSQL 9.3

## install for ubuntu 14.04

```linux
$ sudo apt-get update
$ sudo apt-get install -y postgresql         
$ sudo apt-get install -y postgresql-contrib
$ ps -ef | grep post
$ psql --version  
psql (PostgreSQL) 9.3.13
```

## Database Create, Drop 

linux shell command

```linux
$ sudo su -		
# sudo -i -u postgres
$ psql -c "CREATE DATABASE {database name}"
$ psql -c "CREATE ROLE {user} PASSWORD '{password}' LOGIN"
$ psql -c "GRANT ALL ON DATABASE {database name} TO {user}"
```

linux shell command

```linux
$ sudo su -
# sudo -i -u postgres
$ psql -c "DROP DATABASE {database name}"
$ exit
```

## Database Backup & Restore

linux shell command (backup)

```linux
# PGPASSWORD={password} pg_dump {database name} -U {user} -h localhost > {filename}.dump
```

linux shell command (restore)

```linux
# PGPASSWORD={password} psql -U {user} -h localhost < sql/schema.sql
```



