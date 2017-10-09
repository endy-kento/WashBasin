#!/usr/bin/env python
#-*- coding:utf-8 -*-
#ここで補正を行う
#事前に計測し20*20に集約されたデータに補正のための行列を使って「一枚づつ」補正を行う
#その後、補正されたデータを連結する

import glob
import os,commands
import os.path
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
DirPath_list = glob.glob('./CSV/Convolution/*')#'./CSV/Convolution/1965',...

if os.path.isdir('./CSV/Calibration') == False:#なければ保存用のディレクトリ作成
    os.mkdir('./CSV/Calibration')

for DirPath in DirPath_list:

        DirSavePath = DirPath.replace('Convolution','Calibration')#'./CSV/Calibration/1965',...
        if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
            os.mkdir(DirSavePath)

        CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Convolution/1965/CSP1956000000.csv',...

        for CsvPath in CsvPath_list:

            CsvSavePath = CsvPath.replace('Convolution','Calibration')#'./CSV/Calibration/1965/CSP1956000000.csv',...
            CalCla.calibration(CsvPath,CsvSavePath)#データの補正
