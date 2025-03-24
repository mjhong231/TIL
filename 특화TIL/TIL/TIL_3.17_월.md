[1.소개]

webRTC: 웹 브라우저 환경 및 Android, IOS 애플리케이션에서도 사용 가능한 비디오, 음성 및 일반 데이터가 피어간에 실시간으로 전송되도록 지원하는 오픈 소스

[2.프로토콜]
openvidu


2-1. ICE(Interactive Connectivity Establishment)
: 브라우저가 peer를 통한 연결이 가능하도록 해주는 프레임 워크 -> 두 클라이언트 간 최적의 통신 경로 찾기 활용할 수 있음


2-2.  STUN(Session Traversal Utilities for NAT) 서버

클라이언트 자신의 Public Address(IP:PORT)를 알려준다.

peer간의 직접 연결을 막는 등의 라우터의 제한을 결정하는 프로토콜 (현재 다른 peer가 접근 가능하지 여부 결정)
-클라이언트 Public  Adress와 라우터의 NAT 뒤에 있는 클라이언트가 접근 가능한지에 대한 답변을 STUN 서버에 요청

2-3. NAT
단말에 공개 IP주소를 할당하기 위해 사용

몇몇의 라우터들은 Symmetric NAT이라고 불리우는 제한을 위한 NAT을 채용한다. 즉, peer들이 오직 이전에 연결한 적 있는 연결들만 허용한다. 따라서 STUN서버에 의해 공개 IP주소를 발견한다고 해도 모두가 연결을 할수 있다는 것은 아니다. (위의 설명에서 STUN 서버에 다른 peer가 접근 가능한지 여부를 요청하는 이유)

2-4. TURN(Traversal Using Relays around NAT) 서버 (차선책)

TURN 서버와 연결하고 모든 정보를 그 서버에 전달하는 것으로 Symmetric NAT 제한을 우회하는 것을 의미한다.

이를 위해 TURN 서버와 연결을 한 후 모든 peer들에게 저 서버에 모든 패킷을 보내고 다시 나(TURN서버)에게 전달해달라고 해야 한다.

명백히 오버헤드가 발생하므로 이 방법은 다른 대안이 없을 경우만 사용해야 한다.

2-5. SDP(Session Description Protocol)
해상도나 형식, 코덱, 암호화등의 멀티미디어 컨텐츠의 연결을 설명하기 위한 표준이다.

두 개의 peer가 다른 한쪽이 데이터가 전송되고 있다는 것을 알게 해준다.

기본적으로 미디어 컨텐츠 자체가 아닌 컨텐츠에 대한 메타데이터 설명이다.

기술적으로 보자면 SDP 는 프로토콜이 아니다. 그러나 데이터 포멧은 디바이스간의 미디어를 공유하기 위한 연결을 설명하기 위해 사용한다.


MediaStream - 카메라/마이크 등 데이터 스트림 접근
RTCPeerConnection - 암호화 및 대역폭 관리 및 오디오 또는 비디오 연결
RTCDataChannel - 일반적인 데이터 P2P통신
이 3가지의 객체를 통해서 데이터 교환이 이뤄지며 RTCPeerConnection들이 적절하게 데이터를 교환할 수 있게 처리하는 과정을 시그널링(Signaling) 이라고 한다.

OpenVidu 
: WebRTC를 기반으로 동작하는 프레임워크

Jsoup
HTML 파싱 라이브러리
:위키 낱말 사전에 있는 단어들을 크롤링하여 랜덤 닉네임 생성