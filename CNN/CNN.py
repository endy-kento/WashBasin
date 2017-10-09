#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import glob
import keras
from keras.datasets import mnist
from keras.models import Sequential

from keras.layers import Activation, Dropout, Flatten, Dense
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import random, math

batch_size = 32
num_classes = 7
epochs = 120

img_rows, img_cols = 20, 20

buf=[]
buf_90=[]
buf_180=[]
buf_270=[]

Data_DirPath_list = glob.glob('./CSV/CNNdatas/*/jyu/*/*.csv')
for f in Data_DirPath_list:
    if f.count('Calibration') > 0:
        buf.append([np.loadtxt(f,delimiter=','),0])
    elif  f.count('Roll_90')> 0:
        buf_90.append([np.loadtxt(f,delimiter=','),0])
    elif  f.count('Roll_180')> 0:
        buf_180.append([np.loadtxt(f,delimiter=','),0])
    else:
        buf_270.append([np.loadtxt(f,delimiter=','),0])

random.shuffle(np.array(buf))
random.shuffle(np.array(buf_90))
random.shuffle(np.array(buf_180))
random.shuffle(np.array(buf_270))

buf_list=[np.array(buf),np.array(buf_90),np.array(buf_180),np.array(buf_270)]
test_idx = math.floor(len(buf) * 0.8)
test_idx = int(test_idx)

train_datalist=np.empty([0, 20,20])
train_categorylist=np.empty([0])

test_datalist=np.empty([0, 20,20])
test_categorylist=np.empty([0])

for buf in buf_list:
    for data in buf:
        buf_datalist.append(data[0])
        buf_categorylist.append(data[1])

    train_datalist = np.r_[train_datalist,np.array(buf_datalist[0:test_idx])]
    test_datalist = np.r_[test_datalist,np.array(buf_datalist[test_idx:])]
    train_categorylist = np.r_[train_categorylist,np.array(buf_categorylist[0:test_idx])]
    test_categorylist = np.r_[test_categorylist,np.array(buf_categorylist[test_idx:])]

    buf_datalist=[]
    buf_categorylist=[]



buf=[]
buf_90=[]
buf_180=[]
buf_270=[]

Data_DirPath_list = glob.glob('./CSV/CNNdatas/*/kdo/*/*.csv')
for f in Data_DirPath_list:
    if f.count('Calibration') > 0:
        buf.append([np.loadtxt(f,delimiter=','),1])
    elif  f.count('Roll_90')> 0:
        buf_90.append([np.loadtxt(f,delimiter=','),1])
    elif  f.count('Roll_180')> 0:
        buf_180.append([np.loadtxt(f,delimiter=','),1])
    else:
        buf_270.append([np.loadtxt(f,delimiter=','),1])

random.shuffle(np.array(buf))
random.shuffle(np.array(buf_90))
random.shuffle(np.array(buf_180))
random.shuffle(np.array(buf_270))
buf_list=[np.array(buf),np.array(buf_90),np.array(buf_180),np.array(buf_270)]

test_idx = math.floor(len(buf) * 0.8)
test_idx = int(test_idx)
for buf in buf_list:
    for data in buf:
      buf_datalist.append(data[0])
      buf_categorylist.append(data[1])

    train_datalist = np.r_[train_datalist,np.array(buf_datalist[0:test_idx])]
    test_datalist = np.r_[test_datalist,np.array(buf_datalist[test_idx:])]
    train_categorylist = np.r_[train_categorylist,np.array(buf_categorylist[0:test_idx])]
    test_categorylist = np.r_[test_categorylist,np.array(buf_categorylist[test_idx:])]
    buf_datalist=[]
    buf_categorylist=[]

buf=[]
buf_90=[]
buf_180=[]
buf_270=[]

Data_DirPath_list = glob.glob('./CSV/CNNdatas/*/kwk/*/*.csv')
for f in Data_DirPath_list:
    if f.count('Calibration') > 0:
        buf.append([np.loadtxt(f,delimiter=','),2])
    elif  f.count('Roll_90')> 0:
        buf_90.append([np.loadtxt(f,delimiter=','),2])
    elif  f.count('Roll_180')> 0:
        buf_180.append([np.loadtxt(f,delimiter=','),2])
    else:
        buf_270.append([np.loadtxt(f,delimiter=','),2])

