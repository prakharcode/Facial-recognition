def Recognize(img):
    from keras.models import load_model
    import cv2
    import numpy as np
    model = load_model('facedetect.h5')
    resized_image = cv2.resize(img,(100,100))
    resized_image = np.array(resized_image)
    x = resized_image.reshape(1,100,100,1)
    print model.predict(x)
