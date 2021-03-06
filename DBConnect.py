import cv2
import numpy as np
import sqlite3
import os

def insetOrUpdate(id, name):
    conn = sqlite3.connect('data.db')

    query = "SELECT * FROM people Where id = " + str(id)
    cusror = conn.execute(query)

    isRecordExits = 0

    for row in cusror:
        isRecordExits = 1

    if(isRecordExits == 0):
        query = "Insert Into people(id,name) values(" + str(id) + ",'" + str(name) + "')"
    else:
        query = "Update people Set name = '" + str(name) + "' Where id = " + str(id)
    
    conn.execute(query)
    conn.commit()
    conn.close()

# load mat tu webcam

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +  "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

#insetToDB
id = input("enter your ID: ")
name = input("enter your name: ")
insetOrUpdate(id,name)

index = 0

while(True):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3 , 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

        if not os.path.exists('dataset'):
            os.makedirs('dataSet')
        
        index +=1

        cv2.imwrite('dataSet/User.' + str(id) + '.' + str(index) + ".jpg", gray[y:y + h, x: x+w])
    
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    if index>100:
        break

cap.release()
cv2.destroyAllWindows()
        
