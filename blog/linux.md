Ubuntu 22.04 의 블루투스 자체가 켜지지 않는 문제 해결

### 배경
로봇 개발의 표준 프레임워크인 ROS는 Linux와 호환되고 MacOS를 지원하지 않아, 이번에 Linux 체제를 지원하는 컴퓨터를 구매하게 되었다. 또한 두산 Rokey 캠프의 커리큘럼상 Ubuntu 22.04 를 설치해야해서 해당 버전을 설치했다(가장 최신 버전은 Ubuntu 24.04 LTS이다)

### 본론 
Lenovo의 Legion 모델을 노트북으로 구매 후, 어찌저찌 도움을 받아 Ubuntu 22.04 버전까지는 설치했다. 그런데 블루투스 자체가 켜지지 않는 현상이 있었다. 이를 해결하고자 다양한 방법들을 시도했다. 그래서 Gemini에게 물어보고 Reddit을 구글링했는데 여러 해결 방법들이 먹히지 않았다. 

예를 들어: 
```bash
rfkill list 
``` 
이런 명령어로 Bluetooth 항목이 Block 되어있는지 확인해본다거나, 
```bash
sudo modprobe -r btsub
sudo modprobe btusb
``` 
커널 모듈을 재설치한다거나, 
```bash
sudo dmesg | grep -i bluetooth 
```
커널 관련 어떤 로그들이 있는지 확인한다거나. 

그리고 이런 로그를 복사하여 다시 Gemini 에게 도움을 청했으나 모든 해결책이 먹히지 않았다. 간헐적으로 블루투스 On에 성공한 건 
```bash
sudo modprobe -r btusb mt7925e && sleep 10 && sudo modprobe mt7925e && sudo modprobe btusb && sudo systemctl restart bluetooth
``` 
이런 명령어였다. 그런데 이마저도 절전모드가 되거나 컴퓨터가 재부팅되면 해당 명령어를 실행해도 효과가 없었다. </br>
이런 로우레벨의 하드웨어에 대한 이해가 없었던 나는 미칠 지경이었다. 그래서 아예 블루투스 사용을 포기하려고 마음 먹었으나 집착적으로 찾아낸 결과 문제를 해결하게 되었다. 
이것 저것 시도하다가 내가 사용하고 있는 노트북의 하드웨어 제조사 관련 에러 메시지를 Gemini 가 인식해주었고, 이 키워드로 구글링을 하고, 해외 커뮤니티 글을 타고 들어간 결과! 

### 해결 
https://github.com/LuanAdemi/mediatek7925e-bluetooth-fix  

결국 내가 사용하는 노트북의 리눅스 시스템이 MediatTek 라는 제조사의 와이파이, 블루투스 콤보카드를 네트워크 카드가 아니라 카메라나 휴대폰 같은 미디어 장치로 착각했다는 게 주 원인이었다. 

대화 내용: https://gemini.google.com/share/88ac9da1199d 

그래서? 결국 구글링으로 해결했다는 기쁜 소식. 나와 비슷한 문제를 겪고 있는 사람들도 알면 좋겠다.