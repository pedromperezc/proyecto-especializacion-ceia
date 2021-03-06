from src.read_roid import Roi
import cv2 as cv
import os

os.chdir("datasets/tif")
dir = os.getcwd()

for subdir, dirs, files in os.walk(dir):
    for filename in files:
        filepath = subdir + os.sep + filename
        img = cv.imread(filename,cv.IMREAD_GRAYSCALE)
        #equalizo
        clahe = cv.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        img_eqzd = clahe.apply(img)

        cv.imwrite(str(int(filename[:-4])+300)+ ".png", img_eqzd)