from PIL import Image
import os, sys

path = os.getcwd()+'/images/normalized/kejriwal/'
dirs = os.listdir( path )
save_path = os.getcwd() + '/images/resized/kejriwal/'
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            print 'is file'
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((100,100), Image.ANTIALIAS)
            imResize.save(save_path+item, 'JPEG', quality=90)

resize()
