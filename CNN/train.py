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

    """モデルを作成"""

  def __init__(self,indirname,npname):
    input_dir = indirname
    self.nb_classes = len([name for name in os.listdir(input_dir) if name != ".DS_Store"])
    x_train, x_test, y_train, y_test = np.load("./"+npname+".npy")
    # データを正規化する
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
      model.add(Conv2D(32, (3, 3), padding="same", input_shape=input)) #padding="same"　フィルタ分を補うためのゼロパディング

    model.add(Activation('relu'))                   # 活性化関数

    model.add(MaxPooling2D(pool_size=(2, 2)))       # 入力データをより扱いやすい形に変形するために、情報を圧縮し、down samplingする

    model.add(Dropout(0.25))                        # dropout

    model.add(Conv2D(64, (3, 3), padding="same"))   # K=64, M=3, H=3（調整）

    model.add(Activation('relu'))                   # 活性化関数

    model.add(Conv2D(64, (3, 3)))                   # K=64, M=3, H=3（調整）

    model.add(MaxPooling2D(pool_size=(2, 2)))       # 入力データをより扱いやすい形に変形するために、情報を圧縮し、down samplingする

    model.add(Dropout(0.25))                        # dropout

    model.add(Flatten())                            #リストをフラット化 [[1,2,3],[4,5,6], [7]] -> [1,2,3,4,5,6,7]

    #4x4ピクセルの画像が50枚である。2次元の画像のままでは多層パーセプトロンに入力できないので、4x4x50=800次元のベクトルに変換する

    model.add(Dense(512))                           #全結合層-識別部、

    model.add(Activation('relu'))                   # 活性化関数

    model.add(Dropout(0.5))                         # dropout

    model.add(Dense(self.nb_classes))               #全結合層-識別部、

    model.add(Activation('softmax'))                # 活性化関数


    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    if input == None :
      # 学習してモデルを保存
      model.fit(self.x_train, self.y_train, batch_size=32, nb_epoch=10)
      #訓練データを、いくつかのミニバッチに分けて、ミニバッチごとに、Forward処理、Backward処理、パラメーター更新を行う方法
      #epoch データを何回回したか？
      hdf5_file = "./"+modelname+".hdf5"
      model.save_weights(hdf5_file)

      # modelのテスト
      score = model.evaluate(self.x_test, self.y_test)
      print modelname
      print 'loss=', score[0] #損失関数
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
