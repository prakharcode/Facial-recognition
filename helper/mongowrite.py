from pymongo import MongoClient
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io ,os
from bson.binary import Binary
client = MongoClient()
db = client.facedb
face= db.face
filepath = './dataset/'
file_list = os.listdir(filepath)
def write_data():
    for filename in file_list:
        image_file_handle = open(filepath+filename)
        image_binary_data = Binary(image_file_handle.read())
        image_name = filename.split('.')[0]
        data = {image_name:image_binary_data}
        try:
            data_id = face.insert_one(data).inserted_id
            print data_id
        except:
            print "Upload Error"


def image_retrieve(image_id):
    image_dict = face_collection.find_one({"_id":image_id})
    stream = io.BytesIO(image_dict[image_dict.keys()[1]])
    img = Image.open(stream)
    draw = ImageDraw.Draw(img)
    img.save("a_test.png")
write_data()
