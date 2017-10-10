#!/usr/bin/env python
#-*- coding:utf-8 -*-
#平均、SD、SDのヒストグラムを画像として書き出す

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


class Ave_SD_Hist_FigClass:
    """平均、SD、SDのヒストグラムを画像として書き出す"""
    def ave_Gen(self,Motion):
        line,column,frame = Motion.shape
        ave_map = np.zeros([line,column])
        ave_mask = np.zeros([line,column])

        for lines in range(line):
            for columns in range(column):
                ave_map[lines,columns]=np.average(Motion[lines,columns,:])
                if ave_map[lines,columns] == 0:
                    ave_mask[lines,columns] = 1

        return ave_map,ave_mask


    def SD_Gen(self,Motion):
        line,column,frame = Motion.shape
        SD_map = np.zeros([line,column])
        SD_mask = np.zeros([line,column])

        for lines in range(line):
            for columns in range(column):
                SD_map[lines,columns]=np.std(Motion[lines,columns,:])
                if SD_map[lines,columns] == 0:
                    SD_mask[lines,columns] = 1

        return SD_map,SD_mask


    def plot_AveASD(self,Motion,mask,figSavePath,num):

        fig, ax = plt.subplots(figsize=(25, 20))
        sns.heatmap(Motion[:,:], mask=mask[:,:],vmin=0, cmap='viridis',linecolor='black',linewidths=0.1)
        ax.set_xticks(np.arange(Motion[:,:].shape[0]) + 0.5, minor=False)
        ax.set_yticks(np.arange(Motion[:,:].shape[1]) + 0.5, minor=False)
        ax.xaxis.tick_top()
        ax.set_xticklabels(np.arange(60), minor=False)
        ax.set_yticklabels(np.arange(60), minor=False)
        if num == 1:
            plt.savefig(figSavePath+"/Ave.png")
        else:
            plt.savefig(figSavePath+"/SD.png")
        plt.close()


    def plot_Hist(self,Motion,figSavePath):
        Motion = Motion.flatten()
        fig, ax = plt.subplots(figsize=(25, 20))
        # ax.set_xticks(np.arange(Motion[:,:].shape[0]) + 0.5, minor=False)
        # ax.set_yticks(np.arange(Motion[:,:].shape[1]) + 0.5, minor=False)
        # ax.xaxis.tick_top()
        # ax.set_xticklabels(np.arange(60), minor=False)
        # ax.set_yticklabels(np.arange(60), minor=False)
        plt.hist(Motion,label="hist")
        plt.title("Hist",fontsize=30)
        plt.xlabel("Output",fontsize=30)
        plt.ylabel("bins",fontsize=30)
        plt.grid(True)
        # plt.legend(fontsize=30)
        plt.tick_params(labelsize=30)
        plt.savefig(figSavePath+"/Hist.png")
        plt.close()


