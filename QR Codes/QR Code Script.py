# Import QR Code library
import qrcode

qr = qrcode.QRCode(
  version=1,
  error_correction = qrcode.constants.ERROR_CORRECT_H,
  box_size=15,
  border=5
)

# Data about you 
data = 'https://www.gannett-cdn.com/presto/2020/03/24/USAT/866ee04e-9c56-4f84-ada3-e0c0ea0c0fb3-XXX_FUN_SMARTPET_041814.JPG?crop=3734,2100,x0,y29&width=3200&height=1680&fit=bounds'
name=input('~ Ahmed Serag')

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save it somewhere, change the extension as needed:
# img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
img.save('barcode.png')