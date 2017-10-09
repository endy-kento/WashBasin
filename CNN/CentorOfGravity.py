#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import glob
import os, commands
import os.path
import csv
from tqdm import tqdm
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")


class CentorOfGravityClass:

    """フレーム毎の全体、各足の重心を求める"""

    # def __init__(self):

    def centorofgravity(self,data_path,centcsv_path):
        #対象のファイルと整形後のファイルを開く
        file_in = open(data_path,"r")
        file_out = open(centcsv_path,"w")

        data = np.loadtxt(data_path,delimiter=',')
        row, col = data.shape

        addx = addy = addz = Laddx = Laddy = Laddz = Raddx = Raddy = Raddz = 0

        for rows in range(20):
            for cols in range(20) :
                addx = addx + rows*float(data[rows][cols])
                addy = addy + cols*float(data[rows][cols])
                addz = addz + float(data[rows][cols])
                if  col/2 > cols:
                    Laddx = Laddx + rows*float(data[rows][cols])
                    Laddy = Laddy + cols*float(data[rows][cols])
                    Laddz = Laddz + float(data[rows][cols])
                else:
                    Raddx = Raddx + rows*float(data[rows][cols])
                    Raddy = Raddy + cols*float(data[rows][cols])
                    Raddz = Raddz + float(data[rows][cols])

        if addx or addy or addz != 0:
            xg=addx/rows*rows/addz
            yg=addy/rows*rows/addz
        else:
            xg=0
            yg=0

        if Laddx or Laddy or Laddz != 0:
            Lxg=Laddx/rows*rows/Laddz
            Lyg=Laddy/rows*rows/Laddz
        else:
            Lxg=0
            Lyg=0

        if Raddx or Raddy or Raddz != 0:
            Rxg=Raddx/rows*rows/Raddz
            Ryg=Raddy/rows*rows/Raddz
        else:
            Rxg=0
            Ryg=0

        file_out.write(str(xg)+','+str(yg)+','+str(Lxg)+','+str(Lyg)+','+str(Rxg)+','+str(Ryg)+'\n')

        #開いたものを閉じる
        file_in.close()
        file_out.close()

#集約後のデータの重心を求める
COGCla=CentorOfGravityClass()
DirPath_list = glob.glob('./CSV/Calibration/*')#'./CSV/Calibration/jyu',...

if os.path.isdir('./CSV/CentorOfGravity') == False:#なければ保存用のディレクトリ作成
    os.mkdir('./CSV/CentorOfGravity')

for DirPath in tqdm(DirPath_list):

    DirSavePath = DirPath.replace('Calibration','CentorOfGravity')
    if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
        os.mkdir(DirSavePath)

    TryNumPath_list = glob.glob(DirPath+'/*')#'./CSV/Calibration/jyu/1',...

    for TryNumPath in TryNumPath_list :#試行回数分、回転('1', '2', '3',...)

        TryNumSavePath = TryNumPath.replace('Calibration','CentorOfGravity')
        if os.path.isdir(TryNumSavePath) == False:#なければ保存用のディレクトリ作成
            os.mkdir(TryNumSavePath)

        CsvPath_list = glob.glob(TryNumPath+'/*')#'./CSV/Calibration/jyu/1/CSP1427000000.csv',...

        for CsvPath in CsvPath_list:#フレーム分、回転('CSP1427000000.csv', 'CSP1427000001.csv',...)
            CsvSavePath = CsvPath.replace('Calibration','CentorOfGravity')#'./CSV/Calibration/jyu/1/CSP1956000000.csv',...
            COGCla.centorofgravity(CsvPath,CsvSavePath)#重心の計算
