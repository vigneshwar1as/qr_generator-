import qrcode
url=input("enter the url: ").strip()
file="*************.png" """give the location of the pic to be saved"""
qr =qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file)

print("qr code is generated")
