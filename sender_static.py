import serial
import hashlib
from PIL import Image
import io


with serial.Serial('/dev/ttyUSB0', 115200) as ser:
    image =  Image.open('./images/gray.jpg')
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG')
    img_bytes = buffer.getvalue()
    ser.write(img_bytes)
    print(hashlib.sha224(img_bytes).hexdigest(), len(img_bytes))

