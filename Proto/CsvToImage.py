#!/usr/bin/env python
#-*- coding:utf-8 -*-

import glob
import os, commands
import os.path
import csv
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import shutil
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")

class CsvToImageClass:

    """csvデータから画像を作成する"""

    def __init__(self):
        self.all_count = 0

    def csvtoimage(self,data_path,save_path):
        listlist =[]

        #データを引っ張ってくる
        data = np.loadtxt(data_path,delimiter=',')

        #重心のデータを引っ張ってくる
        centdata_path = data_path.replace('Convolution','CentorOfGravity')
        centdata = np.loadtxt(centdata_path,delimiter=',')

        #カラーバーの上限下限を決めるための全結合のファイル中の、最大と最小
        # max=np.max(data)
        # min=np.min(data)

        #listlistに先頭から一行ずつ貯めていって、20行たまると描画し、保存
        for rows in range(20):
            for cols in range(20) :
                introw = map(self.string2int,data[rows][cols])
                listlist.append(introw);

        #カラーバー含め、描画
        src = np.array(listlist)

        #画像のみにするために左、下のラベル消去
        plt.tick_params(labelbottom='off')
        plt.tick_params(labelleft='off')

        plt.imshow(src,cmap=plt.cm.cool,clim=(0,60000))
        # plt.colorbar()
        # https://matplotlib.org/examples/color/colormaps_reference.html

        #重心のファイルからそれぞれのデータを持ってくる
        X = centdata[0]
        Y = centdata[1]
        LX = centdata[2]
        LY = centdata[3]
        RX = centdata[4]
        RY = centdata[5]

        #両足の重心
        if X or Y != 0:
            plt.plot(X, Y,marker="*", markersize=10,color="r")
        #左足の重心
        if LX or LY != 0:
            plt.plot(LX, LY,marker="*", markersize=10,color="g")
        #右足の重心
        if RX or RY != 0:
            plt.plot(RX, RY,marker="*", markersize=10,color="y")

        #画像を名前をつけて保存
        # data_name = data_name.replace('Cent', '')
        # filename = allimage_path+'/'+str(filenum)+".png"

        plt.savefig(save_path,bbox_inches='tight',pad_inches=-0.05)
        # shutil.copyfile(filename, save_path)
        #https://mzmttks.blogspot.jp/2012/01/pylab-2.html
        plt.close()

        #listlistを初期化
        listlist = []

    def string2int(self,str):
        if(str):
            return float(str)
        else:
            return 0


#集約後のデータを画像化し、学習用データと検証用データに分けて保存
CTICla = CsvToImageClass()
if os.path.isdir('./Image') == False:#なければ保存用のディレクトリ作成
    os.mkdir('./Image')

Data_DirPath_list = glob.glob('./CSV/Convolution/*')#'./CSV/Convolution/1965',...

for Data_DirPath in Data_DirPath_list:

        DirSavePath = Data_DirPath.replace('CSV/Convolution','Image')

        if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
            os.mkdir(DirSavePath)

        CsvPath_list = glob.glob(Data_DirPath+'/*.csv')#'./CSV/Convolution/1965/CSP1956000000.csv',...

        for CsvPath in CsvPath_list:

            CsvSavePath = CsvPath.replace('CSV/Convolution','Image')#'./CSV/Image/1965/CSP1956000000.csv',...
            CsvSavePath = CsvSavePath.replace('.csv','.png')#'./CSV/Image/1965/CSP1956000000.png',...
            CTICla.csvtoimage(CsvPath,CsvSavePath)
