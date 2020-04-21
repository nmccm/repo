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

```linux	
# vi hash_entry.c

const zend_function_entry hash_entry_functions[] = {
        PHP_FE(confirm_hash_entry_compiled,     NULL)
        PHP_FE(hash_entry_func,     NULL)       // add
        PHP_FE_END
};

zend_module_entry hash_entry_module_entry = {
        STANDARD_MODULE_HEADER,
        PHP_HASH_ENTRY_EXTNAME,
        hash_entry_functions,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        PHP_HASH_ENTRY_VERSION,
        STANDARD_MODULE_PROPERTIES
};

PHP_FUNCTION(hash_entry_func)
{
    char* s;
    long len;

    if (zend_parse_parameters(ZEND_NUM_ARGS() TSRMLS_CC, "s", &s, &len) == FAILURE) {
        RETURN_NULL();
    }

    php_printf("String(%d) : %s\n", len, s);
}

```

컴파일
		
```linux	
# find / -name phpize
/usr/local/php/bin/phpize

# /usr/local/php/bin/phpize 
Configuring for:
PHP Api Version:         20151012
Zend Module Api No:      20151012
Zend Extension Api No:   320151012

# find / -name php-config
/usr/local/php/bin/php-config

# ./configure --with-php-config=/usr/local/php/bin/php-config
checking for grep that handles long lines and -e... /bin/grep
checking for egrep... /bin/grep -E
checking for a sed that does not truncate output... /bin/sed
checking for cc... cc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables...
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether cc accepts -g... yes
checking for cc option to accept ISO C89... none needed
checking how to run the C preprocessor... cc -E
checking for icc... no
checking for suncc... no
checking whether cc understands -c and -o together... yes
checking for system library directory... lib
checking if compiler supports -R... no
checking if compiler supports -Wl,-rpath,... yes
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking target system type... x86_64-unknown-linux-gnu
checking for PHP prefix... /usr/local/php
checking for PHP includes... -I/usr/local/php/include/php -I/usr/local/php/include/php/main -I/usr/local/php/include/php/TSRM -I/usr/local/php/include/php/Zend -I/usr/local/php/include/php/ext -I/usr/local/php/include/php/ext/date/lib
checking for PHP extension directory... /usr/local/php/lib/php/extensions/no-debug-non-zts-20151012
checking for PHP installed headers prefix... /usr/local/php/include/php
checking if debug is enabled... no
checking if zts is enabled... no
checking for re2c... no
configure: WARNING: You will need re2c 0.13.4 or later if you want to regenerate PHP parsers.
checking for gawk... gawk
checking whether to enable hash_entry support... yes, shared
checking for ld used by cc... /usr/bin/ld
checking if the linker (/usr/bin/ld) is GNU ld... yes
checking for /usr/bin/ld option to reload object files... -r
checking for BSD-compatible nm... /usr/bin/nm -B
checking whether ln -s works... yes
checking how to recognize dependent libraries... pass_all
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking dlfcn.h usability... yes
checking dlfcn.h presence... yes
checking for dlfcn.h... yes
checking the maximum length of command line arguments... 1572864
checking command to parse /usr/bin/nm -B output from cc object... ok
checking for objdir... .libs
checking for ar... ar
checking for ranlib... ranlib
checking for strip... strip
checking if cc supports -fno-rtti -fno-exceptions... no
checking for cc option to produce PIC... -fPIC
checking if cc PIC flag -fPIC works... yes
checking if cc static flag -static works... no
checking if cc supports -c -o file.o... yes
checking whether the cc linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking whether -lc should be explicitly linked in... no
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... yes
checking whether to build static libraries... no

creating libtool
appending configuration tag "CXX" to libtool
configure: creating ./config.status
config.status: creating config.h

# make
/bin/sh /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/libtool --mode=compile cc -DZEND_ENABLE_STATIC_TSRMLS_CACHE=1 -I. -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry -DPHP_ATOM_INC -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry/include -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry/main -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry -I/usr/local/php/include/php -I/usr/local/php/include/php/main -I/usr/local/php/include/php/TSRM -I/usr/local/php/include/php/Zend -I/usr/local/php/include/php/ext -I/usr/local/php/include/php/ext/date/lib  -DHAVE_CONFIG_H  -g -O2   -c /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/hash_entry.c -o hash_entry.lo
 cc -DZEND_ENABLE_STATIC_TSRMLS_CACHE=1 -I. -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry -DPHP_ATOM_INC -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry/include -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry/main -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry -I/usr/local/php/include/php -I/usr/local/php/include/php/main -I/usr/local/php/include/php/TSRM -I/usr/local/php/include/php/Zend -I/usr/local/php/include/php/ext -I/usr/local/php/include/php/ext/date/lib -DHAVE_CONFIG_H -g -O2 -c /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/hash_entry.c  -fPIC -DPIC -o .libs/hash_entry.o
/bin/sh /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/libtool --mode=link cc -DPHP_ATOM_INC -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry/include -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry/main -I/home/ec2-user/gabia/php-7.0.33/ext/hash_entry -I/usr/local/php/include/php -I/usr/local/php/include/php/main -I/usr/local/php/include/php/TSRM -I/usr/local/php/include/php/Zend -I/usr/local/php/include/php/ext -I/usr/local/php/include/php/ext/date/lib  -DHAVE_CONFIG_H  -g -O2   -o hash_entry.la -export-dynamic -avoid-version -prefer-pic -module -rpath /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/modules  hash_entry.lo
cc -shared  .libs/hash_entry.o   -Wl,-soname -Wl,hash_entry.so -o .libs/hash_entry.so
creating hash_entry.la
(cd .libs && rm -f hash_entry.la && ln -s ../hash_entry.la hash_entry.la)
/bin/sh /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/libtool --mode=install cp ./hash_entry.la /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/modules
cp ./.libs/hash_entry.so /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/modules/hash_entry.so
cp ./.libs/hash_entry.lai /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/modules/hash_entry.la
PATH="$PATH:/sbin" ldconfig -n /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/modules
----------------------------------------------------------------------
Libraries have been installed in:
   /home/ec2-user/gabia/php-7.0.33/ext/hash_entry/modules

If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the `-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the `LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the `LD_RUN_PATH' environment variable
     during linking
   - use the `-Wl,--rpath -Wl,LIBDIR' linker flag
   - have your system administrator add LIBDIR to `/etc/ld.so.conf'

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------------

