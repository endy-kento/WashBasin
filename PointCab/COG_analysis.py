#!/usr/bin/env python
#-*- coding:utf-8 -*-
#時系列的にそれぞれの軸がどう遷移したか確認するための画像を出力する
#iirでのローパスフィルタを通した波形も生成可能

from IIRFilter import IIRFilter
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


class COG_analysisClass:

    """時系列的にそれぞれの軸がどう遷移したか確認するための画像を出力する"""
    def normalize(self,data,inmin=0,inmax=60,outmin=-1,outmax=1):
        for i in range(len(data)):
            data[i] =  (data[i] - inmin)*(outmax-outmin)/(inmax-inmin)+(outmin)
        return (data)

    def ommit(self,data,ommit_value):
        data_list = []
        for d in data:
            if d != ommit_value:
                data_list.append(d)
        return data_list

    def plot_COG_analysis(self,COGdata,figSavePath):

         frame,count = COGdata.shape

         for i in range(count):
            if i == 0:
               axes = 'X'
            elif i == 1:
               axes = 'Y'
            elif i == 2:
               axes = 'Z'
            elif i == 3:
               axes = 'LX'
            elif i == 4:
               axes = 'LY'
            elif i == 5:
               axes = 'LZ'
            elif i == 6:
               axes = 'RX'
            elif i == 7:
               axes = 'RY'
            elif i == 8:
               axes = 'RZ'

            Sample    = self.normalize( self.ommit( COGdata.T[i] , 0 ) )
            fs = 37
            iir = IIRFilter()
            iir.lpf(10,fs)#10以上をカット
            Sample = iir.iir(Sample)


            if i ==2 or i ==5 or i ==8:

                Y = [item for item in Sample[:] if item]
                frame = len(Y)
                X=np.array(range(frame))

                fig, ax = plt.subplots(figsize=(25, 20))

                plt.plot(X, Y, linewidth=4, color="red", label="COG")
                # plt.plot(X, Sample[i], linewidth=4, color="red")

                plt.title("COG_analysis",fontsize=30)
                plt.xlabel("Frame",fontsize=30)
                plt.ylabel(axes+"'s COG",fontsize=30)
                plt.grid(True)
                # plt.legend(fontsize=30)
                plt.tick_params(labelsize=30)

                # if min(Y) > 29:
                #     plt.fill_between(X,min(Y),max(Y),facecolor='b',alpha=0.3,label='bottom')
                # elif max(Y) < 29:
                #     plt.fill_between(X,min(Y),max(Y),facecolor='g',alpha=0.3,label='top')
                # else:
                #     plt.fill_between(X,29,max(Y),facecolor='b',alpha=0.3,label='bottom')
                #     plt.fill_between(X,min(Y),29,facecolor='g',alpha=0.3,label='top')
                plt.legend(fontsize=30)


                plt.savefig(figSavePath+"/Ana_10lpf_"+axes+".png")


                plt.close()
            elif i ==1 or i ==4 or i ==7:
                Y = [item for item in Sample[:] if item]
                frame = len(Y)
                X=np.array(range(frame))

                fig, ax = plt.subplots(figsize=(25, 20))

                plt.plot(X, Y, linewidth=4, color="red", label="COG")
                # plt.plot(X, Sample[i], linewidth=4, color="red")

                plt.title("COG_analysis",fontsize=30)
                plt.xlabel("Frame",fontsize=30)
                plt.ylabel(axes+"'s COG",fontsize=30)
                plt.grid(True)
                # plt.legend(fontsize=30)
                plt.tick_params(labelsize=30)

                if min(Y) > 29:
                    plt.fill_between(X,min(Y),max(Y),facecolor='b',alpha=0.3,label='bottom')
                elif max(Y) < 29:
                    plt.fill_between(X,min(Y),max(Y),facecolor='g',alpha=0.3,label='top')
                else:
                    plt.fill_between(X,29,max(Y),facecolor='b',alpha=0.3,label='bottom')
                    plt.fill_between(X,min(Y),29,facecolor='g',alpha=0.3,label='top')
                plt.legend(fontsize=30)


                plt.savefig(figSavePath+"/Ana_10lpf_"+axes+".png")


                plt.close()


            else:
                Y = [item for item in Sample[:] if item]
                frame = len(Y)
                X=np.array(range(frame))

                fig, ax = plt.subplots(figsize=(25, 20))

                plt.plot(X, Y, linewidth=4, color="red", label="COG")
                # plt.plot(X, Sample[i], linewidth=4, color="red")

                plt.title("COG_analysis",fontsize=30)
                plt.xlabel("Frame",fontsize=30)
                plt.ylabel(axes+"'s COG",fontsize=30)
                plt.grid(True)
                # plt.legend(fontsize=30)
                plt.tick_params(labelsize=30)

                if min(Y) > 29:
                    plt.fill_between(X,min(Y),max(Y),facecolor='b',alpha=0.3,label='right')
                elif max(Y) < 29:
                    plt.fill_between(X,min(Y),max(Y),facecolor='g',alpha=0.3,label='left')
                else:
                    plt.fill_between(X,29,max(Y),facecolor='b',alpha=0.3,label='right')
                    plt.fill_between(X,min(Y),29,facecolor='g',alpha=0.3,label='left')
                plt.legend(fontsize=30)

                plt.savefig(figSavePath+"/Ana_10lpf_"+axes+".png")

                plt.close()

