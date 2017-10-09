#!/usr/bin/env python
# coding: utf-8
import glob
import os, commands
import os.path
from tqdm import tqdm
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys
import seaborn as sns
import cv2
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")
args = sys.argv

class COD_SD_testClass:

    """補正後の個人データを画像出力"""

#元のデータそのもののマスクを返す
    def SD_test(self,data):

        SD_COG_npy = np.zeros([6])

        SD_COG_npy[0]= np.std(data[:,0])
        SD_COG_npy[1]= np.std(data[:,1])

        SD_COG_npy[2] = np.std(data[:,3])
        SD_COG_npy[3] = np.std(data[:,4])

        SD_COG_npy[4] = np.std(data[:,6])
        SD_COG_npy[5] = np.std(data[:,7])


        return SD_COG_npy

if __name__ == '__main__':
    CSt = COD_SD_testClass()
    NamePath_list = glob.glob('./NewCabed_COG/*')#'./NewCabed_COD/jyu',...
    for NamePath in tqdm(NamePath_list):
        npyPath_list = glob.glob(NamePath+'/*.npy')#'./NewCabed_COD/jyu/cabed_all_1_COG.npy',...
        for npyPath in tqdm(npyPath_list):


            figSavePath = npyPath.replace('cabed_all_','')
            figSavePath = figSavePath.replace('cabed_rep_','')
            figSavePath = figSavePath.replace('_COG.npy','')#'./NewCabed_Person/jyu/1',...
            if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
                os.mkdir(figSavePath)#'./NewCabed_Person/jyu/1'...

            all_figSavePath = figSavePath+'/all/'#'./NewCabed_Person/jyu/1/all/',...
            rep_figSavePath = figSavePath+'/rep/'#'./NewCabed_Person/jyu/1/rep/',...
            if os.path.isdir(all_figSavePath) == False:#なければ保存用のディレクトリ作成
                os.mkdir(all_figSavePath)#'./NewCabed_Person/jyu/1/all/'...
            if os.path.isdir(rep_figSavePath) == False:#なければ保存用のディレクトリ作成
                os.mkdir(rep_figSavePath)#'./NewCabed_Person/jyu/1/rep/'...

            COGdata = np.load(npyPath)
            # print COGdata.shape
                #(10,9)
            SD_COG_npy = CSt.SD_test(COGdata)

            if 'all' in npyPath:
                file_out = open(all_figSavePath+'SD_COD.txt',"w")
                # file_out.write(str(COGdata)+'\n')
                # file_out.write(str(xg)+','+str(yg)+','+str(Lxg)+','+str(Lyg)+','+str(Rxg)+','+str(Ryg)+'\n')
                # file_out.close()
                np.save(all_figSavePath+"SD_COG.npy", SD_COG_npy)
            elif 'rep' in npyPath:
                # file_out = open(rep_figSavePath+'SD_COD.txt',"w")
                # file_out.write(str(xg)+','+str(yg)+','+str(Lxg)+','+str(Lyg)+','+str(Rxg)+','+str(Ryg)+'\n')
                # file_out.close()
                np.save(rep_figSavePath+"SD_COG.npy", SD_COG_npy)



    DirPath_list = glob.glob('./ED*_COG')

    for DirPath in tqdm(DirPath_list):
            NamePath_list = glob.glob(DirPath+'/*')#'./Cabed_Person/jyu'...

            for NamePath in NamePath_list:
                npyPath_list = glob.glob(NamePath+'/*.npy')#'./Cabed_Person/jyu/1.npy'...

                for npyPath in npyPath_list:
                    figSavePath = npyPath.replace('cabed_all_','')
                    figSavePath = figSavePath.replace('cabed_rep_','')
                    figSavePath = figSavePath.replace('_ED_COG.npy','')#'./NewCabed_Person/jyu/1',...
                    if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
                        os.mkdir(figSavePath)#'./NewCabed_Person/jyu/1'...

                    all_figSavePath = figSavePath+'/all/'#'./NewCabed_Person/jyu/1/all/',...
                    rep_figSavePath = figSavePath+'/rep/'#'./NewCabed_Person/jyu/1/rep/',...
                    if os.path.isdir(all_figSavePath) == False:#なければ保存用のディレクトリ作成
                        os.mkdir(all_figSavePath)#'./NewCabed_Person/jyu/1/all/'...
                    if os.path.isdir(rep_figSavePath) == False:#なければ保存用のディレクトリ作成
                        os.mkdir(rep_figSavePath)#'./NewCabed_Person/jyu/1/rep/'...

                    COGdata = np.load(npyPath)
                    SD_COG_npy = CSt.SD_test(COGdata)
                    if 'all' in npyPath:
                        file_out = open(all_figSavePath+'SD_COD.txt',"w")
                        file_out.write(str(COGdata)+'\n')
                        file_out.write(str(SD_COG_npy[0])+','+str(SD_COG_npy[1])+','+str(SD_COG_npy[2])+','+str(SD_COG_npy[3])+','+str(SD_COG_npy[4])+','+str(SD_COG_npy[5])+'\n')
                        file_out.close()
                        np.save(all_figSavePath+"SD_COG.npy", SD_COG_npy)
                    elif 'rep' in npyPath:
                        file_out = open(rep_figSavePath+'SD_COD.txt',"w")
                        file_out.write(str(COGdata)+'\n')
                        file_out.write(str(SD_COG_npy[0])+','+str(SD_COG_npy[1])+','+str(SD_COG_npy[2])+','+str(SD_COG_npy[3])+','+str(SD_COG_npy[4])+','+str(SD_COG_npy[5])+'\n')
                        file_out.close()
                        np.save(rep_figSavePath+"SD_COG.npy", SD_COG_npy)
