import roifile
import numpy as np
import cv2 as cv

class Roi(object):
    def __init__(self, ruta_imagen):
        self.imagen = roifile.roiread(ruta_imagen)
        self.contorno = np.array(self.imagen.coordinates())
        #self.contorno.resize((len(self.contorno), 1, 2))

    def get_contorno(self):
        return self.contorno



