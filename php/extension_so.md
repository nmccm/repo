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

config.m4, php_hash_entry.h, hash_entry.c 파일을 수정해준다.
		
```linux	
# vi config.m4			

dnl PHP_ARG_WITH(hash_entry, for hash_entry support,
dnl Make sure that the comment is aligned:
dnl [  --with-hash_enty             Include hash_entry support])

dnl Otherwise use enable:

PHP_ARG_ENABLE(hash_entry, whether to enable hash_entry support,
[  --enable-hash_entry           Enable hash_entry support])

if test "$PHP_HASH_ENTRY" != "no"; then
        AC_DEFINE(HAVE_HASH_ENTRY, 1, [Whether you have hash_entry])
  PHP_NEW_EXTENSION(hash_entry, hash_entry.c, $ext_shared,, -DZEND_ENABLE_STATIC_TSRMLS_CACHE=1)
fi
```

```linux	
# vi php_hash_entry.h

#ifndef PHP_HASH_ENTRY_H
#define PHP_HASH_ENTRY_H
#define PHP_MYEXT_EXTNAME "hash_entry"

PHP_FUNCTION(hash_entry_func);

extern zend_module_entry hash_entry_module_entry;
#define phpext_hash_entry_ptr &hash_entry_module_entry

#define PHP_HASH_ENTRY_VERSION "0.1.0" 

#ifdef PHP_WIN32
#       define PHP_HASH_ENTRY_API __declspec(dllexport)
#elif defined(__GNUC__) && __GNUC__ >= 4
#       define PHP_HASH_ENTRY_API __attribute__ ((visibility("default")))
#else
#       define PHP_HASH_ENTRY_API
#endif

#ifdef ZTS
#include "TSRM.h"
#endif

#define HASH_ENTRY_G(v) ZEND_MODULE_GLOBALS_ACCESSOR(hash_entry, v)

#if defined(ZTS) && defined(COMPILE_DL_HASH_ENTRY)
ZEND_TSRMLS_CACHE_EXTERN()
#endif

#endif
```
