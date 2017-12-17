import cv2
import numpy as np
import os
from skimage import io
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.models import Sequential, Model, load_model
from keras.layers import Dense, Dropout, Activation ,Flatten,Conv2D, MaxPooling2D, Input, merge
from keras.layers.pooling import AveragePooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import PReLU
from keras.optimizers import RMSprop, SGD
from keras.optimizers import *
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, History, Callback
from keras import initializers


base_path = './dataset/'
DatasetPath = []
for i in os.listdir(base_path):
    if i != 'Readme.txt':
        DatasetPath.append(os.path.join(base_path, i))


imageData = []
imageLabels = []

for fl in DatasetPath:
    imgRead = io.imread(fl, as_grey=True)
    imageData.append(imgRead)
    if os.path.split(fl)[1].split(".")[0].startswith("kejriwal"):
        labelRead = 0 # Parse class label from file
    else:
        labelRead = 1
    imageLabels.append(labelRead)

#train_test_split of data
X = np.array(imageData)
y = np.array(imageLabels)
X_train, X_test, y_train, y_test = train_test_split(X, y,
    train_size=0.6, random_state = 20)
# Total no of labels for sanity check
nb_labels = len(np.unique(y))
print 'Number of unique classes ', nb_labels

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train /= 255.
X_test /= 255.

# reshape to: nb_sample, channels, height, width
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], X_train.shape[2],1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], X_test.shape[2],1)

print "Training matrix shape", X_train.shape
print "Testing matrix shape", X_test.shape

def conv_3x3_2fc_500(size):
    model = Sequential()
    init = 'he_normal'
    # Block 1

    model.add(Conv2D(64, (5, 5), activation='relu', name='block1_conv1',
                            kernel_initializer=init, input_shape=(size, size,1) , padding="same", strides=(1, 1)))
    model.add(MaxPooling2D((3, 3), strides=(2, 2), name='block1_pool'))

    model.add(Conv2D(128, (3, 3), activation='relu', padding='same', name='block2_conv2', kernel_initializer=init))
    model.add(MaxPooling2D((3, 3), strides=(2, 2), name='block2_pool'))

    model.add(Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv3', kernel_initializer=init))
    model.add(MaxPooling2D((3, 3), strides=(2, 2), name='block3_pool'))

    model.add(Conv2D(512, (3, 3), activation='relu', padding='same', name='block4_conv4', kernel_initializer=init))
    model.add(MaxPooling2D((3, 3), strides=(2, 2), name='block4_pool'))

    model.add(Flatten())
    model.add(Dense(500, activation='relu', kernel_initializer=init, name='fc1'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(500, activation='relu', kernel_initializer=init, name='fc2'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(2, activation='softmax', name='predictions'))

    optim = Adam(lr=0.0005, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)

    model.compile(loss='sparse_categorical_crossentropy', optimizer=optim, metrics=['accuracy'])
    return model

model = conv_3x3_2fc_500(size=100)
model.summary()

loss_history = History()
model.fit(X_train, y_train, batch_size=64, nb_epoch=100,
          verbose=1, validation_data=(X_test, y_test),
          callbacks=[loss_history])
filepath='facedetect.h5'
model.save(filepath)
