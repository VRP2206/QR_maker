import qrcode

url = input("Input Url: ")
name = input("Enter name of website: ")

image = qrcode.make(url)

image.save(name + ".png")