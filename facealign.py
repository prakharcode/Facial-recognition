import numpy as np
import cv2
import os, math
from PIL import Image
from support import CropFace
left_eye_cascade = cv2.CascadeClassifier('/home/prakhar/Desktop/opencv/data/haarcascades/haarcascade_lefteye_2splits.xml')
right_eye_cascade = cv2.CascadeClassifier('/home/prakhar/Desktop/opencv/data/haarcascades/haarcascade_righteye_2splits.xml')
eye_pair_cass = cv2.CascadeClassifier('/home/prakhar/Desktop/opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
fp = open('./images/narendra/log.txt','r')
images_total_extracted = int(fp.read())
fp.close()
folder_images = os.getcwd()+'/images/normalized/modi'
for i in range(images_total_extracted+1):
    try:
        file_pt='./images/detected/modi/'+str(i)+'.jpg'
        im = Image.open(file_pt)
        img = cv2.imread(file_pt)
        # right_eye = left_eye_cascade.detectMultiScale(img, 1.3, 5)
        # left_eye = right_eye_cascade.detectMultiScale(img, 1.3, 5)
        eye_pair =eye_pair_cass.detectMultiScale(img,1.1,5)
        if len(eye_pair) ==2:
            right_eye = [eye_pair[0]]
            left_eye = [eye_pair[1]]
            print "EYE PAIR in IMAGE: %d" % i
        else:
            print "no  transform"
            continue
        print left_eye, right_eye
        cv2.line(img,center_left,center_right,(0,0,255),2)
        im = CropFace(im,(left_eye[0][0],left_eye[0][1]),(right_eye[0][0],right_eye[0][1]))
        im.save(os.path.join(folder_images,str(i)+".jpg"), "JPEG")
    except:
        pass
