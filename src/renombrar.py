from src.read_roid import Roi
import cv2 as cv
import os

os.chdir("src/datasets/imagen")
dir = os.getcwd()

for subdir, dirs, files in os.walk(dir):
    for filename in files:
        filepath = subdir + os.sep + filename
        img = cv.imread(filename)
        cv.imwrite(filename[:-4] + ".png", img)