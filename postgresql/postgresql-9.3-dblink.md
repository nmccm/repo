# PostgreSQL 9.3 dblink

## install for ubuntu 14.04

```linux
$ sudo apt-get update         
$ sudo apt-get install -y postgresql-contrib
$ sudo su -
# sudo -i -u postgres
$ psql
postgres=# CREATE EXTENSION dblink;
```

using

postgresql-server

ㄴdatabase1

	ㄴ table1
	
ㄴdatabase2

	ㄴ table2

```linux
postgres=# insert into table1 (log_time, user_id, kind, cmd, action)
			select * from dblink(
				'hostaddr=127.0.0.1 port=5432 dbname={database name} user={user} password={password}',
				'select log_time, user_id, kind, cmd, action from table2 where user_id = 509'
			) 
			as t1(
				log_time timestamp with time zone, 
				user_id integer, 
				kind character(3), 
				cmd character varying(32), 
				action json
			) 
```