import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os


img = cv.imread('\\Users\\pperez\\Desktop\\Personal\\MAESTRIA\\proyecto-especializacion-ceia\\src\\datasets\\label\\75.png', cv.IMREAD_GRAYSCALE)

# Imagen original
plt.figure()
ax1=plt.subplot(221)
ax1.imshow(img, cmap='gray', vmin=0, vmax=255)
ax1.set_title('Original')

hist1,bins1 = np.histogram(img.ravel(),256,[0,256])
ax3=plt.subplot(223)
ax3.plot(hist1)

#Equalizo
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_eqzd = clahe.apply(img)
ax2=plt.subplot(222)

ax2.imshow(img_eqzd, cmap='gray', vmin=0, vmax=255)
ax2.set_title('Ecualizada')

hist2,bins2 = np.histogram(img_eqzd.ravel(),256,[0,256])
ax4=plt.subplot(224)
ax4.plot(hist2)

plt.figure()
ax = plt.subplot()
ax.imshow(img_eqzd, cmap='gray', vmin=0, vmax=255)
plt.show()


# plt.imshow(l,cmap='gray', vmin=0, vmax=255)
# plt.show()