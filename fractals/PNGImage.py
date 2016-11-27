from PIL import Image


class PNGImage:

    def __init__(self, psize, size, origin=(0, 0), color=(0, 0, 0)):
        self.psize = psize
        self.size = size
        self.origin = origin

        self.image = Image.new('RGB', self.psize, color)
        self.pixels = self.image.load()

    def toPixel(self, point):
        return ( (point[0] - self.origin[0])*self.psize[0]/self.size[0],
                (point[1] - self.origin[1])*self.psize[1]/self.size[1])

    def setPixelbyPosition(self, x, y, col=(255, 255, 128)):
        xp, yp = self.toPixel((x, y))
        if 0 <= xp < self.psize[0] and 0 <= yp < self.psize[1]:
            self.pixels[xp, yp] = col



    def write(self, filename):
        self.image.save(filename, 'PNG')




