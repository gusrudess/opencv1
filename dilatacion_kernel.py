import cv2
import numpy as np
# shift+F6 Cambias nombre de archivo
print("importado")

img = cv2.imread("Resources/leonel.jpg")
kernel = np.ones((5,5),np.uint8)#8bit de 0 a 255
imgCanny=cv2.Canny(img,150,200)#Canny
imgDilatacion=cv2.dilate(imgCanny,kernel,iterations=1)#dilatacion mas iteraciones mas dilatada
imgAerosol=cv2.erode(imgDilatacion,kernel,iterations=1)
#imgDilatacion=cv2.Canny(img,100,100)#Canny


cv2.imshow("Canny",imgCanny)
cv2.imshow("dilatacion",imgDilatacion)
cv2.imshow("Aerosol",imgAerosol)

cv2.waitKey(0)
