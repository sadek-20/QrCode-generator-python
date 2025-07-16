import qrcode

data = input('enter the text or url : ').strip()
fileName = input('enter the filename : ')

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)

image = qr.make_image(fill_color='blue', back_color='white')
image.save(fileName)
print(f'Qrcode saved as {fileName}')
