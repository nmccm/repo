# GIT 

버전관리 프로그램

## install for centos 6.8

```linux
# yum install git 
```

## 저장소 생성

저장소에 접근할 SSH 계정이 필요하므로 우선 계정을 생성, 계정 전환을 해야한다.

```linux
# adduser note		
# su - note
```

저장소에 사용할 디렉토리 생성, 이동, 빈 저장소를 생성
		
```linux	
# mkdir note			
# cd note				 	
# git init --bare	
```

