# GIT 

버전관리 프로그램

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

저장소에 사용할 디렉토리 생성, 이동, 빈 저장소를 생성 (저장소 디렉토리명은 관행상 .git 를 붙이도록 한다)
		
```linux	
$ mkdir sample.git			
$ cd sample.git		 	
$ git init --bare
Initialized empty Git repository in /home/note/sample.git/	
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

프로젝트 폴더로 이동하여 개인저장소를 생성하고, 작업된 파일들을 푸시한다.

```linux
$ cd ~projectDir
$ vi .gitignore												// .gitignore 파일을 생성하며 커밋하지 않을 파일을 설정 (git init 이후에 만들어지는 .gitignore 는 적용되지 않으므로 캐쉬를 git 캐쉬를 삭제해야한 한다.)
$ git init													// .git 디렉토리가 생긴것을 확인할수 있다.				
$ git add .													// commit file 들을 추가 (.은 모든 파일을 뜻함)
$ git status												// commit status 확인
$ git config --list											// 환경 설정 확인
$ git config --global user.name 'name'						// commit user 설정
$ git config --global user.email 'email'					// commit user email 설정
$ git config color.ui 'auto'								// color 설정
$ git commit -m 'msg'										// commit with msg
$ git remote add origin note@1.1.1.1:/home/note/sample.git 	// remote 저장소 등록
$ git push origin master
```

## 등록된 원격 저장소 확인 및 삭제

등록된 원격 저장소 확인 및 삭제 방법

```linux
$ git remote -v
$ git remote remove origin
```

## 브랜치 전체 리스트 확인 및 브랜치 이동 방법, 브랜치 삭제

```linux
$ git branch -a
$ git checkout <branch_name>
$ git branch -d <branch_name>	// 브랜치를 이동후 삭제하여야 한다.
$ git branch -b <branch_name> origin/master
Deleted branch issue1 (was e59bd24).
```


## 원격 저장소 복제

최초 개인 저장소에서 소스를 푸시 한후, 타 개발자에게 소스를 전달할경우 사용된다. 아래 명령어를 사용할경우 해당 폴더를 기준으로 하위폴더에 sample 폴더가 생성된다.

```linux
$ git clone note@1.1.1.1:/home/note/sample.git sample
```

## stash

local master 브랜치에서 작업도중 새로운 일감을 처리해야될 경우 stash 사용하여 처리한다. 아래는 기존 master 브랜치에서 newWorkFile 을 생성하고 기존 first 파일을 수정한다음, 새로운 일감을 처리할때 stash 사용법을 다룬다.

```linux
$ vi master1		// 새로운 파일을 생성하고
$ vi first			// 기존 파일을 수정한다.
$ git status 
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   first

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        master1

no changes added to commit (use "git add" and/or "git commit -a")

$ git stash
Saved working directory and index state WIP on master: e711e9c temp commit
HEAD is now at e711e9c temp commit

$ git status		// stash 명령 덕분에 새로운 파일만 남고 기존에 수정하던 파일은 숨겨진다.
On branch master
Your branch is up-to-date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        master1

nothing added to commit but untracked files present (use "git add" to track)

$ git stash list		// list 확인
stash@{0}: WIP on master: e711e9c temp commit

// 새로운 이슈사항을 적용하고 commit & push
$ vi first	// 새로운 라인에 추가
$ git add first
$ git commit -m 'first bug fix'
$ git push origin master

// stash 복원
$ git stash apply
$ git stash clear	// stash list clear 
``` 

## Trouble Shooting

만약 아래와 같은 에러가 발생하면 윈도우의 CR (carriage-Return) 때문에 발생하는 문제이므로 다음과 같이 설정하자.

```linux
$ git config –-global core.autocrlf true
$ git config –-global core.autocrlf input
$ git config –-global core.autocrlf false
```