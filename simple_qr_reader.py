import requests
import cv2

# URL of the image who has the QR code
url = 'http://targeturl:targetport/'

s = requests.Session() # Optional
myheaders = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.2651.74'}
s.headers.update(myheaders)

# Download image
img_data = s.get(url, headers=myheaders).content 

# Save image
with open('qr.png', 'wb') as handler: 
    handler.write(img_data)

# Read QR
qr_image = cv2.imread('qr.png')
qr_detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode  = qr_detector.detectAndDecode(qr_image)

if data is not None:
    print(f"Data from QRCode: \n {data} ")

