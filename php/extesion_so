# PHP 확장 라이브러리 

PHP 확장 라이브러리 작성 및 사용법에 관한 문서

## PHP source download

wget 으로 다운받는 php-xxxx.tar.gz 은 구글링을 통해 확인해야 한다.

```linux
# yum -y install wget
# mkdir php_source
# cd php_source
# wget https://www.php.net/distributions/php-7.0.33.tar.gz 
# tar zxvf php-7.0.33.tar.gz
# cd php-7.0.33/ext/ 
```

## 확장 라이브러리 개발 환경 설정

```linux
# ls -al | grep ^- 		
-rwxrwxr-x  1 1000 1000  8671 Dec  5  2018 ext_skel
-rw-rw-r--  1 1000 1000  1169 Dec  5  2018 ext_skel_win32.php

# ./ext_skel --extname=hash_entry
Creating directory hash_entry
Creating basic files: config.m4 config.w32 .gitignore hash_entry.c php_hash_entry.h CREDITS EXPERIMENTAL tests/001.phpt hash_entry.php [done].

To use your new extension, you will have to execute the following steps:

1.  $ cd ..
2.  $ vi ext/hash_entry/config.m4
3.  $ ./buildconf
4.  $ ./configure --[with|enable]-hash_entry
5.  $ make
6.  $ ./sapi/cli/php -f ext/hash_entry/hash_entry.php
7.  $ vi ext/hash_entry/hash_entry.c
8.  $ make

Repeat steps 3-6 until you are satisfied with ext/hash_entry/config.m4 and
step 6 confirms that your module is compiled into PHP. Then, start writing
code and repeat the last two steps as often as necessary.

# cd hash_entry
```
