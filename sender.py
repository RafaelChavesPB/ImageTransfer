import serial
import hashlib
from PIL import Image
import io


ser = serial.Serial('/dev/ttyUSB0', 115200)
image =  Image.open('gray.jpg')
buffer = io.BytesIO()
image.save(buffer, format='JPEG')
img_bytes = buffer.getvalue()
ser.write(img_bytes)
print(hashlib.sha224(img_bytes).hexdigest())
print(len(img_bytes))
