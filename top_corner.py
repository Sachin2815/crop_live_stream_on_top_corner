import cv2
cam = cv2.VideoCapture(0)
while True:
    status , photo = cam.read()
    photo[0:200,0:150] = photo[100:300,150:300]
    cv2.imshow("myphoto",photo)
    if cv2.waitKey(10) == 13:
        break
cv2.destroyAllWindows()
cam.release()