if __name__ == '__main__':
    ASHF = Ave_SD_Hist_FigClass()

    #Row_Motion
    # if os.path.isdir('./Row_Motion') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./Row_Motion')
    # npyPath_list = glob.glob('../npyGen/NPY/Motion_Data/*.npy')#'../npyGen/NPY/Motion_Data/Dentifrice.npy',...
    # for npyPath in tqdm(npyPath_list):#'../npyGen/NPY/Motion_Data/Dentifrice.npy',...
    #     MotionSavePath = npyPath.replace('../npyGen/NPY/Motion_Data/','./Row_Motion/')#'./Row_Motion/Dentifrice.npy'...
    #     MotionSavePath = MotionSavePath.replace('.npy','')#'./Row_Motion/Dentifrice'...
    #     if os.path.isdir(MotionSavePath) == False:#なければ保存用のディレクトリ作成
    #         os.mkdir(MotionSavePath)#'./Cabed_Motion/Dentifrice/'...
    #     Motiondata = np.load(npyPath)
    #     ave_map,ave_mask = ASHF.ave_Gen(Motiondata)
    #     SD_map,SD_mask   = ASHF.SD_Gen(Motiondata)
    #     ASHF.plot_AveASD(ave_map,ave_mask,MotionSavePath,1)
    #     ASHF.plot_AveASD(SD_map,SD_mask,MotionSavePath,2)
    #     ASHF.plot_Hist(SD_map,MotionSavePath)
    #
    #     np.save(MotionSavePath+"/ave_map.npy", ave_map)
    #     np.save(MotionSavePath+"/ave_mask.npy", ave_mask)
    #     np.save(MotionSavePath+"/SD_map.npy", SD_map)
    #     np.save(MotionSavePath+"/SD_mask.npy", SD_mask)


    #Cabed_Motion
    # MotionPath_list = glob.glob('./Cabed_Motion/*')#'./Cabed_Motion/Dentifrice'...
    # for MotionPath in MotionPath_list:#'./Cabed_Motion/Dentifrice'...
    #     npyPath_list = glob.glob(MotionPath+'/*.npy')#'Cabed_Motion/Dentifrice/cabed_all.npy'...
    #     for npyPath in npyPath_list:#'Cabed_Motion/Dentifrice/cabed_all.npy'...
    #         figSavePath = npyPath.replace('cabed_','')#'Cabed_Motion/Dentifrice/all.npy'...
    #         figSavePath = figSavePath.replace('.npy','')#'Cabed_Motion/Dentifrice/all'...
    #         if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
    #             os.mkdir(figSavePath)#'Cabed_Motion/Dentifrice/all'...
    #
    #         Motiondata = np.load(npyPath)
    #         ave_map,ave_mask = ASHF.ave_Gen(Motiondata)
    #         SD_map,SD_mask   = ASHF.SD_Gen(Motiondata)
    #         ASHF.plot_AveASD(ave_map,ave_mask,figSavePath,1)
    #         ASHF.plot_AveASD(SD_map,SD_mask,figSavePath,2)
    #         ASHF.plot_Hist(SD_map,figSavePath)
    #
    #         np.save(figSavePath+"/ave_map.npy", ave_map)
    #         np.save(figSavePath+"/ave_mask.npy", ave_mask)
    #         np.save(figSavePath+"/SD_map.npy", SD_map)
    #         np.save(figSavePath+"/SD_mask.npy", SD_mask)



    #Cabed_Motion//Dentifrice/ED44
    MotionPath_list = glob.glob('./Cabed_Motion/*')#'./Cabed_Motion/Dentifrice'...
    for MotionPath in tqdm(MotionPath_list):#'./Cabed_Motion/Dentifrice'...
        EDPath_list = glob.glob(MotionPath+'/ED*')#'Cabed_Motion/Dentifrice/ED44'...
        for EDPath in EDPath_list:#'Cabed_Motion/Dentifrice/ED44'...
            npyPath_list = glob.glob(EDPath+'/*.npy')#'Cabed_Motion/Dentifrice/ED44/cabed_all.npy'...
            for npyPath in npyPath_list:
                figSavePath = npyPath.replace('cabed_','')#'Cabed_Motion/Dentifrice/ED44/all.npy'...
                figSavePath = figSavePath.replace('.npy','')#'Cabed_Motion/Dentifrice/ED44/all'...
                if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
                    os.mkdir(figSavePath)#'Cabed_Motion/Dentifrice/ED44/all'...

                Motiondata = np.load(npyPath)
                ave_map,ave_mask = ASHF.ave_Gen(Motiondata)
                SD_map,SD_mask   = ASHF.SD_Gen(Motiondata)
                ASHF.plot_AveASD(ave_map,ave_mask,figSavePath,1)
                ASHF.plot_AveASD(SD_map,SD_mask,figSavePath,2)
                ASHF.plot_Hist(SD_map,figSavePath)

                np.save(figSavePath+"/ave_map.npy", ave_map)
                np.save(figSavePath+"/ave_mask.npy", ave_mask)
                np.save(figSavePath+"/SD_map.npy", SD_map)
                np.save(figSavePath+"/SD_mask.npy", SD_mask)
