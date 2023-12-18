import sys
import math
from PIL import Image


def main(args):
    dir = args[0]

    for i in range(0, 10):
        img = Image.new("RGB", (5000, 5000), "black")
        pixels = img.load()
        for j in range(img.size[0]):
            for k in range(i * 500):
                pixels[j, k] = (
                    180 - math.floor(k / 500) * 20,
                    180 - math.floor(k / 500) * 20,
                    180 - math.floor(k / 500) * 20,
                )
        img.save(dir + "test" + str(i) + ".bmp")


if __name__ == "__main__":
    main(sys.argv[1:])
