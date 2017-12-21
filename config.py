import os
class Configuration(object):    #instructs flask to run in production mode
    APPLICATION_DIR = os.getcwd()#os.path.dirname(os.path.realpath(__file__)) #getting current directory location
    DEBUG = True
    SECRET_KEY = 'flask is fun!'
    STATIC_DIR = os.path.join(APPLICATION_DIR,'static')
    IMAGE_DIR  = os.path.join(STATIC_DIR,'image')
