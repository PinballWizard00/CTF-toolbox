from PIL import Image
from io import BytesIO
import requests
from pyzbar.pyzbar import decode
import base64
import cv2
# Reading multiple QR without writing to disk. 

# URL of the image who has the QR code
url = "http://url:port/"
s = requests.Session()
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.2651.74'}
s.headers.update(headers)
data = ""
last_data = ""
flag = ""
i = 0
while i < 10000:
    image_data = s.get(url, headers=headers).content
    # Open image
    image = Image.open(BytesIO(image_data))
    # Read QR
    decoded_objects = decode(image)
    # Concatenate results
    for obj in decoded_objects:
        data = obj.data.decode("utf-8")
    if data is not None:
        if last_data == data:
            i = 10000
        else:
            flag = flag + data
            last_data = data

print(flag)
