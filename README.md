# 프로젝트 이름
계단 청소로봇(컴퓨터 비전 파트)

## 개요
객체 탐지 서버, 라즈베리 파이, 아두이노, 그리고 YOLOv5를 이용하여 기존에 청소 로봇이 가지지 못한 계단을 인식하는 기능 개발. 라즈베리 파이에서 계단의 위치 정보를 송신하고 아두이노에서 수신하는 백엔드 api설계.
계단을 향해 이동하기 위해 모델 학습(.pt 파일)과 데이터 송수신 구조 개발.

## 주요 기능
- 계단을 인식하고 라벨링된 바운딩 박스 생성
- 객체 감지 서버, 라즈베리 파이의 Flask 서버, 아두이노 간 데이터 송수신을 통한 객체 감지 성능 최적화
- 계단의 위치정보(계단과 로봇 사이의 거리, 계단이 기울어진 정도, 바운딩 박스의 중심 x좌표, 계단 인식 여부) 연산, 실시간 갱신

## 기술 스택
- 객체 탐지 및 영상처리: Python, Opencv, YOLOv5, Roboflow, GoogleColab
- 백엔드: Flask
- 라즈베리 파이 원격 접속: Real VNC
- arduinoTestCode 작성: C++


## 실행 방법
1. 저장소 클론: `git clone https://github.com/junhyung8795/StairwayBot_detect.git`
2. 객체 감지 서버 의존성 설치: `sudo pip3 install --upgrade pip`, `sudo python3 -m pip install -r requirements.txt`
3. 라즈베리 파이 의존성 설치:`sudo apt install -y python3-picamera2`, `pip3 install flask`
4. arduinoTestCode는 아두이노에 다운로드 후 ArduinoJson 헤더 파일 다운로드(아두이노 하드웨어는 UNO가 아닌 Mega를 사용하는 것을 추천합니다. UNO도 테스트 코드는 실행 가능하지만 바퀴 모터나 여러 로직이 섞일 경우 Mega가 효율적입니다.)
5. flaskServer 폴더의 camera.py = 라즈베리 파이에 다운로드 후 Flask 서버 실행: `python3 camera.py`
6. 아두이노 IDE에서 arduinoTestCode 실행 후 시리얼 모니터 실행
7. 객체 감지 서버(yolov5의 detect.py) 실행 예시(실행 위치 StairwayBot_detect/): `python3 yolov5/detect.py --weights yolov5/weightFile/blackWoodStair_autoContrast_50.pt  --img 416 --conf 0.8 --source http://192.168.xxx.xxx:5000/video_feed`

## 시연 영상
객체 감지 데이터 송수신 시연 영상: https://youtu.be/OJPKubmBZKU
객체 감지 영상처리 시연 영상: https://youtu.be/ss0D5uS3Y8o

## 상세 내용
더 자세한 프로젝트 설명은 [노션 링크](https://www.notion.so/13de84ee7a74802abb67dba4bf2e3be8?pvs=12)에서 확인할 수 있습니다.
