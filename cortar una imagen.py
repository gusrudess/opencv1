import cv2
import numpy as np
# shift+F6 Cambias nombre de archivo
print("importado")

img = cv2.imread("Resources/leonel.jpg")
print(img.shape)#(altura,anchura,rgb)

imgResize = cv2.resize(img,(1000,500))
print('Nuevo tama '+str(imgResize.shape))

#en si una imagen es una matriz de pixeles, cortamos dando los puntos de matriz
imgCortada=imgResize[0:200,200:500]

#cv2.imshow("Imagen",img)
cv2.imshow("resize",imgResize)
cv2.imshow("ImgCortada",imgCortada)


cv2.waitKey(0)