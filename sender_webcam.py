import serial
import hashlib
import cv2

with serial.Serial('/dev/ttyUSB0', 115200) as ser: 
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    if result:
        result, image = cv2.imencode('.jpg', image)
        if result:
            img_bytes = image.tobytes()
            ser.write(img_bytes)    
    print(hashlib.sha224(img_bytes).hexdigest(), len(img_bytes))
