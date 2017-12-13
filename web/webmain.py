from flask import Flask,render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from config import Configuration
import os,cv2
app = Flask(__name__)
app.config.from_object(Configuration)
@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        print request.files
        if 'file' not in request.files:
            print 'No file part '+ str(request.files)
            return 'FILE NOT UPLOADED'
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['IMAGE_DIR'], filename))
        face_cascade = cv2.CascadeClassifier('/home/prakhar/Desktop/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
        img = cv2.imread(os.path.join(app.config['IMAGE_DIR'], filename))
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        print faces
        if faces!=():
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imwrite(os.path.join(app.config['IMAGE_DIR'], filename),img)
            return render_template('result.html', success=True, filename=filename)
        else:
            return render_template('result.html', success=False, filename=filename)
    return render_template('modi.html')




if __name__=='__main__':
    app.run()
