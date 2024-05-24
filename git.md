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

프로젝트 폴더로 이동 및 .gitignore 파일 작성
.gitignore 파일을 생성하며 커밋하지 않을 파일을 설정 (git init 이후에 만들어지는 .gitignore 는 적용되지 않으므로 캐쉬를 git 캐쉬를 삭제해야한 한다.

```linux
$ cd ~projectDir
$ vi .gitignore
```

저장소 생성 및 최초 파일 등록

```linux
$ git init				// .git 디렉토리가 생긴것을 확인할수 있다.
$ git add .				// commit file 들을 추가 (.은 모든 파일을 뜻함)
$ git reset <filename>	// 로컬 스테이지에 저장된 파일을 제거 unadd
$ git status			// 상태 확인
```

환경 설정

```linux
$ git config --list							// 환경 설정 확인
$ git config --global user.name 'name'		// commit user 설정
$ git config --global user.email 'email'	// commit user email 설정
$ git config color.ui 'auto'				// color 설정
```

커밋 및 원격 저장소 추가, Push

```linux
$ git commit -m <msg>										// commit with msg
$ git remote add origin note@1.1.1.1:/home/note/sample.git 	// remote 저장소 등록
$ git push origin master

// SSH 기본포트가 아닌 다른 포트로 ssh 접속할때 
$ git remote add origin ssh://note@1.1.1.1:1111/home/note/sample.git
```

## 등록된 원격 저장소 확인 및 삭제

등록된 원격 저장소 확인 및 삭제 방법 (remote add 시에 origin 으로 이름을 붙였기 때문에 삭제도 origin)

```linux
$ git remote -v
$ git remote remove origin
```

## 원격저장소 갱신

원격 저장소에는 존재하지만 내 작업공간에 없는 브랜치목록 갱신 방법

```linux
$ git fetch --prune origin
```

## 과거 커밋(과거 리비전)으로 돌아가기

등록된 원격 저장소 확인 및 삭제 방법 (remote add 시에 origin 으로 이름을 붙였기 때문에 삭제도 origin)

```linux
$ git log
commit 3a514296ef686ea274bee53f5c1a3daea1b3d1e5 (HEAD -> master, origin/master)
Author: webMain <master@domain.com>
Date:   Tue Apr 14 16:07:54 2020 +0900

    add test source
    brbr

commit 15fe2e67230f16364003f59e0c269164576f1df3
Author: EC2 Default User <ec2-user@domain.localdomain>
Date:   Tue Apr 14 14:31:13 2020 +0900

    init 

// 아래와 같이 처리하면 새로운 브런치를 만듬과 동시에 해당 브런치에 과거 커밋으로 돌아갈수 있다.
$ git checkout -b 15fe2e67230f16364003f59e0c269164576f1df3

// 원래 작업버전으로 돌아오려면 
$ git checkout 3a514296ef686ea274bee53f5c1a3daea1b3d1e5
```

## 브랜치 전체 리스트 확인 및 브랜치 이동 방법, 브랜치 삭제

```linux
$ git branch -a
$ git checkout <branch_name>
$ git branch -d <branch_name>	// 브랜치를 이동후 삭제하여야 한다.
$ git branch -D <branch_name>   // 브랜치 강제 삭제
Deleted branch issue1 (was e59bd24).
```

## 원격 저장소로부터 새로운 브랜치 생성
```linux
$ git checkout -b <branch_name> origin/master
```

## 원격 저장소 복제

최초 개인 저장소에서 소스를 푸시 한후, 타 개발자에게 소스를 전달할경우 사용된다. 아래 명령어를 사용할경우 해당 폴더를 기준으로 하위폴더에 sample 폴더가 생성된다.

```linux
$ git clone note@1.1.1.1:/home/note/sample.git sample
```

## .gitignore 수정후 재 적용 방법

간혹 사용도중 새로운 개발자가 들어오고, 그 개발자가 자신의 개발툴 환경설정 파일 (다른 개발자에게도 있는 파일)을 올리게 되면 .gitignore 파일에 등록해야하는데, 이 파일이 중간에 등록하면 효력을 발휘하지 못한다.
그럴때는 캐쉬를 삭제해 줌으로써 처리가능

```linux
$ git update-index --assume-unchanged WebApplication1/WebApplication1.csproj 
```

반대로 다시 트래킹을 하기 싶다면

```linux
git update-index --no-assume-unchanged WebApplication1/WebApplication1.csproj  
```

## 동일 브랜치에서 stash 방법

local master 브랜치 작업도중 새로운 일감을 처리해야될 경우 stash 사용하여 처리한다. 
아래는 master1 의 새로운 파일을 생성하고, 기존 first 파일을 수정한 상황에서 새로운 이슈가 들어왔다고 가정. 

```linux
$ vi master1		
$ vi first			
$ git status -u // -u 옵션은 untracked 파일까지 모두 숨겨준다.
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
```

현재 상태를 stash 를 한다.

```linux
$ git stash -u
Saved working directory and index state WIP on master: e711e9c temp commit
HEAD is now at e711e9c temp commit
```

상태를 보면 stash 덕분에 새로운 파일만 남고 기존에 수정하던 파일은 숨겨진다.

```linux
$ git status		
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        master1
nothing added to commit but untracked files present (use "git add" to track)
```

stash 리스트를 확인

```linux
$ git stash list		// list 확인
stash@{0}: WIP on master: e711e9c temp commit
```

```linux
// 새로운 이슈사항을 적용하고 commit & push
$ vi first	// 새로운 이슈사항 처리
$ git add first
$ git commit -m <msg>
$ git push origin master

// stash 복원 및 삭제
$ git stash apply
$ git stash clear	// stash list clear 

// clear 로 삭제되지 않을경우엔 drop 한다
$ git stash drop
``` 

## 새로운 브랜치를 생성하여 stash 사용

작업도중 새로운 이슈가 발생했을때 새로운 브랜치를 생성하여 작업하는 방법
새로운 브랜치를 체크아웃 (브랜치명은 이슈번호로 처리하는게 좋다)

```linux
git checkout -b issue1 origin/master
M       WebApplication1/Controllers/HomeController.cs
M       WebApplication1/Lib/Class1.cs
M       WebApplication1/Lib/Util.cs
Branch issue1 set up to track remote branch master from origin.
Switched to a new branch 'issue1'
```

## 코멘트 작성시 여러줄 입력방법
```linux
$ git commit -m '헬로우
> 파인
> 떙큐'
```

## 이미 GIT 서버에 올라간 파일을 더이상 추적(관리)되지 않도록 하는 방법
```linux
$ git update-index --assume-unchanged [file]
```

## 추적되지 않는 파일 리스트 확인
```linux
$ git ls-files -v | grep ^h
```

## 다시 추적되도록 하는 방법
```linux
$ git update-index --no-assume-unchanged [file]
```

## remote branch 갱신 및 브랜치 재생성 방법
```linux
dk_game_monitor> git checkout master
master> git branch -D release
master> git fetch --prune origin
master> git checkout -t origin/release
```

## 마지막 commit 메세지 변경
```linux
release> git commit --amend
```


## Trouble Shooting

만약 아래와 같은 에러가 발생하면 윈도우의 CR (carriage-Return) 때문에 발생하는 문제이므로 다음과 같이 설정하자.   

```linux
$ git config –-global core.autocrlf true
$ git config –-global core.autocrlf input
$ git config –-global core.autocrlf false
```


## image test

![sample_image](https://github.com/nmccm/repo/blob/master/cap8.png)
