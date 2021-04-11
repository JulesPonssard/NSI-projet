import os
os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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

#look at the datatype
print(type(x_train))
print(type(y_train))
print(type(x_test))
print(type(y_test))
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

print('x_train shape', x_train.shape)
print('y_train shape', y_train.shape)
print('x_test shape', x_test.shape)
print('y_test shape', y_test.shape)

index = 0
print(x_train[index])

img = plt.imshow(x_train[index])
print(y_train[index])
plt.show()

classification = ['airplane','automobile','bird','cat','deer','frog','horse4','ship','truck']
print(classification[y_train[index][0]])

y_train_one_hot = to_categorical(y_train)
y_test_one_hot = to_categorical(y_test)

#print new label
print(y_train_one_hot)

#new label
print("the one hot label is", y_train_one_hot[index])

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

print('gg')