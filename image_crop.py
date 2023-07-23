import argparse
import os
from pathlib import Path
from PIL import Image

path = r"path"


def image_crop():
    files = [os.path.join(path, x) for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))]

    for image in files:
        img = Image.open(image)

        w, h = img.size

        img_l = img.crop((0, 0, h, h))
        img_r = img.crop((w-h, 0, w, h))

        img_l.save(os.path.join(os.path.splitext(image)[0] + "_l.png"), 'PNG', quality=100)
        img_r.save(os.path.join(os.path.splitext(image)[0] + "_r.png"), 'PNG', quality=100)

        os.remove(image)


image_crop()
