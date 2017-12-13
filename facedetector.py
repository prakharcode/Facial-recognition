import numpy as np
import cv2
import os
face_cascade = cv2.CascadeClassifier('/home/prakhar/Desktop/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml')
fp = open('./images/arvind/log.txt','r')
images_total_extracted = int(fp.read())
fp.close()
error_img=[]
path= './images/normalized/kejriwal'
for i in range(0,images_total_extracted+1):
    try:
        img = cv2.imread('./images/normalized/kejriwal/'+str(i)+'.jpg')
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        faces = face_cascade.detectMultiScale(hsv, 1.3, len(img.shape))
        for (x,y,w,h) in faces:
            img = img[y:y+h,x:x+w]
        if faces!=():
            print "FACES: "+str(faces), "Image no: %d"%i
            cv2.imwrite(os.path.join(path,str(i)+'.jpg'),img)
    except:
        print "file path %s error" % (path+str(i)+'.jpg')
        error_img.append(i)
        cv2.destroyAllWindows()

for i in error_img:
    try:
        img = cv2.imread('./images/normalized/kejriwal/'+str(i)+'.jpg')
        faces = face_cascade.detectMultiScale(img, 1.3, 3)
        for (x,y,w,h) in faces:
            img = img[y:y+h,x:x+w]
        if faces!=():
            print "FACES: "+str(faces), "Image no: %d"%i
            cv2.imwrite(os.path.join(path,str(i)+'.jpg'),img)
    except:
        print "file path %s error" % (path+str(i)+'.jpg')
        cv2.destroyAllWindows()
