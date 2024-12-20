# 프로젝트 이름
계단 청소로봇(컴퓨터 비전 파트)

## 개요
이 프로젝트는 [문제 해결 동기]를 바탕으로 [핵심 기능]을 구현한 웹 애플리케이션입니다.  
주요 목표는 [성과 및 목적]을 달성하는 것이었습니다.

## 주요 기능
- [기능 1]
- [기능 2]
- [기능 3]

## 기술 스택
- 프론트엔드: React
- 백엔드: Flask
- 데이터베이스: MongoDB
- 배포: AWS EC2, Nginx

## 실행 방법
1. 저장소 클론: `git clone <repo-url>`
2. 객체 감지 서버 의존성 설치: `sudo pip3 install --upgrade pip`, `sudo python3 -m pip install -r requirements.txt`
3. 라즈베리 파이 의존성 설치: 
4. flaskServer폴더의 camera.py = 라즈베리 파이에 다운로드 후 Flask서버 실행: `python3 camera.py`
5. 아두이노 IDE
6. 객체 감지 서버(yolov5의 detect.py) 실행: `python3 yolov5/detect.py --weights yolov5/weightFile/blackWoodStair_autoContrast_50.pt  --img 416 --conf 0.8 --source http://192.168.105.238:5000/video_feed`

## 시연 영상
[시연 영상 링크](https://youtube.com)

## 상세 내용
더 자세한 프로젝트 설명은 [노션 링크](https://www.notion.so/13de84ee7a74802abb67dba4bf2e3be8?pvs=12)에서 확인할 수 있습니다.
