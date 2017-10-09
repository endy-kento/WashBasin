#!/usr/bin/env python
# coding: utf-8
#指定した次元の補正関数を作成し、保存する
#引数に第一 : 次元数
#ex) python CabMapGen.py 1 new

import glob
import os, commands
import os.path
from tqdm import tqdm
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.optimize import curve_fit
from scipy.optimize import nnls
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")
args = sys.argv

class CabMapGenClass:

    #0以外のインデックスを選出
    def get_NonZeroIndex(self,data,line,column):
        i=data[line,column,:].nonzero()
        i=i[0].tolist()
        ilen =len(i)
        if ilen==0:
            i.append(0)
        return i


    def get_3d(self,line,column):

        #0以外のインデックスを選出
        i = self.get_NonZeroIndex(First,line,column)
        j = self.get_NonZeroIndex(Second,line,column)
        k = self.get_NonZeroIndex(Third,line,column)
        l = self.get_NonZeroIndex(Fourth,line,column)
        m = self.get_NonZeroIndex(Fifth,line,column)

        #全てのサンプルを使用する
        #ソートの後、最大最小を取り除いている
        allSample = []
        allSample=np.r_[allSample,np.sort(First[line][column][:])[1:-1]]
        allSample=np.r_[allSample,np.sort(Second[line][column][:])[1:-1]]
        allSample=np.r_[allSample,np.sort(Third[line][column][:])[1:-1]]
        allSample=np.r_[allSample,np.sort(Fourth[line][column][:])[1:-1]]
        allSample=np.r_[allSample,np.sort(Fifth[line][column][:])[1:-1]]


        #0以外のインデックスの中から最頻値を代表点として選出して使用する
        repSample = []
        repSample = np.r_[repSample,stats.mode(First[line,column,i], axis=None)[0][0]]
        repSample = np.r_[repSample,stats.mode(Second[line,column,j], axis=None)[0][0]]
        repSample = np.r_[repSample,stats.mode(Third[line,column,k], axis=None)[0][0]]
        repSample = np.r_[repSample,stats.mode(Fourth[line,column,l], axis=None)[0][0]]
        repSample = np.r_[repSample,stats.mode(Fifth[line,column,m], axis=None)[0][0]]

        # return allGrams,allSample
        return allSample,repSample


    def cabMapGen(self,x,y,repSample,deg,new):
        if deg =='1':
            #全てのサンプルを使用して回帰直線を計算
            all_a, all_b = np.polyfit(x, y, deg)
            all_cab_deg1_map[line,column,0] = all_a
            all_cab_deg1_map[line,column,1] = all_b

            #代表点を使用して回帰曲線を計算
            rep_a_rep , rep_b_rep = np.polyfit([ 50 , 55.5 , 62.5 , 93.75 , 111.1 ], repSample, deg)
            rep_cab_deg1_map[line,column,0] = rep_a_rep
            rep_cab_deg1_map[line,column,1] = rep_b_rep
            if new == 'new':
                np.save("./NewCabMaps_nonzero/all_cab_deg1_map.npy", all_cab_deg1_map)
                np.save("./NewCabMaps_nonzero/rep_cab_deg1_map.npy", rep_cab_deg1_map)
            else:
                np.save("./CabMaps_nonzero/all_cab_deg1_map.npy", all_cab_deg1_map)
                np.save("./CabMaps_nonzero/rep_cab_deg1_map.npy", rep_cab_deg1_map)

if __name__ == '__main__':
    CMG = CabMapGenClass()

    # if os.path.isdir('./CabMaps') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./CabMaps')
    if os.path.isdir('./CabMaps_nonzero') == False:#なければ保存用のディレクトリ作成
        os.mkdir('./CabMaps_nonzero')
    if os.path.isdir('./NewCabMaps_nonzero') == False:#なければ保存用のディレクトリ作成
        os.mkdir('./NewCabMaps_nonzero')

    if args[2]=='new':
        #各重さのサンプルデータ(修正後)
        First = np.load("../npyGen/NPY/Cabed_Ave_Sample/50gp.npy")
        Second = np.load("../npyGen/NPY/Cabed_Ave_Sample/55.5gp.npy")
        Third = np.load("../npyGen/NPY/Cabed_Ave_Sample/62.5gp.npy")
        Fourth = np.load("../npyGen/NPY/Cabed_Ave_Sample/93.75gp.npy")
        Fifth = np.load("../npyGen/NPY/Cabed_Ave_Sample/111.1gp.npy")
    else:
        #各重さのサンプルデータ(未修正)
        First = np.load("../npyGen/NPY/50gp.npy")
        Second = np.load("../npyGen/NPY/55.5gp.npy")
        Third = np.load("../npyGen/NPY/62.5gp.npy")
        Fourth = np.load("../npyGen/NPY/93.75gp.npy")
        Fifth = np.load("../npyGen/NPY/111.1gp.npy")

    all_cab_deg1_map = np.zeros([60,60,2])#全てのサンプルデータを用いた回帰直線
    rep_cab_deg1_map = np.zeros([60,60,2])#代表点を用いた回帰直線

    allGrams =[]
    for z in range(8):
        allGrams.append(50)
    for z in range(8):
        allGrams.append(55.5)
    for z in range(8):
        allGrams.append(62.5)
    for z in range(98):
        allGrams.append(93.75)
    for z in range(98):
        allGrams.append(111.1)
    allGrams = np.array(allGrams,dtype=np.float32)

    for line in tqdm(range(60)):
        for column in range(60):
            allSample,repSample = CMG.get_3d(line,column)

            CMG.cabMapGen(allGrams,allSample,repSample,args[1],args[2])
