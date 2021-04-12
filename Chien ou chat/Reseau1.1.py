import os
os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#Description : This program will classifies images
#Import Libraries
import tensorflow as tf

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras import layers
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

#Load the data
from keras.datasets import cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

classification = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

y_train_one_hot = to_categorical(y_train)
y_test_one_hot = to_categorical(y_test)
1
#Normalize the pixels to be values between 0 and 1
x_train = x_train / 255
x_test = x_test / 255

#Creation du réseau
model = Sequential()

#add the first layer
model.add( Conv2D(32, (5,5), activation='relu', input_shape=(32,32,3)))

#add other layer pooling
model.add(MaxPooling2D(pool_size=(2,2)))

#add other convulation layer
model.add( Conv2D(32, (5,5), activation='relu',))

#add other layer pooling
model.add(MaxPooling2D(pool_size=(2,2)))

#add flattening layer
model.add(Flatten())

#add a layer with 1000  neurons
model.add(Dense(1000, activation='relu'))

#add a dropout layer
model.add(Dropout(0.5))

#add a layer with 500  neurons
model.add(Dense(500, activation='relu'))

#add a dropout layer
model.add(Dropout(0.5))

#add a layer with 250  neurons
model.add(Dense(250, activation='relu'))

#add a layer with 10  neurons
model.add(Dense(10, activation='softmax'))

#compile the model
model.compile(loss = 'categorical_crossentropy',
              optimizer = 'adam',
              metrics= ['accuracy'])

#train the model
hist = model.fit(x_train, y_train_one_hot,
                 batch_size= 256,
                 epochs=10,
                 validation_split= 0.2)



import skimage
from skimage.transform import resize

def Prediction(images):
    new_img = plt.imread(images)
    new_img = skimage.img_as_float(new_img)
    plt.show()

    # resize img
    new_image = resize(new_img, (32, 32, 3))
    img2 = plt.imshow(new_image)
    plt.show()

    # PRediction FINAL LOLLLL
    predictions = model.predict(np.array([new_image]))
    print(predictions)

    list_index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = predictions

    for i in range(10):
        for j in range(10):
            if x[0][list_index[i]] > x[0][list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    print(list_index)
    for i in range(5):
        print(classification[list_index[i]], ':', round(predictions[0][list_index[i]] * 100, 2), '%')

Prediction('chat1.jpg')







