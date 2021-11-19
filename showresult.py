import cv2
import numpy as np
import os.path
import sqlite3
#dung de lay anh tu thu muc
from PIL import Image
#trainning hinh anh nhan dien vs thu vien khuon mat face
face_casade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer\\trainningData.yml')
#ham get profile by id from database
def getprofile(id):
    con =sqlite3.connect('data.db')
    query = "Select * From people WHERE id ="+str(id)
    cusor = con.execute(query)
    profile = None
    for row in cusor:
        profile = row
    con.close()
    return profile

cap = cv2.VideoCapture(0)
fontface = cv2.FONT_HERSHEY_COMPLEX
while(True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face_casade.detectMultiScale(gray)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cut_gray = gray[y: y+h ,x: x+w]
        id,confidence =recognizer.predict(cut_gray)
        if(confidence<40):
            profile = getprofile(id)
            if(profile != None):
                
                cv2.putText(frame,""+str(profile[1]),(x+10,y+h+30),fontface,1,(0,255,0),2)
        else:
            cv2.putText(frame,"Unknow",(x+10,y+h+30),fontface,1,(0,255,0),2)
    cv2.imshow('anh',frame)
    if(cv2.waitKey(1)==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

