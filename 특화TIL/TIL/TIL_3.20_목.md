"use client"; // 클라이언트 컴포넌트 설정

- Next.js의 App Router(app/)는 기본적으로 서버 컴포넌트
- 하지만 브라우저 API(navigator.mediaDevices.getUserMedia)를 사용하려면 클라이언트 컴포넌트여야 함 -> "use client";를 추가하면 이 파일이 클라이언트에서 실행


웹소켓 -> STOMP

웹RTC -> 참가자가 여러명일 수 있으니까 SFU

브라우저에서 녹음하기 (MediaRecorder API)

-> WebRTC 스트림을 녹음하려면 MediaRecorder API를 사용
녹음된 데이터를 Blob 형태로 변환하여 백엔드에 업로드