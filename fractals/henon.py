from PNGImage import PNGImage

size = 3000

im = PNGImage(psize=(size, size), size=(3, 1), origin=(-1.5, -0.5))
x = 0
y = 0
for i in range(1000000):
    x, y = y+1-1.4*x*x, 0.3*x
    im.setPixelbyPosition(x, y)
im.write('henon.png')
