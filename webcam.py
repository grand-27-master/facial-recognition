import cv2;

#reading camera id
cam=cv2.VideoCapture(0)

#camera is a dynamic object so we need infinite loop
while True:
    ret,frame=cam.read()

    #display
    cv2.imshow("My camera",frame)

    #it will wiat till 1ms until enter key is pressed (ASCII=13)
    if(cv2.waitKey(1)==13):
        break
cam.release()
cv2.destroyAllWindows()    
