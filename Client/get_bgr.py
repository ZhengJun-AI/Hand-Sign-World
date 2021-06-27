import cv2
import time

ipconf = 'http://192.168.137.39:4747/mjpegfeed?1920x1080'
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
# old = time.time()
if ret:
    time.sleep(1)
    ret, frame = cap.read()
    cv2.imwrite('bgr.jpg',frame)
cap.release()
    