import cv2;
import numpy as np;

ref_point=[]
crop=False

def select_area(event,x,y,flag,param):
    global ref_point,crop

    if event==cv2.EVENT_LBUTTONDOWN:
        ref_point=[(x,y)]
    elif event==cv2.EVENT_LBUTTONUP:
        ref_point.append((x,y))
        cv2.rectangle(img,ref_point[0],ref_point[1],(0,255,0),5)
        cv2.imshow("image loaded",img)  

img=cv2.imread('mask.jpg')

#cloning our image
clone_img=img.copy()

#title
cv2.namedWindow("Snipping Tool")

#mouse events
cv2.setMouseCallback("Snipping Tool",select_area)

while True:
    cv2.imshow("image loaded",img)
    if cv2.waitKey(1)==ord('r'):
        img=clone_img.copy()
    elif cv2.waitKey(1)==ord('c'):
        break   

if len(ref_point)==2:
    crop_img=clone_img[ref_point[0][1]:ref_point[1][1],ref_point[0][0]:ref_point[1][0]]
    cv2.imshow("cropped image",crop_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
