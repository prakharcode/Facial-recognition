import numpy as np
import cv2
import os
face_cascade = cv2.CascadeClassifier('/home/prakhar/Desktop/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
fp = open('./images/arvind/log.txt','r')
images_total_extracted = int(fp.read())
fp.close()
for i in range(0,images_total_extracted+1):
    try:
        try:
            img = cv2.imread('./images/arvind/'+str(i)+'.jpg')
            faces = face_cascade.detectMultiScale(img, 1.3, 5)
            for (x,y,w,h) in faces:
                img = img[y:y+h,x:x+w]
        except:
            print "IMAGE NO: %d " % i
        path= './images/detected/kejriwal'
        try:
            if faces!=():
                print "FACES: "+str(faces)
                cv2.imwrite(os.path.join(path,str(i)+'.jpg'),img)
        except:
            print "file path %s error" %path+str(i)+'.jpg'
        cv2.destroyAllWindows()
    except:
        pass
