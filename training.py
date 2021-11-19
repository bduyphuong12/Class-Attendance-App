import cv2
import numpy as np
import os.path
#dung de lay anh tu thu muc
from PIL import Image

#dau tien phai lay duoc id va mang cac du lieu anh cua minh de minh train
#id thi minh trong duong dan cua anh lun
#face la thu vien mac dinh cua opencv de training cai hinh anh
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'

#ham de minh lay ra duoc id va 1 list cac du lieu anh dung de train
def getImageWithId(path):
    imagepath= [os.path.join(path,f) for f in os.listdir(path)]
    #print(imagepath)
    faces = []
    IDs = []
    for x in imagepath:
        #chuyen doi lay tat ca cac anh tu imagepath roi minh cvt sang keiu anh PIL de trainning du lieu
        faceimage = Image.open(x).convert('L')    
        #'L' la gray
        #face chua anh duoi dang ma tran
        facenp = np.array(faceimage,'uint8')
        id = int(x.split('\\')[1].split('.')[1])
        faces.append(facenp)
        IDs.append(id)
        cv2.imshow('trainning',facenp)
        cv2.waitKey(10)
    return faces,IDs

       


faces,Ids=getImageWithId(path)
recognizer.train(faces,np.array(Ids))
if not os.path.exists('recognizer'):
    os.makedirs('recognizer')
recognizer.save('recognizer\\trainningData.yml')
cv2.destroyAllWindows()

