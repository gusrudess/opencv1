import cv2
import numpy as np
# shift+F6 Cambias nombre de archivo
print("importado")

img = cv2.imread("Resources/leonel.jpg")
print(img.shape)#(altura,anchura,rgb)

imgResize = cv2.resize(img,(300,200))
print('Nuevo tama '+str(imgResize.shape))

cv2.imshow("Imagen",img)
cv2.imshow("resize",imgResize)


cv2.waitKey(0)