random.shuffle(np.array(buf))
random.shuffle(np.array(buf_90))
random.shuffle(np.array(buf_180))
random.shuffle(np.array(buf_270))
buf_list=[np.array(buf),np.array(buf_90),np.array(buf_180),np.array(buf_270)]

test_idx = math.floor(len(buf) * 0.8)
test_idx = int(test_idx)
for buf in buf_list:
    for data in buf:
      buf_datalist.append(data[0])
      buf_categorylist.append(data[1])

    train_datalist = np.r_[train_datalist,np.array(buf_datalist[0:test_idx])]
    test_datalist = np.r_[test_datalist,np.array(buf_datalist[test_idx:])]
    train_categorylist = np.r_[train_categorylist,np.array(buf_categorylist[0:test_idx])]
    test_categorylist = np.r_[test_categorylist,np.array(buf_categorylist[test_idx:])]
    buf_datalist=[]
    buf_categorylist=[]
buf=[]
buf_90=[]
buf_180=[]
buf_270=[]

Data_DirPath_list = glob.glob('./CSV/CNNdatas/*/okd/*/*.csv')
for f in Data_DirPath_list:
    if f.count('Calibration') > 0:
        buf.append([np.loadtxt(f,delimiter=','),3])
    elif  f.count('Roll_90')> 0:
        buf_90.append([np.loadtxt(f,delimiter=','),3])
    elif  f.count('Roll_180')> 0:
        buf_180.append([np.loadtxt(f,delimiter=','),3])
    else:
        buf_270.append([np.loadtxt(f,delimiter=','),3])

random.shuffle(np.array(buf))
random.shuffle(np.array(buf_90))
random.shuffle(np.array(buf_180))
random.shuffle(np.array(buf_270))
buf_list=[np.array(buf),np.array(buf_90),np.array(buf_180),np.array(buf_270)]

test_idx = math.floor(len(buf) * 0.8)
test_idx = int(test_idx)
for buf in buf_list:
    for data in buf:
      buf_datalist.append(data[0])
      buf_categorylist.append(data[1])

    train_datalist = np.r_[train_datalist,np.array(buf_datalist[0:test_idx])]
    test_datalist = np.r_[test_datalist,np.array(buf_datalist[test_idx:])]
    train_categorylist = np.r_[train_categorylist,np.array(buf_categorylist[0:test_idx])]
    test_categorylist = np.r_[test_categorylist,np.array(buf_categorylist[test_idx:])]
    buf_datalist=[]
    buf_categorylist=[]

buf=[]
buf_90=[]
buf_180=[]
buf_270=[]

Data_DirPath_list = glob.glob('./CSV/CNNdatas/*/skr/*/*.csv')
for f in Data_DirPath_list:
    if f.count('Calibration') > 0:
        buf.append([np.loadtxt(f,delimiter=','),4])
    elif  f.count('Roll_90')> 0:
        buf_90.append([np.loadtxt(f,delimiter=','),4])
    elif  f.count('Roll_180')> 0:
        buf_180.append([np.loadtxt(f,delimiter=','),4])
    else:
        buf_270.append([np.loadtxt(f,delimiter=','),4])

random.shuffle(np.array(buf))
random.shuffle(np.array(buf_90))
random.shuffle(np.array(buf_180))
random.shuffle(np.array(buf_270))
buf_list=[np.array(buf),np.array(buf_90),np.array(buf_180),np.array(buf_270)]

test_idx = math.floor(len(buf) * 0.8)
test_idx = int(test_idx)
for buf in buf_list:
    for data in buf:
      buf_datalist.append(data[0])
      buf_categorylist.append(data[1])

    train_datalist = np.r_[train_datalist,np.array(buf_datalist[0:test_idx])]
    test_datalist = np.r_[test_datalist,np.array(buf_datalist[test_idx:])]
    train_categorylist = np.r_[train_categorylist,np.array(buf_categorylist[0:test_idx])]
    test_categorylist = np.r_[test_categorylist,np.array(buf_categorylist[test_idx:])]
    buf_datalist=[]
    buf_categorylist=[]

buf=[]
buf_90=[]
buf_180=[]
buf_270=[]

