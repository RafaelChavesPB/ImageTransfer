import serial
import hashlib
import cv2

ser = serial.Serial('/dev/ttyUSB0', 115200)
cam_port = 0
cam = cv2.VideoCapture(cam_port)
result, image = cam.read()
if result:
    result, image = cv2.imencode('.jpg', image)
    if result:
        img_bytes = image.tobytes()
        ser.write(img_bytes)    
print(hashlib.sha224(img_bytes).hexdigest(), len(img_bytes))
