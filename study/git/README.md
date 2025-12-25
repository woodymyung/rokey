---

# Git study

로컬 작업 환경에 Git을 설치하고 Github repository와 연결하는 과정을 정리한 문서입니다.

1. Git 설치 및 계정 설정
2. SSH Key 생성 및 등록
3. 로컬 작업 환경-Git 연결
4. 로컬 작업 환경-Github 연결
5. 작업 내용 관리

### 1. Git 설치 및 계정 설정

1. **로컬에 git 설치**

```bash
sudo apt update
sudo apt install git -y

```

로컬 환경에서 git을 구동할 수 있게 프로그램을 설치합니다.

* `sudo apt update` : 컴퓨터에 설치된 최신 버전의 프로그램의 명단을 불러오는 커맨드라인으로, 이 절차를 수행하지 않으면 과거 버전 주소로 가서 설치를 시도하려고 하여 설치에 실패할 수 있다.
* `sudo apt install git -y` : git을 설치하는 커맨드라인으로, `-y` 는 설치를 자동으로 허용해주기 위해 붙인다.

2. **Git 버전 확인**

```bash
git --version

```

3. **Git 계정 설정**

```bash
git config --global user.name "your-github-id"
git config --global user.email "your-github-email"

```

Git에서 작업하며 기록이 남을 때 사용할 이름과 이메일을 입력합니다. 실제로 Github에서 사용 중인 username, email을 입력해주는 것이 좋습니다. 

* `--global` 은 이 컴퓨터의 모든 프로젝트에 적용한다는 뜻

### 2. SSH Key 생성 및 등록

SSH(Secure Shell)는 네트워크상에서 컴퓨터에 안전하게 접속하고 원격으로 명령을 실행하거나 파일을 전송할 수 있게 해주는 보안 통신 프로토콜입니다. 이 SSH Key(Public)을 Github에 등록하여, 내 로컬 서버가 Github 서버의 데이터를 읽고 쓸 수 있는 권한을 얻게 됩니다.

1. **SSH 키 생성**

```bash
ssh-keygen -t ed25519 -C "your-github-email"

```

* `-t` : `ed25519` 암호화 타입 지정
* `-C` : `your-github-email` 이 작성된 부분을 대체

2. **SSH 키(public) 확인 및 복사**

```bash
cat ~/.ssh/id_ed25519.pub

```

이 커맨드라인 실행 후 나오는 문자열을 복사합니다.

> 참고: 리눅스 기준 /home/user/.ssh 폴더에 ssh key가 생성되는데, 이때 파일이 두 개 생성된 걸 확인할 수 있습니다. 이때 `.pub` 확장자가 붙은 파일에 있는 공개키를 등록해주어야 합니다.

3. **Github에 SSH 키 등록**

