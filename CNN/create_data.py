#!/usr/bin/env python
#-*- coding:utf-8 -*-
from PIL import Image
import sys
from sklearn.model_selection import train_test_split
import os, glob
import numpy as np
import random, math

class DataCreate :

    """�g���[�j���O�f�[�^���쐬"""

  def __init__(self, script_name):
    Image.LOAD_TRUNCATED_IMAGES = True

  def create(self,indirname,npname) :
    input_dir = indirname
    categorys = []

    dir_list = os.listdir(input_dir)
    for index, dir_name in enumerate(dir_list):
      if dir_name == '.DS_Store' :
        continue
      categorys.append(dir_name)
    image_size = 50
    train_data = [] # �摜�f�[�^, ���x���f�[�^
    for idx, category in enumerate(categorys):
      try :
        print("---", category)
        image_dir = input_dir + "/" + category
        files = glob.glob(image_dir + "/*.png")
        for i, f in enumerate(files):
          img = Image.open(f)
          img = img.convert("RGB")
          img = img.resize((image_size, image_size))
          data = np.asarray(img)
          train_data.append([data, idx])

      except:
        print("SKIP : " + category)

    # �f�[�^��shuffle
    random.shuffle(train_data)
    X, Y = [],[]
    for data in train_data:
      X.append(data[0])
      Y.append(data[1])

    test_idx = math.floor(len(X) * 0.8)
    test_idx = int(test_idx)
    #https://stackoverflow.com/questions/20733156/slice-indices-must-be-integers-or-none-or-have-index-method
    xy = (np.array(X[0:test_idx]), np.array(X[test_idx:None]),
          np.array(Y[0:test_idx]), np.array(Y[test_idx:None]))
    np.save("./"+npname, xy)


if __name__ == "__main__":
  args = sys.argv
  datacreate = DataCreate(args[0])
  datacreate.create("TrainingImage","intensive_result")
  datacreate.create("TrainingNaiveImage","naive_result")
