from PIL import Image
import numpy as np
import os


def main():
    folders = os.listdir("./dataset")
    x_point = []
    y_point = []
    for i in folders:
        pictures = os.listdir("./dataset/"+i)
        for pic in pictures:
            img = Image.open("./dataset/"+i+"/"+pic)
            img = img.convert("L")
            img = img.load(scale=0.25)
            img = np.asarray(img, dtype=np.uint8).reshape(1, -1)[0]
            print(len(img))
            x_point.append(img)
            y_point.append(i)
        print(i)
    print(len(x_point))
    print(len(y_point))

# im = Image.open("test.png")
# im.save("test-600.png", dpi=(600,600))
if __name__ == '__main__':
    main()
