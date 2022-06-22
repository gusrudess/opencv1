import cv2
# shift+F6 Cambias nombre de archivo
print("importado")

cap = cv2.VideoCapture(0)#seleccionar camara
cap.set(3,1280)#(ancho,cantidad)
cap.set(4,720)#(alto,canntidad)
cap.set(10,200)#(brillo,cantidad brillo)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #si presiono q cierra ventana
        break