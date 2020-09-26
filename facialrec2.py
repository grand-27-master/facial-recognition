import cv2
import numpy as np
#used for data extraction
from os import listdir
from os.path import isfile,join

data_path='C:/Users/abc/Downloads/Additional learning/machine learning/Computer Vision/faces/'
onlyfiles=[f for f in listdir(data_path) if isfile(join(data_path,f))]

train_data,labels=[],[]

for i,files in enumerate(onlyfiles):
    image_path=data_path+onlyfiles[i]
    images=cv2.imread(image_path,0)
    train_data.append(np.asarray(images,dtype=np.uint8))
    labels.append(i)

labels=np.asarray(labels,dtype=np.int32)

#building our model
model=cv2.face.LBPHFace_Recognizer_create()

model.train(np.asarray(train_data),np.asarray(labels))
print('Training completed!')

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

def face_detector(img,size=0.5):
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray_img,1.3,5)

    if face_cascade is():
        return img,[]

    for (x,y,w,h) in face_cascade:
        cv2.rectangle(img,(x,y),(x+h,y+w),(255,0,0),10)

        #region of interest
        roi=img[x:x+w,y:y+h]
        roi=cv2.resize(roi,(300,300))

    return img,roi

cam=cv2.VideoCapture(0)
while True:
    ret,frame=cam.read()     
    image,face=face_detector(frame)

    try:
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
           
        #predicting model
        result=model.predict(face)

        if result[1]<500:
            confidence=int(100*(1-(result[1])/300))
            disp= str(confidence) + 'is='
        cv2.putText(image,disp,(200,200),cv2.FONT_HERSHEY_PLAIN,2,(255,0,100),5)

        if confidence>80:
            cv2.putText(image,'Unlocked',(250,200),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),5)
            cv2.imshow('Face cropped',image)

        else:
            cv2.putText(image,'Locked',(250,200),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),5)
            cv2.imshow('Face cropped',image)  

    except:
        cv2.putText(image,'Face not found',(250,200),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),5)
        cv2.imshow('Face cropped',image)      

    if cv2.waitKey(1)==13:
        break


cam.release()
cv2.destroyAllWindows()