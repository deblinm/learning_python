import qrcode

user_input = input("Please enter the url for which QR code will be generated: ")

qr_code=qrcode.QRCode(version=1,
                      error_correction=qrcode.constants.ERROR_CORRECT_H,
                      box_size=10,
                      border=10)

qr_code.add_data(user_input)
qr_code.make(fit=True)
img = qr_code.make_image(fill_color="black", back_color="white")
img.save("../Files/MY_QR_Code.jpeg")
print("QR Code generated successfully!")

