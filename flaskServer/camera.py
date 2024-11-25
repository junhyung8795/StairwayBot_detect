
from flask import Flask, Response, request
from picamera2 import Picamera2
import cv2
import serial
import json
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv(verbose=True)
ARDUINO_PORT = os.getenv("ARDUINO_PORT")

arduino = serial.Serial(ARDUINO_PORT, 9600)
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()
def generate_frames():
    while True:
        frame = picam2.capture_array()
        
        ret, buffer = cv2.imencode('.jpg', frame)
        
        if not ret:
            print("Frame encoding failed")
            continue
        
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/detections', methods=['POST'])
def detections():
    data = request.json
    arduino.write(json.dumps(data).encode('utf-8'))
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')