if __name__ == '__main__':
    COGana= COG_analysisClass()

    # #Row_Motion
    # npyPath_list = glob.glob('./Row_Motion_COG/*.npy')#'./Row_Motion_COG/Dentifrice.npy',...
    # for npyPath in tqdm(npyPath_list):#'./Row_Motion_COG/Dentifrice.npy',...
    #     figSavePath = npyPath.replace('_COG.npy','')#'Row_Motion_COG/Dentifrice'...
    #     if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
    #             os.mkdir(figSavePath)#'./Row_Motion_COG/Dentifrice'...
    #     COGdata = np.load(npyPath)
    #     COGana.plot_COG_analysis(COGdata,figSavePath)
    #
    #
    #
    # # Cabed_Motion
    # MotionPath_list = glob.glob('./Cabed_Motion_COG/*/')#'./Cabed_Motion_COG/Dentifrice'...
    # for MotionPath in tqdm(MotionPath_list):#'./Cabed_Motion_COG/Dentifrice'...
    #     npyPath_list = glob.glob(MotionPath+'/*.npy')#'Cabed_Motion_COG/Dentifrice/cabed_all_COG.npy'...
    #     for npyPath in npyPath_list:#'Cabed_Motion_COG/Dentifrice/cabed_all_COG.npy'...
    #         figSavePath = npyPath.replace('cabed_','')#'Cabed_Motion_COG/Dentifrice/all_COG.npy'...
    #         figSavePath = figSavePath.replace('_COG.npy','')#'Cabed_Motion/Dentifrice/all'...
    #         if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
    #                 os.mkdir(figSavePath)#'./Row_Motion_COG/Dentifrice/Heatmap'...
    #         COGdata = np.load(npyPath)
    #         COGana.plot_COG_analysis(COGdata,figSavePath)


    #Cabed_Motion//Dentifrice/ED44
    MotionPath_list = glob.glob('./Cabed_Motion_COG/*/')#'./Cabed_Motion_COG/Dentifrice'...
    for MotionPath in tqdm(MotionPath_list):#'./Cabed_Motion_COG/Dentifrice'...
        EDPath_list = glob.glob(MotionPath+'/ED*')#'Cabed_Motion_COG/Dentifrice/ED44'...
        for EDPath in EDPath_list:#'Cabed_Motion_COG/Dentifrice/ED44'...
            npyPath_list = glob.glob(EDPath+'/*.npy')#'Cabed_Motion_COG/Dentifrice/ED44/cabed_all_COG.npy'...
            for npyPath in npyPath_list:
                figSavePath = npyPath.replace('cabed_','')#'Cabed_Motion_COG/Dentifrice/ED44/all_COG.npy'...
                figSavePath = figSavePath.replace('_COG.npy','')#'Cabed_Motion/Dentifrice/ED44/all'...
                if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
                        os.mkdir(figSavePath)#'./Row_Motion_COG/Dentifrice/ED44/Heatmap'...
                COGdata = np.load(npyPath)
                COGana.plot_COG_analysis(COGdata,figSavePath)




    # DirPath_list = glob.glob('./ED*Cabed_Dent_COG')#'ED44Cabed_Dent/'...
    #
    # for DirPath in DirPath_list:
    #
    #     npyPath_list = glob.glob(DirPath+'/*.npy')#'ED44Cabed_Dent/1956_cabed_all_ED_COG.npy'...
    #
    #     for npyPath in npyPath_list:#'ED44Cabed_Dent/1956_cabed_all_ED_COG.npy'...
    #
    #         COGdata = np.load(npyPath)
    #         COGana.plot_COG_analysis(COGdata,DirPath)

    # DirPath_list = glob.glob('./ED*Cabed_COG')#'ED44Cabed_COG/'...
    #
    #
    # for DirPath in DirPath_list:#'ED44Cabed_COG/'...
    #
    #     NamePath_list = glob.glob(DirPath+'/*')#'ED44Cabed_COG/jyu'...
    #     for NamePath in NamePath_list:#'ED44Cabed_COG/jyu'...
    #
    #         npyPath_list = glob.glob(NamePath+'/*.npy')#'ED44Cabed_COG/jyu/cabed_all_1_ED_COG.npy'...
    #         for npyPath in npyPath_list:#'ED44Cabed_COG/1956_cabed_all_ED_COG.npy'...
    #
    #             figSavePath = npyPath.replace('cabed_all_','')#'ED44Cabed_COG/jyu/1_ED_COG.npy'...
    #             figSavePath = figSavePath.replace('cabed_rep_','')#'ED44Cabed_COG/jyu/1_ED_COG.npy'...
    #             figSavePath = figSavePath.replace('_ED_COG.npy','')#'ED44Cabed_COG/jyu/1'...
    #
    #             COGdata = np.load(npyPath)
    #             print COGdata.shape
    #             COGana.plot_COG_analysis(COGdata,figSavePath)