* [이 문서](https://www.google.com/search?q=https://github.com/KennethanCeyer/tutorial-git%3Ftab%3Dreadme-ov-file%23lock-ssh)를 참고해주세요.

4. **SSH 키가 잘 등록되었는지 확인**

```bash
ssh -T git@github.com

```

### 3. 로컬 작업 환경(폴더) 설정 및 Git 연결

만약 작업할 디렉토리가 있다면 해당 디렉토리로 이동해줍니다.

1. **로컬 디렉토리 생성 혹은 이동**

```bash
mkdir ~/your_dir_name
cd ~/your_dir_name

```

* `mkdir ~/your_dir_name` : 디렉토리 생성 (오타 수정: mkidr -> mkdir)
* `cd ~/your_dir_name` : 해당 디렉토리로 이동

2. **Git 초기화**

```bash
git init

```

이 커맨드라인을 통해 Git은 해당 디렉토리의 모든 변경사항을 감지하게 됩니다. 실제로 하위에 숨겨진 폴더 `.git` 이 생성된 걸 확인할 수 있습니다.

### 4. 로컬 작업 환경(폴더)와 Github Repository 연결

작업 내용을 연동하고 싶은 GitHub repository에서 SSH 주소를 복사합니다. 보통 repository 페이지 상단에 있습니다.

```bash
git remote add origin your_ssh_url

```

* `your_ssh_url` 부분에 SSH 주소를 붙여넣은 뒤, 위 커맨드라인을 실행합니다.
* 이는 내 컴퓨터에게 '앞으로 `origin` 이라는 이름을 부르면 저 Github 주소를 뜻하는 거야'라고 별명을 지어주는 과정입니다.

### 5. 작업 내용 관리

보통 여러 명의 개발자가 협업을 하기 때문에 서로의 변경사항이 겹치거나 충돌되지 않게 Branch로 공간을 나누어 작업합니다. 예를 들어 누군가는 로봇의 센서의 오류를 수정하는 업무를, 누군가는 로봇의 비전 AI 모델을 개선하는 업무를 해야 할 때 각자 Branch를 나누어 작업하면 각자 독립적인 작업 영역을 보장할 수 있습니다. 또한 실제 서비스되고 있는 프로덕션 환경에 바로 작업 내용이 반영되지 않고 충분한 코드 리뷰를 거치기 위해서도 별도의 Branch를 생성하여 작업합니다. 아래는 기본적인 용어를 정리한 것입니다.

* **Branch**: 별도의 작업 공간
* **Commit**: 작업 내용을 적절한 단위별로 묶는 행위로, 일종의 분기점입니다. 이후 작업을 하다 이전 버전으로 되돌리고 싶을 때 해당 Commit을 선택하여 revert(혹은 reset)할 수 있습니다.
* **Push**: 내가 나의 컴퓨터(로컬)에서 작업한 내용을 Github의 원격 저장소(Origin)에 업데이트하는 행위입니다.
* **Pull**: Github의 원격 저장소(Origin)에서의 가장 최신 내용을 나의 컴퓨터(로컬)에 불러와서 작업할 환경을 최신화하는 행위입니다.
* **Merge**: 두 개의 Branch를 합쳐 하나로 만드는 행위입니다. 예컨대 A Branch에서 로봇 센서 오류를 수정한 내용을 Origin에 Push하면, Origin의 Main Branch에서 Merge하여 실제 서비스되고 있는 환경에 수정된 내용을 반영합니다.

아래 내용은 이런 작업 과정에 필요한 명령어(커맨드라인)를 정리한 내용입니다.

#### 5.1. Branch 생성 및 변경

1. **작업할 Branch 생성**

```bash
git checkout -b your-branch-name

```

* `your-branch-name` 자리에 내가 설정하고 싶은 Branch 이름을 넣습니다. Gemini에 물어본 결과, 기능을 알 수 있게 이름을 구성한다고 하네요. Github의 repository에 있는 다른 Branch와 이름이 겹치지 않게 설정해야 합니다.

2. **현재 내가 작업 중인 Branch 상태 확인**

```bash
git status

```

* 현재 내가 작업 중인 Branch와 아직 Commit 되지 않은 변경 내용을 확인할 수 있습니다.

3. **다른 Branch로 이동**

```bash
git checkout your-branch-name

```

* 내가 작업 중인 Branch를 변경하고 싶을 때 이 커맨드라인을 사용합니다.

#### 5.2. Commit 생성 및 변경

1. **모든 변경사항을 Staged 단계로 이동**

```bash
git add .

```

* Commit 하기 전, 이 변경 내용을 staged 상태로 만드는 커맨드라인입니다.
* 물건을 사기 전, 장바구니에 물건을 담는 것과 비슷한 행위입니다.


* 이때 `.` 은 현재 만들어진 모든 변경사항을 의미합니다.

2. **현재 Staged 단계의 changes를 하나의 Commit으로 합치기**

```bash
git commit -m "your-commit-message"

```

* `your-commit-message` 자리에는 이 변경사항이 어떤 것인지 직관적으로 이해될 수 있게 합니다.
* 참고로 Cursor 에디터에서는 commit message를 자동으로 만들어주는 기능이 있습니다.

3. **Commit 되돌리기 (Reset vs Revert)**
작업을 되돌리는 방법은 크게 두 가지가 있으며, **이미 원격 저장소(Github)에 Push 했는지 여부**가 가장 중요합니다.

**(1) 원격 저장소에 Push 하지 않은 경우 (Local 작업)**
나만 알고 있는 로컬의 기록을 지우는 것이므로 `reset` 을 사용하여 과감하게 되돌릴 수 있습니다.

```bash
# 가장 최신 commit을 취소하고, 변경 내용은 작업 공간(Working directory)에 보존 (가장 많이 씀)
git reset --soft HEAD~1

# 가장 최신 commit을 취소하고, 변경 내용까지 모두 삭제 (주의 필요)
git reset --hard HEAD~1

```

* `HEAD~1` 은 현재 시점(HEAD)에서 1단계 뒤로 간다는 뜻입니다. (즉, 방금 한 Commit 취소)

**(2) 원격 저장소에 이미 Push 한 경우 (협업 중)**
이미 Github에 올라간 Commit을 `reset` 으로 강제 삭제하면, 동료들의 코드와 꼬이게 됩니다. 이때는 **"취소했다는 새로운 Commit"**을 생성하는 `revert` 를 써야 합니다.

```bash
git revert commit-id

```

* `commit-id`: 되돌리고 싶은 특정 Commit의 ID입니다. (예: `a1b2c3d`)
* 이 명령어를 실행하면 *"Revert ... commit-name"* 이라는 새로운 Commit이 생성되며, 코드는 이전 상태로 돌아가지만 기록은 안전하게 남습니다.

#### 5.3. 로컬의 Commit들을 Github의 Origin branch 로 올리기

```bash
git push origin your-branch-name

```

* 지금까지 작업한 내용(Commit)을 작업 중인 로컬 Branch에서 Github의 Origin Branch로 올려 최신화하는 커맨드라인입니다.
* Push 이후 작업자는 Github의 Repository 에서 Pull Request를 하여, 다른 작업자들에게 '내 작업 내용을 프로덕션에 반영해줘'라는 요청을 올리게 됩니다.

```bash
git push origin main

```

* 만약 내가 작업 중인 Branch의 origin이 아니라, main의 origin에 올리게 되면 내가 작업한 내용이 자동으로 main에 적용되게 됩니다.
* 보통은 권한이 있는 작업자만 origin의 main Branch에 작업 내용을 반영할 수 있게 설정합니다.
