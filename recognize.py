def Recognize(img):
    from keras.models import load_model
    import cv2
    import numpy as np
    model = load_model('face.h5')
    resized_image = cv2.resize(img,(100,100))
    resized_image = np.array(resized_image)
    x = resized_image.reshape(1,100,100,1)
    print model.predict(x)
    if int(model.predict(x)[0][1]):
        return "Narendra Modi"
    elif int(model.predict(x)[0][0]):
        return "Arvind Kejriwal"
    else:
        return None
