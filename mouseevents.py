import numpy as np
import cv2

img=np.zeros((500,500,3),np.uint8)
windowName='Frame'
cv2.namedWindow(windowName)

def circle(event,x,y,flag,param):
  if event==cv2.EVENT_LBUTTONDOWN:
    cv2.circle(img,(x,y),10,(0,0,255),-1)
  if event==cv2.EVENT_LBUTTONDBLCLK:
    cv2.circle(img,(x,y),10,(0,255,255),-1)
 
  if event==cv2.EVENT_RBUTTONDOWN:
    cv2.circle(img,(x,y),10,(255,0,0),-1)

cv2.setMouseCallback(windowName,circle)
while True:
  cv2.imshow(windowName,img)
  if cv2.waitKey(1)==13:
    break

cv2.destroyAllWindows()    