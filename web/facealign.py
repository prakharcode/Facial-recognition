import numpy as np
import cv2
import os, math
from PIL import Image
from support import Normalize
# left_eye_cascade = cv2.CascadeClassifier('/home/prakhar/Desktop/opencv/data/haarcascades/haarcascade_lefteye_2splits.xml')
# right_eye_cascade = cv2.CascadeClassifier('/home/prakhar/Desktop/opencv/data/haarcascades/haarcascade_righteye_2splits.xml')
eye_pair_cass = cv2.CascadeClassifier('/home/prakhar/Desktop/opencv/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
def facealign(img):                # for i in range(images_total_extracted+1):
    try:
        eye_pair =eye_pair_cass.detectMultiScale(img,1.1,1)
        if len(eye_pair) ==2:
            right_eye = [eye_pair[0]]
            left_eye = [eye_pair[1]]
            im = Normalize(im,(left_eye[0][0],left_eye[0][1]),(right_eye[0][0],right_eye[0][1]))
            # im.save(os.path.join(folder_images,str(i)+".jpg"), "JPEG")
    except:
        pass
    return img
