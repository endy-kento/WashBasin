#!/usr/bin/env python
#-*- coding:utf-8 -*-
import train as train
import sys, os
from PIL import Image
import numpy as np
import pandas as pd

if len(sys.argv) <= 1:
  quit()

image_size = 50
if str(sys.argv[1:]).find('Naive') > -1:
    input_dir1 = 'TrainingNaiveImage'
    categories1 = [name for name in os.listdir(input_dir1) if name != ".DS_Store"]

    X = []
    for file_name in sys.argv[1:]:
      img = Image.open(file_name)
      img = img.convert("RGB")
      img = img.resize((image_size, image_size))
      in_data = np.asarray(img)
      X.append(in_data)

    X = np.array(X)

    model = train.TrainModel("TrainingNaiveImage","naive_result").train(X.shape[1:],modelname="naive_result")
    model.load_weights("./naive_result.hdf5")

    predict = model.predict(X)

    for pre in predict:
      y = pre.argmax()
      ansname = str(sys.argv[1:]).replace("['./CheckNaiveImage/", '')
      ansname = ansname.replace(".png']", '')
      if ansname == str(categories1[y]):
          print "Naive :" , ansname , categories1[y] , " [correct answer!!]"
      else:
          print "Naive :" , ansname , categories1[y] , " [BAD!!]"

else:

    input_dir1 = 'TrainingImage'
    categories1 = [name for name in os.listdir(input_dir1) if name != ".DS_Store"]

    X = []
    for file_name in sys.argv[1:]:
      img = Image.open(file_name)
      img = img.convert("RGB")
      img = img.resize((image_size, image_size))
      in_data = np.asarray(img)
      X.append(in_data)

    X = np.array(X)

    model = train.TrainModel("TrainingImage","intensive_result").train(X.shape[1:],modelname="intensive_result")
    model.load_weights("./intensive_result.hdf5")

    predict = model.predict(X)

    for pre in predict:
      y = pre.argmax()
      ansname = str(sys.argv[1:]).replace("['./CheckImage/", '')
      ansname = ansname.replace(".png']", '')
      if ansname == str(categories1[y]):
          print "Intensive :" , ansname , categories1[y] , " [correct answer!!]"
      else:
          print "Intensive :" , ansname , categories1[y] , " [BAD!!]"
