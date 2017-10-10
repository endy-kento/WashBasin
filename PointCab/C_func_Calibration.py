#!/usr/bin/env python
#-*- coding:utf-8 -*-
#個人の直立データに補正関数をかけたものをnpy形式で出力する
#ex) python Calibration.py 1 new

import glob
import os, commands
from tqdm import tqdm
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")
args = sys.argv


class C_func_CalibrationClass:
    """補正関数を使用し、キャリブレーションを行う"""
    def cabTest(self,person,deg,tryNum,figSavePath):

        all_cabed_map = np.zeros([60,60,10])#一試行のnpyファイル全体に補正関数をかけた配列
        rep_cabed_map = np.zeros([60,60,10])#一試行のnpyファイル全体に補正関数をかけた配列

        for line in range(60):
            for column in range(60):
                for count in range(10):

                    #個人データに全サンプルを用いた回帰直線を補正関数として使用する
                    if person[line,column,count] <= 0 or  all_cab_deg1_map[line,column,0] == 0:
                        all_cabed_map[line,column,count] = 0
                    else:
                        all_cabed_map[line,column,count] = ( person[line,column,count] - all_cab_deg1_map[line,column,1] ) / all_cab_deg1_map[line,column,0]
                        if all_cabed_map[line,column,count] <= 0:
                            all_cabed_map[line,column,count] = 0

                    #個人データに代表点を用いた回帰直線を補正関数として使用する
                    if person[line,column,count] <= 0 or  rep_cab_deg1_map[line,column,0] == 0:
                        rep_cabed_map[line,column,count] = 0
                    else:
                        rep_cabed_map[line,column,count] = ( person[line,column,count] - rep_cab_deg1_map[line,column,1] ) / rep_cab_deg1_map[line,column,0]
                        if rep_cabed_map[line,column,count] <= 0:
                            rep_cabed_map[line,column,count] = 0

        np.save(figSavePath+"cabed_all_"+tryNum+".npy", all_cabed_map)#'./Cabed_Person/jyu/1/cabed_all_1.npy'
        np.save(figSavePath+"cabed_rep_"+tryNum+".npy", rep_cabed_map)#'./Cabed_Person/jyu/1/cabed_rep_1.npy'

    def Dentcab(self,Dent,deg,tryNum,npySavePath):

        line,column,count = Dent.shape
        print Dent.shape
        all_cabed_map = np.zeros([line,column,count])#一試行のnpyファイル全体に補正関数をかけた配列
        rep_cabed_map = np.zeros([line,column,count])#一試行のnpyファイル全体に補正関数をかけた配列

        for lines in range(line):
            for columns in range(column):
                for counts in range(count):

                    #個人データに全サンプルを用いた回帰直線を補正関数として使用する
                    if Dent[lines,columns,counts] <= 0 or  all_cab_deg1_map[lines,columns,0] == 0:
                        all_cabed_map[lines,columns,counts] = 0
                    else:
                        all_cabed_map[lines,columns,counts] = ( Dent[lines,columns,counts] - all_cab_deg1_map[lines,columns,1] ) / all_cab_deg1_map[lines,columns,0]
                        if all_cabed_map[lines,columns,counts] <= 0:
                            all_cabed_map[lines,columns,counts] = 0

                    #個人データに代表点を用いた回帰直線を補正関数として使用する
                    if Dent[lines,columns,counts] <= 0 or  rep_cab_deg1_map[lines,columns,0] == 0:
                        rep_cabed_map[lines,columns,counts] = 0
                    else:
                        rep_cabed_map[lines,columns,counts] = ( Dent[lines,columns,counts] - rep_cab_deg1_map[lines,columns,1] ) / rep_cab_deg1_map[lines,columns,0]
                        if rep_cabed_map[lines,columns,counts] <= 0:
                            rep_cabed_map[lines,columns,counts] = 0

        np.save(npySavePath+"_cabed_all.npy", all_cabed_map)#'./Cabed_Person/jyu/1/cabed_all_1.npy'
        np.save(npySavePath+"_cabed_rep.npy", rep_cabed_map)#'./Cabed_Person/jyu/1/cabed_rep_1.npy'

    def Motion_cab(self,Motion,npySavePath):

        line,column,count = Motion.shape
        all_cabed_map = np.zeros([line,column,count])#一試行のnpyファイル全体に補正関数をかけた配列
        rep_cabed_map = np.zeros([line,column,count])#一試行のnpyファイル全体に補正関数をかけた配列

        for lines in range(line):
            for columns in range(column):
                for counts in range(count):

                    #個人データに全サンプルを用いた回帰直線を補正関数として使用する
                    if Motion[lines,columns,counts] <= 0 or  all_cab_deg1_map[lines,columns,0] == 0:
                        all_cabed_map[lines,columns,counts] = 0
                    else:
                        all_cabed_map[lines,columns,counts] = ( Motion[lines,columns,counts] - all_cab_deg1_map[lines,columns,1] ) / all_cab_deg1_map[lines,columns,0]
                        if all_cabed_map[lines,columns,counts] <= 0:
                            all_cabed_map[lines,columns,counts] = 0

                    #個人データに代表点を用いた回帰直線を補正関数として使用する
                    if Motion[lines,columns,counts] <= 0 or  rep_cab_deg1_map[lines,columns,0] == 0:
                        rep_cabed_map[lines,columns,counts] = 0
                    else:
                        rep_cabed_map[lines,columns,counts] = ( Motion[lines,columns,counts] - rep_cab_deg1_map[lines,columns,1] ) / rep_cab_deg1_map[lines,columns,0]
                        if rep_cabed_map[lines,columns,counts] <= 0:
                            rep_cabed_map[lines,columns,counts] = 0

        np.save(npySavePath+"/cabed_all.npy", all_cabed_map)#'./Cabed_Person/jyu/1/cabed_all_1.npy'
        np.save(npySavePath+"/cabed_rep.npy", rep_cabed_map)#'./Cabed_Person/jyu/1/cabed_rep_1.npy'


