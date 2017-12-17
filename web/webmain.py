from flask import Flask,render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from config import Configuration
import os,cv2
import numpy as np
import base64
from recognize import Recognize
from facealign import facealign
app = Flask(__name__)
app.config.from_object(Configuration)
@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                return 'FILE NOT UPLOADED'
            f = request.files['file']
            file_data = f.stream.read()
            nparr = np.fromstring(file_data, np.uint8)
            img_color = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            img = cv2.imdecode(nparr, 0)
            face_cascade = cv2.CascadeClassifier('/home/prakhar/Desktop/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(img, 1.3, 5)
            result = []
            if faces!=():
                for (x,y,w,h) in faces:
                    cv2.rectangle(img_color,(x,y),(x+w,y+h),(255,255,0),2)
                    detected_face = img[y:y+h, x:x+w]
                    detected_face = facealign(detected_face)
                    result.append(Recognize(detected_face))
                print result
                img_str = cv2.imencode('.jpg', img_color)[1].tostring()
                encoded = base64.b64encode(img_str)
                mime = "image/jpg"
                mime = mime + ";"
                input_image = "data:%sbase64,%s" % (mime, encoded)
                return render_template('result.html', success=True, input_image=input_image, face_detected=result[0], face_detected_length=len(result))
            else:
                return render_template('result.html', success=False)
        except:
            pass
    return render_template('modi.html')




if __name__=='__main__':
    app.run()
