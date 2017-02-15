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

## install for centos 6.8

```linux
# yum -y install postgresql postgresql-contrib postgresql-server
# service postgresql initdb
$ su - postgresql
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

## Connect

```linux
# sudo -i -u postgres
$ psql
postgres=# \du
```

## role 

```linux
postgres=# \du
                              List of roles
  Role name  |                   Attributes                   | Member of
-------------+------------------------------------------------+-----------
 aaaa        | Superuser                                      | {}
 bbbb        |                                                | {} 
 postgres    | Superuser, Create role, Create DB, Replication | {}

postgres=# \du
```


