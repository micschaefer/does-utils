from PIL import Image
import os, sys

path = r"path"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((256,256), Image.LANCZOS)
            imResize.save(f + '.png', 'PNG', quality=90)


def delete_old():
    dirs = os.listdir(path)
    for item in dirs:
        if item.endswith(".jpg"):
            os.remove(os.path.join(path, item))
        try:
            img = Image.open(os.path.join(path, item))
            w, h = img.size
            if (w > 257) & (h > 257):
                os.remove(os.path.join(path, item))
        except:
            pass


resize()
delete_old()
