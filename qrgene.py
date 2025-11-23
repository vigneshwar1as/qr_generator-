import qrcode
url=input("enter the url: ").strip()
file="C:\\Users\\sarun\\Desktop\\vit coll\\gene\\12.11.25\\qrcode.png"
qr =qrcode.QRCode()
qr.add_data(url)
img=qr.make_image()
img.save(file)
print("qr code is generated")