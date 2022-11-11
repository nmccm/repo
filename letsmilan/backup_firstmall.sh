yum install sshpass


#!/bin/bash

DATE=`date "+%Y%m%d"`

mkdir /root/backup_firstmall_db/${DATE} && chmod +w /root/backup_firstmall_db/${DATE} && sshpass -p\!password scp -o StrictHostKeyChecking=no username@ip:/path/${DATE}/*.sql ./${DATE}/
