import qrcode as qr

a="https://github.com/pranjaltiwari029"
b=qr.make(a)
b.save('github.png')