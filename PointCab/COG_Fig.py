#!/usr/bin/env python
#-*- coding:utf-8 -*-

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


class COG_FigClass:

    """補正後の個人データを画像出力"""

#元のデータそのもののマスクを返す
    def plot_COG(self,person,COGdata,mask,figSavePath):
        line,clumn,count = person.shape
        for counts in tqdm(range(count)):


            fig, ax = plt.subplots(figsize=(25, 20))
            sns.heatmap(person[:,:,counts], mask=mask[:,:,counts],vmin=0, cmap='viridis',linecolor='black',linewidths=0.1)
            # ax.set_xticks(np.arange(person[:,:,0].shape[0]) + 0.5, minor=False)
            # ax.set_yticks(np.arange(person[:,:,0].shape[1]) + 0.5, minor=False)
            # ax.xaxis.tick_top()
            # ax.set_xticklabels(np.arange(60), minor=False)
            # ax.set_yticklabels(np.arange(60), minor=False)
            plt.scatter(COGdata[counts,1],COGdata[counts,0], s=2500,c="yellow", marker="*",linewidths="2",edgecolors="orange")
            plt.scatter(COGdata[counts,4],COGdata[counts,3], s=2500,c="red", marker="*",linewidths="2",edgecolors="orange")
            plt.scatter(COGdata[counts,7],COGdata[counts,6], s=2500,c="green", marker="*",linewidths="2",edgecolors="orange")
            plt.savefig(figSavePath+"/"+str(counts)+".png")
            plt.close()

if __name__ == '__main__':
    COGFCla= COG_FigClass()

    # DirPath_list = glob.glob('./ED*_Person')
    #
    # for DirPath in tqdm(DirPath_list):
    #
    #         NamePath_list = glob.glob(DirPath+'/*')#'ED44Cabed_Person/jyu'...
    #
    #         for NamePath in NamePath_list:
    #
    #             npyPath_list = glob.glob(NamePath+'/*.npy')
    #
    #             for npyPath in npyPath_list:#'ED44Cabed_Person/jyu/cabed_all_1_ED.npy'...
    #                 figSavePath = npyPath.replace('Person','COG')#'ED44Cabed_COG/jyu/cabed_all_1_ED.npy'...
    #                 COGPath = figSavePath.replace('_ED.npy','_ED_COG.npy')#'ED44Cabed_COG/jyu/cabed_all_1_ED_COG.npy',...
    #                 figSavePath = figSavePath.replace('cabed_all_','')#'ED44Cabed_COG/jyu/1_ED.npy'...
    #                 figSavePath = figSavePath.replace('cabed_rep_','')#'ED44Cabed_COG/jyu/1_ED.npy'...
    #                 figSavePath = figSavePath.replace('_ED.npy','')#'ED44Cabed_COG/jyu/1',...
    #                 all_figSavePath = figSavePath+'/all/'#'./NewCabed_Person/jyu/1/all/',...
    #                 rep_figSavePath = figSavePath+'/rep/'#'./NewCabed_Person/jyu/1/rep/',...
    #
    #                 person = np.load(npyPath)
    #                 COGdata = np.load(COGPath)
    #
    #                 if 'all' in npyPath:
    #                     COGFCla.plot_COG(person,COGdata,all_figSavePath)
    #                 elif 'rep' in npyPath:
    #                     COGFCla.plot_COG(person,COGdata,rep_figSavePath)

    # DirPath_list = glob.glob('./ED*_Dent')
    #
    # for DirPath in tqdm(DirPath_list):
    #
    #     npyPath_list = glob.glob(DirPath+'/*.npy')#'ED44Cabed_Dent/1956_cabed_all_ED.py'...
    #
    #     for npyPath in npyPath_list:#'ED44Cabed_Dent/jyu/cabed_all_1_ED.npy'...
    #         figSavePath = npyPath.replace('Dent','Dent_COG')#'ED44Cabed_Dent_COG/1956_cabed_all_ED.py'...
    #         COGPath = figSavePath.replace('_ED.npy','_ED_COG.npy')#'ED44Cabed_COG/1956_cabed_all_ED_COG.py'...
    #         figSavePath = figSavePath.replace('cabed_all_','')#'ED44Cabed_COG/1956_ED.py'...
    #         figSavePath = figSavePath.replace('cabed_rep_','')#'ED44Cabed_COG/1956_ED.py'...
    #         figSavePath = figSavePath.replace('1956_ED.npy','')#'ED44Cabed_COG/1956',...
    #         if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
    #             os.mkdir(figSavePath)#'./NewCabed_Dent/1964/all/'...
    #         all_figSavePath = figSavePath+'all/'#'./NewCabed_Dent/1956/all/',...
    #         rep_figSavePath = figSavePath+'rep/'#'./NewCabed_Dent/1956/rep/',...
    #         if os.path.isdir(all_figSavePath) == False:#なければ保存用のディレクトリ作成
    #             os.mkdir(all_figSavePath)#'./NewCabed_Dent/1964/all/'...
    #         if os.path.isdir(rep_figSavePath) == False:#なければ保存用のディレクトリ作成
    #             os.mkdir(rep_figSavePath)#'./NewCabed_Dent/1964/rep/'...
    #
    #         Dentdata = np.load(npyPath)
    #         COGdata = np.load(COGPath)
    #
    #
    #         if 'all' in npyPath:
    #             maskPath = all_figSavePath.replace('Dent_COG','Dent')#'ED44Cabed_Dent_COG/1956_cabed_all_ED.py'...
    #             mask = np.load(maskPath+'mask.npy')
    #             COGFCla.plot_COG(Dentdata,COGdata,mask,all_figSavePath)
    #         elif 'rep' in npyPath:
    #             maskPath = rep_figSavePath.replace('Dent_COG','Dent')#'ED44Cabed_Dent_COG/1956_cabed_all_ED.py'...
    #             mask = np.load(maskPath+'mask.npy')
    #             COGFCla.plot_COG(Dentdata,COGdata,mask,rep_figSavePath)

    # npyPath_list = glob.glob('../npyGen/NPY/Dentifrice_Cleaned/*.npy')#'../npyGen/NPY/Dentifrice_Cleaned/1964.npy',...
    #
    # for npyPath in npyPath_list:#'../npyGen/NPY/Dentifrice_Cleaned/1964.npy',...
    #     figSavePath = npyPath.replace('../npyGen/NPY/Dentifrice_Cleaned','./Row_Dent')#'./Row_Dent/1956.py',...
    #     COGPath = figSavePath.replace('./Row_Dent','./Row_Dent_COG')#'./Row_Dent_COG/1956.py'...
    #     COGPath = COGPath.replace('.npy','_COG.npy')#'./Row_Dent_Raw/1956_COG.py'...
    #     figSavePath = figSavePath.replace('1956.npy','')#'./Row_Dent/',...
    #
    #     Dentdata = np.load(npyPath)
    #     COGdata = np.load(COGPath)
    #     mask = np.load(figSavePath+'mask.npy')
    #     COGFCla.plot_COG(Dentdata,COGdata,mask,figSavePath)
