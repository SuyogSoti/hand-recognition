from PIL import Image
import numpy as np
import os
import klepto


def main():
    folders = os.listdir("./dataset")
    x_point = []
    y_point = []
    for i in folders:
        pictures = os.listdir("./dataset/"+i)
        for pic in pictures:
            img = Image.open("./dataset/"+i+"/"+pic)
            img = img.convert("L")
            img = np.asarray(img, dtype=np.uint8).reshape(1, -1)[0]
            x_point.append(img)
            y_point.append(i)
        print(i)
    d = klepto.archives.dir_archive('data', cached=True, serialized=True)
    d[0] = x_point
    d[1] = y_point
    d.dump()

# im = Image.open("test.png")
# im.save("test-600.png", dpi=(600,600))
if __name__ == '__main__':
    main()
