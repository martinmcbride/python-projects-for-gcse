from PNGImage import PNGImage

size = 1000

im = PNGImage(psize=(size, size), size=(14, 14), origin=(-4, -4))
x = -0.1
y = 0
for i in range(100000):
    x, y = 1 - y + abs(x), x
    im.setPixelbyPosition(x, y)
im.write('gingerbread.png')
