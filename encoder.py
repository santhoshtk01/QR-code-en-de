# Program to create a QR code encoder using qrcode module

import qrcode
from PIL import Image

data = "Hello"
img = qrcode.make(data=data)
img.save('qr-codes/img-1.jpg')

image = Image.open('qr-codes/img-1.jpg')
image.show()
