#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import os
import numpy as np
import pandas as pd
import gc
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
from keras.layers import Conv2D, MaxPooling2D
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

class TrainModel :

    """���f�����쐬"""

  def __init__(self,indirname,npname):
    input_dir = indirname
    self.nb_classes = len([name for name in os.listdir(input_dir) if name != ".DS_Store"])
    x_train, x_test, y_train, y_test = np.load("./"+npname+".npy")
    # �f�[�^�𐳋K������
    self.x_train = x_train.astype("float") / 256
    self.x_test = x_test.astype("float") / 256
    self.y_train = np_utils.to_categorical(y_train, self.nb_classes)
    self.y_test = np_utils.to_categorical(y_test, self.nb_classes)

  def train(self, input,modelname) :
    model = Sequential()
    # K=32, M=3, H=3
    if input == None :
      model.add(Conv2D(32, (3, 3), padding='same', input_shape=self.x_train.shape[1:]))
    else :
      model.add(Conv2D(32, (3, 3), padding="same", input_shape=input)) #padding="same"�@�t�B���^����₤���߂̃[���p�f�B���O

    model.add(Activation('relu'))                   # �������֐�

    model.add(MaxPooling2D(pool_size=(2, 2)))       # ���̓f�[�^����舵���₷���`�ɕό`���邽�߂ɁA�������k���Adown sampling����

    model.add(Dropout(0.25))                        # dropout

    model.add(Conv2D(64, (3, 3), padding="same"))   # K=64, M=3, H=3�i�����j

    model.add(Activation('relu'))                   # �������֐�

    model.add(Conv2D(64, (3, 3)))                   # K=64, M=3, H=3�i�����j

    model.add(MaxPooling2D(pool_size=(2, 2)))       # ���̓f�[�^����舵���₷���`�ɕό`���邽�߂ɁA�������k���Adown sampling����

    model.add(Dropout(0.25))                        # dropout

    model.add(Flatten())                            #���X�g���t���b�g�� [[1,2,3],[4,5,6], [7]] -> [1,2,3,4,5,6,7]

    #4x4�s�N�Z���̉摜��50���ł���B2�����̉摜�̂܂܂ł͑��w�p�[�Z�v�g�����ɓ��͂ł��Ȃ��̂ŁA4x4x50=800�����̃x�N�g���ɕϊ�����

    model.add(Dense(512))                           #�S�����w-���ʕ��A

    model.add(Activation('relu'))                   # �������֐�

    model.add(Dropout(0.5))                         # dropout

    model.add(Dense(self.nb_classes))               #�S�����w-���ʕ��A

    model.add(Activation('softmax'))                # �������֐�


    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    if input == None :
      # �w�K���ă��f����ۑ�
      model.fit(self.x_train, self.y_train, batch_size=32, nb_epoch=10)
      #�P���f�[�^���A�������̃~�j�o�b�`�ɕ����āA�~�j�o�b�`���ƂɁAForward�����ABackward�����A�p�����[�^�[�X�V���s�����@
      #epoch �f�[�^������񂵂����H
      hdf5_file = "./"+modelname+".hdf5"
      model.save_weights(hdf5_file)

      # model�̃e�X�g
      score = model.evaluate(self.x_test, self.y_test)
      print modelname
      print 'loss=', score[0] #�����֐�
      print 'accuracy=', score[1]
    return model

if __name__ == "__main__":
  args = sys.argv
  train = TrainModel("TrainingImage","intensive_result")
  train.train(None,modelname="intensive_result")
  gc.collect()

  args = sys.argv
  train = TrainModel("TrainingNaiveImage","naive_result")
  train.train(None,modelname="naive_result")
  gc.collect()
