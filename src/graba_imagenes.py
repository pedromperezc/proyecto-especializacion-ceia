from src.read_roid import Roi
import cv2 as cv
import sys

for i in range(100):
    imagen = str(i)
    try:
        roi = Roi("datasets/Labels/" + imagen + ".roi")
        contorno = roi.get_contorno()
        img = cv.imread("datasets/Images/" + imagen + ".tif")
        cv.imwrite(imagen + ".tif", img)
        #cv.drawContours(img, contorno, -1, (0, 255, 0), 7)
        #cv.imwrite(imagen + ".png", img)
    except:
        print("imagen no encontrada: ", i)

