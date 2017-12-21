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
        if 'file' not in request.files:
            return 'FILE NOT UPLOADED'
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['IMAGE_DIR'],filename))
        img_color = cv2.imread(os.path.join(app.config['IMAGE_DIR'], filename))
        img = cv2.imread(os.path.join(app.config['IMAGE_DIR'], filename),0)
        # file_data = f.stream.read()
        # nparr = np.fromstring(file_data, np.uint8)
        # img_color = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # img = cv2.imdecode(nparr, 0)
        # img_str = cv2.imencode('.jpg', img_color)[1].tostring()
        # encoded = base64.b64encode(img_str)
        # mime = "image/jpg"
        # mime = mime + ";"
        # input_image = "data:%sbase64,%s" % (mime, encoded)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        result = []
        if faces!=():
            for (x,y,w,h) in faces:
                cv2.rectangle(img_color,(x,y),(x+w,y+h),(255,255,0),2)
                detected_face = img[y:y+h, x:x+w]
                # detected_face = facealign(detected_face)
                result.append(Recognize(detected_face))
            print result
            # img_str = cv2.imencode('.jpg', img_color)[1].tostring()
            # encoded = base64.b64encode(img_str)
            # mime = "image/jpg"
            # mime = mime + ";"
            # input_image = "data:%sbase64,%s" % (mime, encoded)
            cv2.imwrite(os.path.join(app.config['IMAGE_DIR'], filename),img_color)
            return render_template('result.html', success=True, face_detected=result[0], face_detected_length=len(result), filename=filename) #input_image=input_image

        else:
            return render_template('result.html', success=False, filename=filename) #input_image=input_image
    return render_template('modi.html')




if __name__=='__main__':
    app.run()
