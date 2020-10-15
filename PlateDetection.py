import cv2;
import numpy as np;

img=cv2.imread(r"C:\Users\abc\OneDrive\Pictures\plate.jpg")

# Here is a list of the most common parameters of the detectMultiScale function :
# scaleFactor : Parameter specifying how much the image size is reduced at each image scale.
# minNeighbors : Parameter specifying how many neighbors each candidate rectangle should have to retain it.
# minSize : Minimum possible object size. Objects smaller than that are ignored.
# maxSize : Maximum possible object size. Objects larger than that are ignored.
PlateCascade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
plates=PlateCascade.detectMultiScale(img,1.2,3)

for (x,y,w,h) in plates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("plate detected",img)
cv2.waitKey(0)

