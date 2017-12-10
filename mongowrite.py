from pymongo import MongoClient
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io
from bson.binary import Binary
client = MongoClient()
db = client.facedb
face_collection = db.face_collection

def write_data():
    fp = open('./images/arvind/log.txt','r')
    images_total_extracted = int(fp.read())
    fp.close()
    for counter in range(0,images_total_extracted+1):
        try:
            image_file_handle = open('./images/detected/kejriwal/'+str(counter)+'.jpg')
            image_binary_data = Binary(image_file_handle.read())
            image_name = "Kejriwal"+str(counter)
            data = {image_name:image_binary_data}
            try:
                data_id = face_collection.insert_one(data).inserted_id
                print data_id
            except:
                print "Upload Error"
        except:
            print "Loop Error %d" % counter


def image_retrieve(image_id):
    image_dict = face_collection.find_one({"_id":image_id})
    stream = io.BytesIO(image_dict[image_dict.keys()[1]])
    img = Image.open(stream)
    draw = ImageDraw.Draw(img)
    img.save("a_test.png")
write_data()
