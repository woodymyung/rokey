# Git study 
로컬 작업 환경에 Git을 설치하고 Github repository와 연결하는 과정을 정리한 문서입니다.

## Terminology
1. Git: 프로그래밍 시, 작업 버전을 관리할 수 있는 프로그램
2. Github: git으로 버전을 관리하며 다른 프로그래머와 협업하는 과정을 쉽게 도와주는 툴

## Summary
git 설치 및 github 연결은 아래 과정으로 진행됩니다.
1. 로컬 환경에 git 설치 및 git 계정 설정
2. ssh 키 생성 및 github에 등록
3. git 작업 디렉토리 세팅
4. branch 생성
5. commit
6. push
7. merge

   
### 1. Git 설치 및 계정 설정 
로컬 환경에서 git을 구동할 수 있게 프로그램을 설치합니다. 

```
sudo apt update
sudo apt install git -y
``` 

* `sudo apt update` : 컴퓨터에 설치된 최신 버전의 프로그램의 명단을 불러오는 커맨드라인으로, 이 절차를 수행하지 않으면 과거 버전 주소로 가서 설치를 시도하려고 하여 설치에 실패할 수 있다.
* `sudo apt install git -y` : git을 설치하는 커맨드라인으로, `-y`는 설치를 자동으로 허용해주기 위해 붙인다. 

어떤 버전이 설치되었는지 확인해줍니다. 
```
git --version
``` 
* 현재 어떤 버전이 설치되었는지 확인하는 커맨드라인이다. 

떤 변경사항을 올릴 때 비밀번호 없이 통과할 수 있게 해줍니다. 
누가 작업했는지 남기기 위한 절차이자, Github 서버에 내 컴퓨터를 신뢰할 수 있는 기기로 등록하는 절차입니다. 
###이름과 이메일 등록
커밋(Commit) 기록에 '작성자'로 남기기 위함입니다. Github 계정 이메일과 동일하게 맞추는 것이 좋습니다. 
```
git config --global usre.name "your-github-id"
git config --global user.email "your-github-email" 
```
* `--global`은 이 컴퓨터의 모든 프로젝트에 적용한다는 뜻

### 2. SSH Key 생성 및 등록
SSH(Secure Shell)는 네트워크상에서 컴퓨터에 안전하게 접속하고 원격으로 명령을 실행하거나 파일을 전송할 수 있게 해주는 보안 통신 프로토콜입니다. 이 SSH Key(Public)을 Github에 등록하여, 내 로컬 서버가 Github 서버의 데이터를 읽고 쓸 수 있는 권한을 얻게 됩니다. 

1. SSH 키 생성
```
ssh-keygen -t ed25519 -C "your-github-email"
```
* `-t` : `ed25519` 암호화 타입 지정 
* `-C` : `your-github-email`이 작성된 부분을 대체 

2. SSH 키(public) 확인 및 복사
```cat ~/.ssh/id_ed25519.pub``` 
* 이 커맨드라인 실행 후 나오는 문자열을 복사합니다. 

> 참고: 리눅스 기준 /home/user/.ssh 폴더에 ssh key가 생성되는데, 이때 파일이 두개 생성된 걸 확인할 수 있습니다. 이때 `.pub` 확장자가 붙은 파일에 있는 공개키를 등록해주어야합니다. 
 
3. Github에 SSH 키 등록
키 등록은 [이 문서](https://github.com/KennethanCeyer/tutorial-git?tab=readme-ov-file#lock-ssh)를 참고해주세요. 
* Github 웹사이트 등록 -> 우측 상단 프로필 클릭 -> Settings 
* 좌측 메뉴의 SSH and GPG keys 클릭 -> New SSH Key 버튼 클릭
* Title: 원하는 이름 
* Key: 복사한 공개키 붙여넣기

4. 연결 테스트: 
ssh -T git@github.com 



1. sudo apt update 를 먼저 해야 하는 이유
결론부터 말씀드리면, '내 컴퓨터에 저장된 설치 가능한 소프트웨어 명단(Index)' 을 최신으로 업데이트하기 위해서입니다.

동기화 과정: 리눅스 저장소(Repository)에는 수만 개의 프로그램이 있고, 수시로 버전이 올라갑니다. update 는 프로그램을 실제로 설치하는 게 아니라, "지금 어떤 프로그램이 어떤 버전으로 어디에 있는지" 적힌 최신 카탈로그를 다운로드하는 과정입니다.

오류 방지: 만약 update 를 하지 않고 예전 명단만 가지고 install 을 시도하면, 서버에는 이미 삭제된 구버전 주소로 접속하려다 '404 Not Found' 같은 에러가 발생할 수 있습니다.

의존성 해결: 설치하려는 프로그램이 필요로 하는 다른 도구(의존성)들의 최신 위치도 이 명단에 들어있기 때문에 필수적인 단계입니다.

2. sudo apt install git 의 기능과 역할
사용자께서 짐작하신 내용이 맞습니다! 하지만 단순한 '라이브러리' 하나를 까는 것보다 조금 더 넓은 개념입니다.

무엇이 설치되나요?
실행 파일 (Binary): 터미널에서 git 이라는 명령어를 쳤을 때 실행될 수 있는 프로그램 본체 가 설치됩니다. (보통 /usr/bin/git 경로에 위치하게 됩니다.)

의존성 라이브러리: git 이 돌아가기 위해 필요한 다른 작은 소프트웨어 조각들도 함께 설치됩니다.

환경 설정: 터미널 어디에서든 git 명령어를 인식할 수 있도록 시스템 경로(PATH) 가 설정됩니다.

터미널에서의 작동 원리
sudo apt install git 을 완료하면, 이제 리눅스 시스템은 사용자가 터미널에 git 이라고 입력했을 때 "아, 아까 설치한 그 실행 파일을 돌리라는 거구나!" 라고 이해하게 됩니다.

참고: git 은 단순한 라이브러리가 아니라, 코드의 변경 이력을 관리하는 독립적인 '버전 관리 시스템(Version Control System)' 프로그램입니다. 


##브랜치 
여러명의 개발자들이 동시에 작업할 때 서로의 변경사항이 충돌되지 않게 브랜치의 형태로 공간을 나누어서 작업한다. 
각자 로컬에서 작업한 커스텀브랜치들을 일정 단위로 origin의 커스텀브랜치에 push한 뒤, 그 origin의 커스텀브랜치들을 origin의 main 브랜치에 merge 하는 식으로 동작한다.
그리고 내가 작업 중인 내용이 origin/main 으로 반영되지 않게끔 하는 것. 

1. origin/main: 실제 프로덕션에 반영되어, live 중인 최신 상태 
2. main: ori


###작업할 브랜치 생성 및 변경 
1. 새로운 브랜치를 만들고 싶거나, 현재 만들어진 브랜치가 없을 때
```
git checkout -b your-branch-name
``` 

2. 다른 브랜치로 이동하고 싶을 때
```
git checkout your-branch-name
``` 


현재 내가 작업 중인 브랜치와, 해당 브랜치의 commit되지 않은 변경사항 확인
```
git status 
``` 

해당 브랜치의 변경 사항을 staged 단계로 이동. 즉 하나의 commit에 묶을 변경사항들을 장바구니에 넣는 단계 
```git add . 
```

현재 staged된 changes 들을 commit.
```
git commit -m "your-commit-message"
``` 

origin의 branch로 변경된 내용을 업데이트 
```
git push origin your-branch-name 
``` 

origin의 main branch 에 머지 요청 
```
git push origin main 
``` 
