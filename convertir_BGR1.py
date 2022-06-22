import cv2
# shift+F6 Cambias nombre de archivo
print("importado")

img = cv2.imread("Resources/leonel.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#escala de grises
imgDesenfoque = cv2.GaussianBlur(imgGray,(7,7),0)#desenfoque tiene q ser impares
imgCanny=cv2.Canny(img,100,100)#Canny
imgCanny2=cv2.Canny(img,150,200)#Canny bordes armonizacion


cv2.imshow("gris",imgGray)
cv2.imshow("desenfoque",imgDesenfoque)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Canny2",imgCanny2)
cv2.waitKey(0)
