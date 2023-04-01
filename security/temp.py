import numpy as np
import cv2 as cv
import urllib.request

url = 'http://192.168.137.6/capture'

imgresponse = urllib.request.urlopen(url)
imgnp = np.array(bytearray(imgresponse.read()),dtype=np.uint8)
print(imgnp.shape)
frame = cv.imdecode(imgnp, cv.IMREAD_COLOR)
frame2 = frame.copy()
frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
print(frame.shape)

