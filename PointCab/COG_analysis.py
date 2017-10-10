#!/usr/bin/env python
#-*- coding:utf-8 -*-
#ŽžŒn—ñ“I‚É‚»‚ê‚¼‚ê‚ÌŽ²‚ª‚Ç‚¤‘JˆÚ‚µ‚½‚©Šm”F‚·‚é‚½‚ß‚Ì‰æ‘œ‚ðo—Í‚·‚é

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

    """ŽžŒn—ñ“I‚É‚»‚ê‚¼‚ê‚ÌŽ²‚ª‚Ç‚¤‘JˆÚ‚µ‚½‚©Šm”F‚·‚é‚½‚ß‚Ì‰æ‘œ‚ðo—Í‚·‚é"""

    def plot_COG_analysis(self,COGdata,figSavePath):

         frame,count = COGdata.shape

         for counts in range(count):
            if counts == 0:
               axes = 'X'
            #    print axes+str(COGdata[100,counts])
            elif counts == 1:
               axes = 'Y'
            #    print axes+str(COGdata[100,counts])
            elif counts == 3:
               axes = 'LX'
            #    print axes+str(COGdata[100,counts])
            #    print Y
            elif counts == 4:
               axes = 'LY'
            #    print axes+str(COGdata[100,counts])
            elif counts == 6:
               axes = 'RX'
            #    print axes+str(COGdata[100,counts])
            elif counts == 7:
               axes = 'RY'
            #    print axes+str(COGdata[100,counts])

            if counts ==2 or counts ==5 or counts ==8:
                pass
            elif counts ==1 or counts ==4 or counts ==7:
                Y = [item for item in COGdata[:,counts] if item]
                frame = len(Y)
                X=np.array(range(frame))

                fig, ax = plt.subplots(figsize=(25, 20))

                plt.plot(X, Y, linewidth=4, color="red", label="COG")
                # plt.plot(X, COGdata[counts], linewidth=4, color="red")

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

                if 'all' in npyPath:
                    plt.savefig(figSavePath+"/all_"+axes+".png")
                elif 'rep' in npyPath:
                    plt.savefig(figSavePath+"/rep_"+axes+".png")

                plt.close()


            else:
                Y = [item for item in COGdata[:,counts] if item]
                frame = len(Y)
                X=np.array(range(frame))

                fig, ax = plt.subplots(figsize=(25, 20))

                plt.plot(X, Y, linewidth=4, color="red", label="COG")
                # plt.plot(X, COGdata[counts], linewidth=4, color="red")

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

                if 'all' in npyPath:
                    plt.savefig(figSavePath+"/all_"+axes+".png")
                elif 'rep' in npyPath:
                    plt.savefig(figSavePath+"/rep_"+axes+".png")

                plt.close()

if __name__ == '__main__':
    COGana= COG_analysisClass()

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

    DirPath_list = glob.glob('./ED*Cabed_COG')#'ED44Cabed_COG/'...


    for DirPath in DirPath_list:#'ED44Cabed_COG/'...

        NamePath_list = glob.glob(DirPath+'/*')#'ED44Cabed_COG/jyu'...
        for NamePath in NamePath_list:#'ED44Cabed_COG/jyu'...

            npyPath_list = glob.glob(NamePath+'/*.npy')#'ED44Cabed_COG/jyu/cabed_all_1_ED_COG.npy'...
            for npyPath in npyPath_list:#'ED44Cabed_COG/1956_cabed_all_ED_COG.npy'...

                figSavePath = npyPath.replace('cabed_all_','')#'ED44Cabed_COG/jyu/1_ED_COG.npy'...
                figSavePath = figSavePath.replace('cabed_rep_','')#'ED44Cabed_COG/jyu/1_ED_COG.npy'...
                figSavePath = figSavePath.replace('_ED_COG.npy','')#'ED44Cabed_COG/jyu/1'...

                COGdata = np.load(npyPath)
                print COGdata.shape
                COGana.plot_COG_analysis(COGdata,figSavePath)
