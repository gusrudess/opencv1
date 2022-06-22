import cv2
# shift+F6 Cambias nombre de archivo
print("importado")

cap = cv2.VideoCapture("Resources/decimales.mp4")
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #si presiono q cierra ventana
        break



