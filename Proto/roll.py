#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import glob
import os, commands
import os.path
import csv
from tqdm import tqdm
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")

class RollClass:

    """補正後の行列を90,180,270度回転させたものを作成"""

    # def __init__(self):

    def roll(self,data_path,rollcsv_path):
        #対象のファイルと整形後のファイルを開く
        file_in = open(data_path,"r")


        data = np.loadtxt(data_path,delimiter=',')

        row, col = data.shape
        row=row-1
        col=col-1

        roll_90_map = np.zeros([20, 20])
        roll_180_map = np.zeros([20, 20])
        roll_270_map = np.zeros([20, 20])
        for rows in range(20):
            for cols in range(20) :
                roll_90_map[cols,row-rows]  = data[rows,cols]
                roll_180_map[row-rows,col-cols] = data[rows,cols]
                roll_270_map[col-cols,rows] = data[rows,cols]


        CsvSavePath_90 = rollcsv_path.replace('Roll_X','Roll_90')
        CsvSavePath_180 = rollcsv_path.replace('Roll_X','Roll_180')
        CsvSavePath_270 = rollcsv_path.replace('Roll_X','Roll_270')
        np.savetxt(CsvSavePath_90,roll_90_map,delimiter=',',fmt="%.0f")
        np.savetxt(CsvSavePath_180,roll_180_map,delimiter=',',fmt="%.0f")
        np.savetxt(CsvSavePath_270,roll_270_map,delimiter=',',fmt="%.0f")

        #開いたものを閉じる
        file_in.close()


#集約後のデータの重心を求める
RolCla=RollClass()
DirPath_list = glob.glob('./CSV/Calibration/*')#'./CSV/Calibration/1965',...

if os.path.isdir('./CSV/Roll_90') == False:#なければ保存用のディレクトリ作成
	os.mkdir('./CSV/Roll_90')
if os.path.isdir('./CSV/Roll_180') == False:#なければ保存用のディレクトリ作成
	os.mkdir('./CSV/Roll_180')
if os.path.isdir('./CSV/Roll_270') == False:#なければ保存用のディレクトリ作成
    os.mkdir('./CSV/Roll_270')

for DirPath in DirPath_list:

		DirSavePath = DirPath.replace('Calibration','Roll_90')
		if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
			os.mkdir(DirSavePath)
		DirSavePath = DirPath.replace('Calibration','Roll_180')
		if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
			os.mkdir(DirSavePath)
		DirSavePath = DirPath.replace('Calibration','Roll_270')
		if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
			os.mkdir(DirSavePath)

		CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Calibration/1965/CSP1956000000.csv',...

		for CsvPath in CsvPath_list:

			CsvSavePath = CsvPath.replace('Calibration','Roll_X')#'./CSV/CentorOfGravity/1965/CSP1956000000.csv',...
			RolCla.roll(CsvPath,CsvSavePath)