Build complete.
Don't forget to run 'make test'.

# ls -al modules/
total 56
drwxr-xr-x 2 root root  4096 Apr 21 18:20 .
drwxr-xr-x 8 root root  4096 Apr 21 18:20 ..
-rw-r--r-- 1 root root   832 Apr 21 18:20 hash_entry.la
-rwxr-xr-x 1 root root 44200 Apr 21 18:20 hash_entry.so

# php -i | grep extension_dir 
extension_dir => /usr/local/php/lib/php/extensions/ => /usr/local/php/lib/php/extensions/

# cp -p modules/hash_entry.so /usr/local/php/lib/php/extensions/
# php --ini
Configuration File (php.ini) Path: /usr/local/apache/conf
Loaded Configuration File:         /usr/local/apache/conf/php.ini
Scan for additional .ini files in: (none)
Additional .ini files parsed:      (none)

# vi /usr/local/apache/conf/php.ini
extension_dir = "/usr/local/php/lib/php/extensions/"
extension = "hash_entry.so"

# /etc/init.d/httpd restart
# php -m | grep hash
hash_entry
```

test.php 파일을 만든 후 테스트 소스를 작성하여 실행

```php
$module = 'hash_entry';        
$modules = explode(' ', $module);

foreach($modules as $m) {            
    if(!extension_loaded($m)) {
        //dl($m . '.' . PHP_SHLIB_SUFFIX);
    }            
    echo "<pre>"; print_r(get_extension_funcs($m)); echo "</pre>"; 
}

var_dump(hasn_entry_func('this'));
?>
```
