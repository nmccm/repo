# GIT 

버전관리 프로그램

## 용어정의

- 메인 공유 저장소 : 개발자들이 공유하여 사용할 메일 저장소 (서버에 위치)
- 개인 저장소 : 개인이 사용할 저장소 (개발자 로컬에 위치)

## install for centos 6.8

```linux
# yum install git 
```

## 서버 저장소 생성 (메인 공유 저장소)

저장소에 접근할 SSH 계정이 필요하므로 우선 계정을 생성, 계정 전환을 해야한다.

```linux
# adduser note		
# su - note
```

저장소에 사용할 디렉토리 생성, 이동, 빈 저장소를 생성
		
```linux	
$ mkdir sample			
$ cd sample		 	
$ git init --bare
Initialized empty Git repository in /home/note/sample/	
$ ls -al
drwxrwxr-x. 7 note note 4096 2017-02-07 17:51 .
drwx------. 3 note note 4096 2017-02-07 17:50 ..
-rw-rw-r--. 1 note note   23 2017-02-07 17:51 HEAD
drwxrwxr-x. 2 note note 4096 2017-02-07 17:51 branches
-rw-rw-r--. 1 note note   66 2017-02-07 17:51 config
-rw-rw-r--. 1 note note   73 2017-02-07 17:51 description
drwxrwxr-x. 2 note note 4096 2017-02-07 17:51 hooks
drwxrwxr-x. 2 note note 4096 2017-02-07 17:51 info
drwxrwxr-x. 4 note note 4096 2017-02-07 17:51 objects
drwxrwxr-x. 4 note note 4096 2017-02-07 17:51 refs
```

## 클라이언트 저장소 생성 (개인 저장소)

메인 저장소로 사용한 서버가 아닌 타 서버에서 실행한다. 여기서는 composer 를 사용하여 일반 프로젝트 폴더를 생성, 등록한다.

```linux
...
```