# Program to decode a QR code

from pyzbar.pyzbar import decode
from PIL import Image

image = Image.open('qr-codes/img-1.jpg')

result = decode(image)
print(result[0].data)


