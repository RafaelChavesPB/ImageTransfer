import io
import serial
import hashlib
from PIL import Image

with serial.Serial('/dev/ttyUSB1',115200) as ser:
    img_bytes = b''
    while not ser.in_waiting:
        continue
    img_bytes = ser.read_until(b'\xff\xd9')
    image = Image.open(io.BytesIO(img_bytes))
    image.show()
    print(hashlib.sha224(img_bytes).hexdigest(), len(img_bytes))





