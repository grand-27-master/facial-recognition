import cv2
import numpy as np

img=np.zeros((600,600),np.uint8)
windowName='Drawing'
cv2.namedWindow(windowName)

#global variables
drawing=False
x1,y1=-1,-1
def shape(event,x,y,flag,param):
    global drawing,x1,y1
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        x1,y1=x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.rectangle(img,(x1,y1),(x,y),(255,0,0),3)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False        


cv2.setMouseCallback(windowName,shape)
while True:
    cv2.imshow(windowName,img)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()            