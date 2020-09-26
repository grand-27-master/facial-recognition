import cv2
import numpy as np
import matplotlib.pyplot as plt

#classifier used to detect face
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

#create function which defines face features
def face_feature(img):
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray_img,1.3,5)

    #if there is no face
    if faces is():
        return None

    for (x,y,w,h) in faces:

        #for a particular face
        cropped_face=img[y:y+h,x:x+w] 

    return cropped_face    

cam=cv2.VideoCapture(0)

#used for counting no.of faces
cnt=0
while True:    
    ret,frame=cam.read()

    #if there is something on webcam
    if face_feature(frame) is not None:
        cnt=cnt+1

        #now resize face to set it according to webcam
        face_resize=cv2.resize(face_feature(frame),(500,500))
        face_resize=cv2.cvtColor(face_resize,cv2.COLOR_BGR2GRAY)

        #saving values of the image
        file_path='C:/Users/abc/Downloads/Additional learning/machine learning/Computer Vision/faces/user' + str(cnt) + '.jpg'
        cv2.imwrite(file_path,face_resize)

        #adding text
        font=cv2.FONT_HERSHEY_PLAIN
        cv2.putText(face_resize,str(cnt),(100,100),font,3,(255,0,0),5)
        cv2.imshow('Face detector',face_resize)

    else:
        print('Face not found')    

    if cv2.waitKey(1)==13 or cnt==200:
        break

cam.release()
cv2.destroyAllWindows()
print('Images collected!')        
