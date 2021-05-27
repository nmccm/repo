# WSL

wsl ubuntu 에서 github 를 복제했을경우 기본적인 값으로 bash shell 에 브랜치명이 표기되기 않지만, 아래의 방법으로 브랜치명을 표시할수 있다.

아래의 내용을 홈디렉토리의 .bashrc 맨 하단에 추가한다.

```linux
nmccm@DESKTOP-T0AEAIV ~ $ pwd
/home/nmccm
nmccm@DESKTOP-T0AEAIV ~ $ tail -n 5 .bashrc

parse_git_branch() { git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/' ; }
export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "

nmccm@DESKTOP-T0AEAIV ~ $
```
