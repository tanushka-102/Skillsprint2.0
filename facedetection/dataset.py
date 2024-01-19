import cv2
import os
import time

haar_file = 'haarcascade_frontalface_default.xml'

datasets = 'C:/Users/tanu3/PycharmProjects/facedetection/dataset/'
name = "tanu"

path = os.path.join(datasets, name)
if not os.path.isdir(path):
    os.mkdir(path)
face_cascade = cv2.CascadeClassifier(haar_file)  # CascadeClassifier=distinguish between objects

cap = cv2.VideoCapture(0)
print("Webcam is open?",cap.isOpened())

time.sleep(2)
count=1

while count<101:
    ret,frame=cap.read()
    if ret==True:
        img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(img_gray,1.3,4)
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            face=img_gray[y:y+h,x:x+h]
            face_resize=cv2.resize(face,(640,480))
            cv2.imwrite("%s/%s.png"%(path,count),face_resize)
        count=count+1
        cv2.imshow("Face Capturing",frame)
        if cv2.waitKey(1)==ord("q"):
            break
print("Your shakal has been created")
cap.release()
cv2.destroyAllWindows()


