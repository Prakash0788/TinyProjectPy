import pyqrcode
from pyqrcode import QRCode

# Text or URL to encode
s = "https://www.geeksforgeeks.org/"

# Create the QR code
url = pyqrcode.create(s)

# Save as SVG
url.svg("myqr.svg", scale = 8)

# Save as PNG
url.png("myqr.png", scale = 6)