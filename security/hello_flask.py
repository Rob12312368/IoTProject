from flask import Flask
from flask import render_template, Response
import urllib.request
import cv2 as cv
import numpy as np
import threading
import sys
from datetime import datetime
from singlemotiondetector import SingleMotionDetector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('selectTime.html')

@app.route('/showValue')
def value():
    video = threading.Thread(target = stream)
    video.start()
    return render_template('showValue.html')

@app.route('/video')
def video():
    return Response(stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

def stream():
    url = 'http://192.168.137.91/capture'
    det = SingleMotionDetector()
    while True:
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        imgresponse = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(imgresponse.read()),dtype=np.uint8)
        frame = cv.imdecode(imgnp, cv.IMREAD_COLOR)
        frame2 = frame.copy()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        det.update(frame)
        result = det.detect(frame)
        if result != None:
            if result[1][2] - result[1][0] > 10:
                cv.rectangle(frame2, (result[1][0],result[1][1]), (result[1][2],result[1][3]), (0, 0, 255), 2)
                cv.imwrite(r'C:\Users\USER\Desktop\CSProject\images\Time'+current_time+'.jpg',frame2)
        ret, buffer = cv.imencode('.jpg', frame2)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

'''@app.route('/showValue')
def stram():
    url = 'http://192.168.137.101/capture'
    while True:
        imgresponse = urllib.request.urlopen(url)
        imgnp = np.array(bytearray(imgresponse.read()),dtype=np.uint8)
        frame = cv.imdecode(imgnp, cv.IMREAD_COLOR)

        cv.imshow('window',frame)

        key = cv.waitKey(5)
        if key == (ord('q')):
            break


        cv.destroyAllWindows()'''
        
app.debug = True
app.run()

