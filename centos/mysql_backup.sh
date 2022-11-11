#!/bin/sh

export Today="`date '+%y-%m-%d'`"
HOUR=`/bin/date +"%H"`
#/bin/mkdir -p /home/centos/db_backup/$Today

DBHOST="xxx.xxx.xxx.xxx"
DBUSER="root"
DBPASS="123456789"
DBLIST="textbook"
SQLBIN="/usr/bin" 
BACKUPDIR="/root" 
for THISDB in $DBLIST
    do
    TABLELIST=`${SQLBIN}/mysql -h${DBHOST} -u${DBUSER} -p${DBPASS} ${THISDB} -e "show tables" | /bin/grep -v Tables_in_${THISDB}`
    DIR="${BACKUPDIR}/${THISDB}"
    /bin/mkdir $DIR 
    for THISTABLE in $TABLELIST
        do
        TABLEDIR="${DIR}/${THISDB}.${THISTABLE}.sql"

        $SQLBIN/mysqldump -h$DBHOST -u$DBUSER -p$DBPASS $THISDB $THISTABLE > $TABLEDIR
    done
done

#tar cvfpz /backup/data/$Today/mysql_$Today_${HOUR}h.tar.gz /backup/data/$Today/mysql
#/bin/rm -rf $BACKUPDIR 



#for x in `ls *.sql`;
#do
#    mysql -uUSERID -pPASSWORD DB_NAME < $x
#done;