Data_DirPath_list = glob.glob('./CSV/CNNdatas/*/smd/*/*.csv')
for f in Data_DirPath_list:
    if f.count('Calibration') > 0:
        buf.append([np.loadtxt(f,delimiter=','),5])
    elif  f.count('Roll_90')> 0:
        buf_90.append([np.loadtxt(f,delimiter=','),5])
    elif  f.count('Roll_180')> 0:
        buf_180.append([np.loadtxt(f,delimiter=','),5])
    else:
        buf_270.append([np.loadtxt(f,delimiter=','),5])

random.shuffle(np.array(buf))
random.shuffle(np.array(buf_90))
random.shuffle(np.array(buf_180))
random.shuffle(np.array(buf_270))
buf_list=[np.array(buf),np.array(buf_90),np.array(buf_180),np.array(buf_270)]

test_idx = math.floor(len(buf) * 0.8)
test_idx = int(test_idx)
for buf in buf_list:
    for data in buf:
      buf_datalist.append(data[0])
      buf_categorylist.append(data[1])

    train_datalist = np.r_[train_datalist,np.array(buf_datalist[0:test_idx])]
    test_datalist = np.r_[test_datalist,np.array(buf_datalist[test_idx:])]
    train_categorylist = np.r_[train_categorylist,np.array(buf_categorylist[0:test_idx])]
    test_categorylist = np.r_[test_categorylist,np.array(buf_categorylist[test_idx:])]
    buf_datalist=[]
    buf_categorylist=[]

buf=[]
buf_90=[]
buf_180=[]
buf_270=[]

Data_DirPath_list = glob.glob('./CSV/CNNdatas/*/snd/*/*.csv')
for f in Data_DirPath_list:
    if f.count('Calibration') > 0:
        buf.append([np.loadtxt(f,delimiter=','),6])
    elif  f.count('Roll_90')> 0:
        buf_90.append([np.loadtxt(f,delimiter=','),6])
    elif  f.count('Roll_180')> 0:
        buf_180.append([np.loadtxt(f,delimiter=','),6])
    else:
        buf_270.append([np.loadtxt(f,delimiter=','),6])

random.shuffle(np.array(buf))
random.shuffle(np.array(buf_90))
random.shuffle(np.array(buf_180))
random.shuffle(np.array(buf_270))
buf_list=[np.array(buf),np.array(buf_90),np.array(buf_180),np.array(buf_270)]

test_idx = math.floor(len(buf) * 0.8)
test_idx = int(test_idx)
for buf in buf_list:
    for data in buf:
      buf_datalist.append(data[0])
      buf_categorylist.append(data[1])

    train_datalist = np.r_[train_datalist,np.array(buf_datalist[0:test_idx])]
    test_datalist = np.r_[test_datalist,np.array(buf_datalist[test_idx:])]
    train_categorylist = np.r_[train_categorylist,np.array(buf_categorylist[0:test_idx])]
    test_categorylist = np.r_[test_categorylist,np.array(buf_categorylist[test_idx:])]
    buf_datalist=[]
    buf_categorylist=[]

# print np.array(train_datalist).shape
# print np.array(test_datalist).shape
# print np.array(train_categorylist).shape
# print np.array(test_categorylist).shape

if K.image_data_format() == 'channels_first':
    train_datalist = train_datalist.reshape(train_datalist.shape[0], 1, img_rows, img_cols)
    test_datalist = test_datalist.reshape(test_datalist.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    train_datalist = train_datalist.reshape(train_datalist.shape[0], img_rows, img_cols, 1)
    test_datalist = test_datalist.reshape(test_datalist.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

train_datalist = train_datalist.astype('float32')
test_datalist = test_datalist.astype('float32')
train_datalist /= 65535
test_datalist /= 65535
print('train_datalist shape:', train_datalist.shape)
print(train_datalist.shape[0], 'train samples')
print(test_datalist.shape[0], 'test samples')

train_categorylist = train_categorylist.astype('int32')
test_categorylist = test_categorylist.astype('int32')
train_categorylist = keras.utils.np_utils.to_categorical(train_categorylist, num_classes)
test_categorylist =  keras.utils.np_utils.to_categorical(test_categorylist, num_classes)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), padding="same"))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))


model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])

model.fit(train_datalist, train_categorylist, batch_size=batch_size, epochs=epochs,verbose=1, validation_data=(test_datalist, test_categorylist))