if __name__ == '__main__':
    CfC = C_func_CalibrationClass()

    all_cab_deg1_map = np.load("./NewCabMaps_nonzero/all_cab_deg1_map.npy")#全てのサンプルデータを用いた回帰直線
    rep_cab_deg1_map = np.load("./NewCabMaps_nonzero/rep_cab_deg1_map.npy")#代表点を用いた回帰直線

    if args[2]=='NewPerson':
        if os.path.isdir('./NewCabed_Person') == False:#なければ保存用のディレクトリ作成
            os.mkdir('./NewCabed_Person')
        DirPath_list = glob.glob('../npyGen/NPY/Person/*')#'../npyGen/NPY/Person/jyu',...

        for DirPath in tqdm(DirPath_list):

                DirSavePath = DirPath.replace('../npyGen/NPY/','./NewCabed_')#'./NewCabed_Person/jyu'...
                if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
                    os.mkdir(DirSavePath)#'./NewCabed_Person/jyu'...

                npyPath_list = glob.glob(DirPath+'/*.npy')#'../npyGen/NPY/Person/jyu/1.npy',...
                count = 1
                for npyPath in npyPath_list:
                    npySavePath = npyPath.replace('../npyGen/NPY/','./NewCabed_')#'./NewCabed_Person/jyu/1.npy'...
                    npySavePath = npySavePath.replace('.npy','')#'./NewCabed_Person/jyu/1'...
                    if os.path.isdir(npySavePath) == False:#なければ保存用のディレクトリ作成
                        os.mkdir(npySavePath)#'./NewCabed_Person/jyu/1'...
                    person = np.load(npyPath)
                    CfC.cabTest(person,args[1],str(count),DirSavePath+'/')
                    count = count +1

    elif args[2]=='Dent':


        if os.path.isdir('./NewCabed_Dent') == False:#なければ保存用のディレクトリ作成
            os.mkdir('./NewCabed_Dent')

        npyPath_list = glob.glob('../npyGen/NPY/Dentifrice_Cleaned/*.npy')#'../npyGen/NPY/Dentifrice_Cleaned/1964.npy',...
        count = 1
        for npyPath in tqdm(npyPath_list):
            npySavePath = npyPath.replace('../npyGen/NPY/Dentifrice_Cleaned','./NewCabed_Dent')#'./NewCabed_Dent/1964.npy'...
            npySavePath = npySavePath.replace('.npy','')#'./NewCabed_Dent/1964'...
            Dentdata = np.load(npyPath)
            CfC.Dentcab(Dentdata,args[1],str(count),npySavePath)
            count = count +1


    elif args[2]=='Motion':
        if os.path.isdir('./Cabed_Motion') == False:#なければ保存用のディレクトリ作成
            os.mkdir('./Cabed_Motion')
        npyPath_list = glob.glob('../npyGen/NPY/Motion_Data/*')#'../npyGen/NPY/Motion_Data/Dentifrice.npy',...
        for npyPath in tqdm(npyPath_list):
            npySavePath = npyPath.replace('../npyGen/NPY/Motion_Data','./Cabed_Motion')#'./Cabed_Motion/Dentifrice.npy',...
            npySavePath = npySavePath.replace('.npy','')#'./NewCabed_Dent/Dentifrice'...
            if os.path.isdir(npySavePath) == False:#なければ保存用のディレクトリ作成
                os.mkdir(npySavePath)#'./NewCabed_Dent/Dentifrice/'...
            Motiondata = np.load(npyPath)
            CfC.Motion_cab(Motiondata,npySavePath)


    elif args[2]=='Person':
        if os.path.isdir('./Cabed_Person') == False:#なければ保存用のディレクトリ作成
            os.mkdir('./Cabed_Person')
        DirPath_list = glob.glob('../npyGen/NPY/Person/*')#'../npyGen/NPY/Person/jyu',...

        for DirPath in tqdm(DirPath_list):

                DirSavePath = DirPath.replace('../npyGen/NPY/','./Cabed_')#'./Cabed_Person/jyu'...
                if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
                    os.mkdir(DirSavePath)#'./Cabed_Person/jyu'...

                npyPath_list = glob.glob(DirPath+'/*.npy')#'../npyGen/NPY/Person/jyu/1.npy',...
                count = 1
                for npyPath in npyPath_list:
                    npySavePath = npyPath.replace('../npyGen/NPY/','./Cabed_')#'./Cabed_Person/jyu/1.npy'...
                    npySavePath = npySavePath.replace('.npy','')#'./Cabed_Person/jyu/1'...
                    if os.path.isdir(npySavePath) == False:#なければ保存用のディレクトリ作成
                        os.mkdir(npySavePath)#'./Cabed_Person/jyu/1'...
                    person = np.load(npyPath)
                    CfC.cabTest(person,args[1],str(count),DirSavePath)
                    count = count +1
