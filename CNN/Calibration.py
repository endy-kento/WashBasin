#!/usr/bin/env python
#-*- coding:utf-8 -*-
#ここで補正を行う
#事前に計測し20*20に集約されたデータに補正のための行列を使って「一枚づつ」補正を行う
#その後、補正されたデータを連結する

import glob
import os,commands
import os.path
import csv
import numpy as np
from tqdm import tqdm
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")

class CalibrationClass:

    """データの補正を行う"""

    # def __init__(self):

    def calibration(self,data_path,save_path):
        cal_map = np.zeros([20, 20])

        #対象のデータと補正用の行列を開く
        data = np.loadtxt(data_path,delimiter=',')
        calibration_map = np.loadtxt('./calibration_map.csv',delimiter=',')
        cal_map = calibration_map * data#掛け合わせることによって補正

        np.savetxt(save_path,cal_map,delimiter=',')#修正後行列を保存


#データの補正を行う
CalCla = CalibrationClass()
DirPath_list = glob.glob('./CSV/Convolution/*')#'./CSV/Convolution/jyu',...

if os.path.isdir('./CSV/Calibration') == False:#なければ保存用のディレクトリ作成
    os.mkdir('./CSV/Calibration')

for DirPath in DirPath_list:

    DirSavePath = DirPath.replace('Convolution','Calibration')
    if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
        os.mkdir(DirSavePath)

    TryNumPath_list = glob.glob(DirPath+'/*')#'./CSV/Convolution/jyu/1',...

    for TryNumPath in TryNumPath_list :#試行回数分、回転('1', '2', '3',...)

        TryNumSavePath = TryNumPath.replace('Convolution','Calibration')
        if os.path.isdir(TryNumSavePath) == False:#なければ保存用のディレクトリ作成
            os.mkdir(TryNumSavePath)

        CsvPath_list = glob.glob(TryNumPath+'/*')#'./CSV/Convolution/jyu/1/CSP1427000000.csv',...

        for CsvPath in CsvPath_list:#フレーム分、回転('CSP1427000000.csv', 'CSP1427000001.csv',...)
            CsvSavePath = CsvPath.replace('Convolution','Calibration')
            CalCla.calibration(CsvPath,CsvSavePath)#データの補正
