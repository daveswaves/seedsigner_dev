# pip3 install opencv-python qrcode numpy

# opencv-python : QR code reader with easy webcam integration

# https://www.thepythoncode.com/article/generate-read-qr-code-python

# https://docs.opencv.org/4.x/


import qrcode
import numpy as np

data = "https://www.thepythoncode.com"

qr = qrcode.QRCode(version=1, box_size=10, border=4)

qr.add_data(data)

# compile the data into a QR code array
qr.make()

# print the image shape
print("The shape of the QR image:", np.array(qr.get_matrix()).shape) # The shape of the QR image: (37, 37)

# transfer the array into an actual image
img = qr.make_image(fill_color="white", back_color="black")

# save it to a file
img.save("qrcode_img.png")