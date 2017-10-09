#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Convolution_point.pyをクラス化したもの。
#検証データ(重りを乗せていって得たデータ)から得られた集約データ及び誤差割合データの算出は行わない。
#すでに、誤差割合データを求めているものとする
#ので、ここでは数値のみが入った60*60から9ポイントづつを集約して20*20のデータに変換するだけのプログラムである。

import glob
import os, commands
import os.path
import csv
import numpy as np
from tqdm import tqdm
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")


class ConvolutionClass:

    """60*60から20*20に集約する"""

    # def __init__(self):

    def convolution(self,data_path,save_path):#60*60から20*20に集約する
        convolution_map = np.zeros([20, 20])#集約後の行列の初期化
        data = np.loadtxt(data_path,delimiter=',')#対象のファイルと整形後のファイルを開く
        for line in range(20):
            for column in range(20) :

                if np.sum(data[line*3:line*3+3,column*3:column*3+3]) == 0:
                    ave = 0
                else:
                    ave = np.mean(data[line*3:line*3+3,column*3:column*3+3])

                convolution_map[line][column] = ave

        np.savetxt(save_path,convolution_map,delimiter=',')#集約後行列を保存



ConCla = ConvolutionClass()
DirPath_list = glob.glob('./CSV/Cleaned/*')#'./CSV/Cleaned/1965',...

if os.path.isdir('./CSV/Convolution') == False:#なければ保存用のディレクトリ作成
    os.mkdir('./CSV/Convolution')

for DirPath in tqdm(DirPath_list):

    DirSavePath = DirPath.replace('Cleaned','Convolution')
    if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
        os.mkdir(DirSavePath)

    TryNumPath_list = glob.glob(DirPath+'/*')#'./CSV/Cleaned/jyu/1',...

    for TryNumPath in TryNumPath_list :#試行回数分、回転('1', '2', '3',...)

        TryNumSavePath = TryNumPath.replace('Cleaned','Convolution')
        if os.path.isdir(TryNumSavePath) == False:#なければ保存用のディレクトリ作成
            os.mkdir(TryNumSavePath)

        CsvPath_list = glob.glob(TryNumPath+'/*')#'./CSV/Cleaned/jyu/1/CSP1427000000.csv',...

        for CsvPath in CsvPath_list:#フレーム分、回転('CSP1427000000.csv', 'CSP1427000001.csv',...)
            CsvSavePath = CsvPath.replace('Cleaned','Convolution')
            ConCla.convolution(CsvPath,CsvSavePath)#生データのいらない部分を削除して整形
