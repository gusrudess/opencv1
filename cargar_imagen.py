import cv2
# shift+F6 Cambias nombre de archivo
print("importado")

img = cv2.imread("Resources/leonel.jpg")
cv2.imshow("salida",img)
cv2.waitKey(0)
