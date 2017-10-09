#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Convolution_point.pyをクラス化したもの。
#./CSV/Cleaned/ 以下のデータを60*60から30*30に集約し ./CSV/Convolution/ に保存
#そのポイントの2秒間分(10データ)を[平均,中央,最頻,分散,標準偏差]の30*30の5つのcsvファイルを作成

import glob
import os, commands
import os.path
import csv
import numpy as np
from scipy import stats
from tqdm import tqdm
import matplotlib.pyplot as plt
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")#.DS_Storeファイルを取り除く


class ConvolutionClass:

    """60*60から15*16に集約する"""

    # def __init__(self):

    #60*60*10から30*30*10に集約
    def convolution(self,data_path,save_path):
        convolution_map = np.zeros([15, 16])#集約後の行列の初期化
        data = np.loadtxt(data_path,delimiter=',')#対象のファイルと整形後のファイルを開く

        for line in range(15):
            for column in range(16) :
                if np.sum(data[line*4:line*4+4,column*4:column*4+4]) == 0:
                    ave = 0
                else:
                    ave = np.mean(data[line*4:line*4+4,column*4:column*4+4])

                convolution_map[line][column] = ave#16マスの平均で畳み込み

        np.savetxt(save_path,convolution_map,delimiter=',')#集約後行列を保存

    #15*16*10から15*16に集約
    def calibrationMapGenerator(self,dirpath_list):
        mean_map = np.zeros([15, 16])#集約後の行列の初期化(平均)
        med_map = np.zeros([15, 16])#集約後の行列の初期化(中央)
        mode_map = np.zeros([15, 16])#集約後の行列の初期化(最頻値)
        var_map = np.zeros([15, 16])#集約後の行列の初期化(分散)
        sd_map = np.zeros([15, 16])#集約後の行列の初期化(標準偏差)

        for DirPath in dirpath_list:#1-1,1-2,...毎

            CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Convolution/1-1/CSP1956000000.csv',...
            CsvName_list = os.listdir(DirPath)#'CSP1956000000.csv',...
            num = DirPath.replace('./CSV/Convolution/','')#'1-1/CSP1956000000.csv',...
            num=num.split("-")#[1] [1/CSP1956000000.csv],...
            line = int(num[0])-1#[1]-1
            column = int(num[1])-1#[1(/CSP1956000000.csv)]-1,...
            holder = np.array([])#そのポイントの2秒間分(10データ)を格納する配列の初期化

            for CsvPath in CsvPath_list:#CSP1956000000.csv,...毎
                data = np.loadtxt(CsvPath,delimiter=',')#対象のファイルのファイルを開く
                holder = np.append(holder,data[line,column])#そのポイントの2秒間分(10データ)を格納

            #平均値
            mean_map[line,column] = np.average(holder)
            #中央値
            med_map[line,column] = np.median(holder)
            #最頻値
            mode_map[line,column] = stats.mode(holder)[0]
            #分散
            var_map[line,column] = np.var(holder)
            #標準偏差
            sd_map[line,column] = np.std(holder)

        np.savetxt('mean_map.csv',mean_map,delimiter=',')#集約後行列を保存(平均)
        np.savetxt('med_map.csv',med_map,delimiter=',')#集約後行列を保存(中央)
        np.savetxt('mode_map.csv',mode_map,delimiter=',')#集約後行列を保存(最頻値)
        np.savetxt('var_map.csv',var_map,delimiter=',')#集約後行列を保存(分散)
        np.savetxt('sd_map.csv',sd_map,delimiter=',')#集約後行列を保存(標準偏差)

        mean_map = np.loadtxt('./mean_map.csv',delimiter=',')
        #外周と中央の縁部分を取り除く
        mean_map = np.delete(mean_map, 0, 0)#行削除
        mean_map = np.delete(mean_map, -1, 0)#行削除
        mean_map = np.delete(mean_map, 7, 1)#列削除
        mean_map = np.delete(mean_map, 0, 1)#列削除
        mean_map = np.delete(mean_map, -1, 1)#列削除

        mean_list=mean_map.reshape(-1,)#一次元配列に
        i=mean_list.nonzero()#0以外を取り除く
        print stats.mode(mean_list[i])
        mean_hist_1000_hist = np.c_[np.append(np.histogram(mean_list[i], bins=1000)[0], 0 ), np.histogram(mean_list[i], bins=1000)[1]]
        np.savetxt('mean_hist_1000_hist.csv',mean_hist_1000_hist,delimiter=',', fmt='%d')
        print mean_hist_1000_hist[np.argmax(mean_hist_1000_hist[:,0]),1]
        # print np.argmax(mean_hist_1000_hist[:,0])
        mean_hist_500_hist = np.c_[np.append(np.histogram(mean_list[i], bins=500)[0], 0 ), np.histogram(mean_list[i], bins=500)[1]]
        np.savetxt('mean_hist_500_hist.csv',mean_hist_500_hist,delimiter=',', fmt='%d')
        print mean_hist_500_hist[np.argmax(mean_hist_500_hist[:,0]),1]
        # print np.argmax(mean_hist_500_hist[:,0])
        mean_hist_100_hist = np.c_[np.append(np.histogram(mean_list[i], bins=100)[0], 0 ), np.histogram(mean_list[i], bins=100)[1]]
        np.savetxt('mean_hist_100_hist.csv',mean_hist_100_hist,delimiter=',', fmt='%d')
        print mean_hist_100_hist[np.argmax(mean_hist_100_hist[:,0]),1]
        # print np.argmax(mean_hist_100_hist[:,0])


        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mean_list, bins=1000)
        plt.savefig('./mean_1000.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mean_list, bins=500)
        plt.savefig('./mean_500.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mean_list, bins=100)
        plt.savefig('./mean_100.png')

        med_map = np.loadtxt('./med_map.csv',delimiter=',')
        #外周と中央の縁部分を取り除く
        med_map = np.delete(med_map, 0, 0)#行削除
        med_map = np.delete(med_map, -1, 0)#行削除
        med_map = np.delete(med_map, 7, 1)#列削除
        med_map = np.delete(med_map, 0, 1)#列削除
        med_map = np.delete(med_map, -1, 1)#列削除

        med_list = med_map.reshape(-1,)#一次元配列に
        i = med_list.nonzero()#0以外を取り除く
        print stats.mode(med_list[i])
        med_hist_1000_hist = np.c_[np.append(np.histogram(med_list[i], bins=1000)[0], 0 ), np.histogram(med_list[i], bins=1000)[1]]
        np.savetxt('med_hist_1000_hist.csv',med_hist_1000_hist,delimiter=',', fmt='%d')
        print med_hist_1000_hist[np.argmax(med_hist_1000_hist[:,0]),1]
        # print np.argmax(med_hist_1000_hist[:,0])
        med_hist_500_hist = np.c_[np.append(np.histogram(med_list[i], bins=500)[0], 0 ), np.histogram(med_list[i], bins=500)[1]]
        np.savetxt('med_hist_500_hist.csv',med_hist_500_hist,delimiter=',', fmt='%d')
        print med_hist_500_hist[np.argmax(med_hist_500_hist[:,0]),1]
        # print np.argmax(med_hist_500_hist[:,0])
        med_hist_100_hist = np.c_[np.append(np.histogram(med_list[i], bins=100)[0], 0 ), np.histogram(med_list[i], bins=100)[1]]
        np.savetxt('med_hist_100_hist.csv',med_hist_100_hist,delimiter=',', fmt='%d')
        print med_hist_100_hist[np.argmax(med_hist_100_hist[:,0]),1]
        # print np.argmax(med_hist_100_hist[:,0])

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(med_list, bins=1000)
        plt.savefig('./med_1000.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(med_list, bins=500)
        plt.savefig('./med_500.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(med_list, bins=100)
        plt.savefig('./med_100.png')

        mod_map = np.loadtxt('./mode_map.csv',delimiter=',')
        #外周と中央の縁部分を取り除く
        mod_map = np.delete(mod_map, 0, 0)#行削除
        mod_map = np.delete(mod_map, -1, 0)#行削除
        mod_map = np.delete(mod_map, 7, 1)#列削除
        mod_map = np.delete(mod_map, 0, 1)#列削除
        mod_map = np.delete(mod_map, -1, 1)#列削除

        mod_list = mod_map.reshape(-1,)#一次元配列に
        i = mod_list.nonzero()#0以外を取り除く
        print stats.mode(mod_list[i])
        mod_hist_1000_hist = np.c_[np.append(np.histogram(mod_list[i], bins=1000)[0], 0 ), np.histogram(mod_list[i], bins=1000)[1]]
        np.savetxt('mod_hist_1000_hist.csv',mod_hist_1000_hist,delimiter=',', fmt='%d')
        print mod_hist_1000_hist[np.argmax(mod_hist_1000_hist[:,0]),1]
        # print np.argmax(mod_hist_1000_hist[:,0])
        mod_hist_500_hist = np.c_[np.append(np.histogram(mod_list[i], bins=500)[0], 0 ), np.histogram(mod_list[i], bins=500)[1]]
        np.savetxt('mod_hist_500_hist.csv',mod_hist_500_hist,delimiter=',', fmt='%d')
        print mod_hist_500_hist[np.argmax(mod_hist_500_hist[:,0]),1]
        # print np.argmax(mod_hist_500_hist[:,0])
        mod_hist_100_hist = np.c_[np.append(np.histogram(mod_list[i], bins=100)[0], 0 ), np.histogram(mod_list[i], bins=100)[1]]
        np.savetxt('mod_hist_100_hist.csv',mod_hist_100_hist,delimiter=',', fmt='%d')
        print mod_hist_100_hist[np.argmax(mod_hist_100_hist[:,0]),1]
        # print np.argmax(mod_hist_100_hist[:,0])

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mod_list, bins=1000)
        plt.savefig('./mod_1000.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mod_list, bins=500)
        plt.savefig('./mod_500.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mod_list, bins=100)
        plt.savefig('./mod_100.png')


ConCla = ConvolutionClass()
DirPath_list = glob.glob('./CSV/Cleaned/*')#'./CSV/Cleaned/1-1',...

if os.path.isdir('./CSV/Convolution') == False:#なければ保存用のディレクトリ作成
    os.mkdir('./CSV/Convolution')

for DirPath in tqdm(DirPath_list):

    DirSavePath = DirPath.replace('Cleaned','Convolution')
    if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
        os.mkdir(DirSavePath)

    CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Cleaned/1-1/CSP1956000000.csv',...

    for CsvPath in CsvPath_list:

        CsvSavePath = CsvPath.replace('Cleaned','Convolution')#'./CSV/Convolution/1-1/CSP1956000000.csv',...
        #./CSV/Cleaned/ 以下のデータを60*60から30*30に集約し ./CSV/Convolution/ に保存
        ConCla.convolution(CsvPath,CsvSavePath)

DirPath_list = glob.glob('./CSV/Convolution/*')#'./CSV/Convolution/1-1',...
#そのポイントの2秒間分(10データ)を[平均,中央,最頻,分散,標準偏差]の30*30の5つのcsvファイルを作成
ConCla.calibrationMapGenerator(DirPath_list)
