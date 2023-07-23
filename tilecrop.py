import cv2
import glob
import os

# [256, 320, 480, 720, 1024]
tileWidth = 720
tileHeight = tileWidth
step = 339

scrap_class = "E8"

def croptiles(path):
    croppedimgs = []
    img = cv2.imread(path)
    iheight = img.shape[0]
    iwidth = img.shape[1]
    for i in range(0, iheight - tileHeight, step):
        for j in range(0, iwidth - tileWidth, step):
            a = img[i:i + tileHeight, j:j + tileWidth]
            try:
                croppedimgs.append(a)
            except:
                pass
    return croppedimgs

def getImageFiles(path, ending):
    return glob.glob(path + '/**/*.' + ending, recursive=True)


def saveCroppedImages(sourcePath, destPath, ending):
    files = getImageFiles(sourcePath, ending)
    for i in files:
        croppedTiles = croptiles(i)
        file_name = os.path.split(os.path.splitext(i)[0])[1]  # splitext splits string at rightmost '.'
        c = 0
        for k in croppedTiles:
            try:
                cv2.imwrite(destPath + "/" + file_name + "_" + str(c) + "." + ending, k)
                c = c + 1
            except:
                print("Error")


filepath = r'path'
saveCroppedImages(filepath + scrap_class + "/raw", filepath + scrap_class + "/tiles", "jpg")


