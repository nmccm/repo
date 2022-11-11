#!/bin/sh

export today="`date '+%Y%m%d'`"
#/bin/mkdir -p /root/backup_database/$today
DBHOST="localhost"
DBUSER="dbuser"
DBPASS="password"
DBLIST="database_name"
SQLBIN="/usr/bin"
BACKUPDIR="/root/backup_database/${today}"
/bin/mkdir $BACKUPDIR

for THISDB in $DBLIST
    do
    TABLELIST=`${SQLBIN}/mysql -h${DBHOST} -u${DBUSER} -p${DBPASS} ${THISDB} -e "show tables" | /bin/grep -v Tables_in_${THISDB}`
    DIR="${BACKUPDIR}/${THISDB}"
    /bin/mkdir $DIR
    for THISTABLE in $TABLELIST
        do
        TABLEDIR="${DIR}/${THISTABLE}.sql"

        $SQLBIN/mysqldump -h$DBHOST -u$DBUSER -p$DBPASS $THISDB $THISTABLE > $TABLEDIR
    done
done
