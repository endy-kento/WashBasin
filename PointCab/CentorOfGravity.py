#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
import glob
import os, commands
import os.path
from tqdm import tqdm
import sys
import glob
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")
args = sys.argv

class CentorOfGravityClass:

    """フレーム毎の全体、各足の重心を求める"""

    # def __init__(self):

    def centorofgravity(self,data):
        #対象のファイルと整形後のファイルを開く
        line,clumn,count = data.shape
        COG = np.zeros([count,9])#集約後の行列の初期化(平均)
        # print data.shape
        row, col, count = data.shape
        for counts in tqdm(range(count)):

            for rows in range(row):
                for cols in range(col):

                    COG[counts,0] = COG[counts,0] + rows*float(data[rows][cols][counts])
                    COG[counts,1] = COG[counts,1] + cols*float(data[rows][cols][counts])
                    COG[counts,2] = COG[counts,2] + float(data[rows][cols][counts])

                    if  col/2 >= cols:
                        COG[counts,3] = COG[counts,3] + rows*float(data[rows][cols][counts])
                        COG[counts,4] = COG[counts,4] + cols*float(data[rows][cols][counts])
                        COG[counts,5] = COG[counts,5] + float(data[rows][cols][counts])
                    else:
                        COG[counts,6] = COG[counts,6] + rows*float(data[rows][cols][counts])
                        COG[counts,7] = COG[counts,7] + cols*float(data[rows][cols][counts])
                        COG[counts,8] = COG[counts,8] + float(data[rows][cols][counts])

            if COG[counts,0] or COG[counts,1] or COG[counts,2] != 0:
                COG[counts,0]=COG[counts,0]/row*row/COG[counts,2]
                COG[counts,1]=COG[counts,1]/row*row/COG[counts,2]
            else:
                COG[counts,0]=0
                COG[counts,1]=0

            if COG[counts,3] or COG[counts,4] or COG[counts,5] != 0:
                COG[counts,3]=COG[counts,3]/row*row/COG[counts,5]
                COG[counts,4]=COG[counts,4]/row*row/COG[counts,5]
            else:
                COG[counts,3]=0
                COG[counts,4]=0

            if COG[counts,6] or COG[counts,7] or COG[counts,8] != 0:
                COG[counts,6]=COG[counts,6]/row*row/COG[counts,8]
                COG[counts,7]=COG[counts,7]/row*row/COG[counts,8]
            else:
                COG[counts,6]=0
                COG[counts,7]=0

        return COG

#集約後のデータの重心を求める
if __name__ == '__main__':
    COGCla= CentorOfGravityClass()

    # #Row_Motion
    # if os.path.isdir('./Row_Motion_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./Row_Motion_COG')
    # npyPath_list = glob.glob('../npyGen/NPY/Motion_Data/*.npy')#'../npyGen/NPY/Motion_Data/Dentifrice.npy',...
    # for npyPath in npyPath_list:#'../npyGen/NPY/Motion_Data/Dentifrice.npy',...
    #     MotionSavePath = npyPath.replace('../npyGen/NPY/Motion_Data/','./Row_Motion_COG/')#'./Row_Motion_COG/Dentifrice.npy'...
    #     MotionSavePath = MotionSavePath.replace('.npy','')#'./Row_Motion_COG/Dentifrice'...
    #     Motiondata = np.load(npyPath)
    #     COGdata = COGCla.centorofgravity(Motiondata)
    #     np.save(MotionSavePath+"_COG.npy", COGdata)
    #
    #
    # #Cabed_Motion
    # if os.path.isdir('./Cabed_Motion_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./Cabed_Motion_COG')
    # MotionPath_list = glob.glob('./Cabed_Motion/*/')#'./Cabed_Motion/Dentifrice'...
    # for MotionPath in MotionPath_list:#'./Cabed_Motion/Dentifrice'...
    #     MotionSavePath = MotionPath.replace('Motion/','Motion_COG/')#'./Cabed_Motion_COG/Dentifrice'...
    #     if os.path.isdir(MotionSavePath) == False:#なければ保存用のディレクトリ作成
    #         os.mkdir(MotionSavePath)#'./Cabed_Motion_COG/Dentifrice/'...
    #     npyPath_list = glob.glob(MotionPath+'/*.npy')#'Cabed_Motion/Dentifrice/cabed_all.npy'...
    #     for npyPath in npyPath_list:#'Cabed_Motion/Dentifrice/cabed_all.npy'...
    #         Motiondata = np.load(npyPath)
    #         COGdata = COGCla.centorofgravity(Motiondata)
    #         if 'all' in npyPath:
    #             np.save(MotionSavePath+"/cabed_all_COG.npy", COGdata)
    #         elif 'rep' in npyPath:
    #             np.save(MotionSavePath+"/cabed_rep_COG.npy", COGdata)


    #Cabed_Motion//Dentifrice/ED44
    MotionPath_list = glob.glob('./Cabed_Motion/*')#'./Cabed_Motion/Dentifrice'...
    for MotionPath in MotionPath_list:#'./Cabed_Motion/Dentifrice'...
        EDPath_list = glob.glob(MotionPath+'/*/')#'Cabed_Motion/Dentifrice/ED44'...
        for EDPath in EDPath_list:#'Cabed_Motion/Dentifrice/cabed_all.npy'...
            EDSavePath = EDPath.replace('Cabed_Motion/','Cabed_Motion_COG/')#'Cabed_Motion/Dentifrice/ED44'...
            if os.path.isdir(EDSavePath) == False:#なければ保存用のディレクトリ作成
                os.mkdir(EDSavePath)#'./Cabed_Motion_COG/Dentifrice/'...
            npyPath_list = glob.glob(EDPath+'/*.npy')#'Cabed_Motion/Dentifrice/cabed_all.npy'...
            for npyPath in npyPath_list:
                Motiondata = np.load(npyPath)
                COGdata = COGCla.centorofgravity(Motiondata)
                if 'all' in npyPath:
                    np.save(EDSavePath+"/cabed_all_COG.npy", COGdata)
                elif 'rep' in npyPath:
                    np.save(EDSavePath+"/cabed_rep_COG.npy", COGdata)



    # if os.path.isdir('./NewCabed_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./NewCabed_COG/')
    # DirPath_list = glob.glob('./NewCabed_Person/*')#'../npyGen/NPY/Person/jyu',...
    #
    # for DirPath in DirPath_list:
    #
    #         DirSavePath = DirPath.replace('Person','COG')#'./Cabed_Person/jyu'...
    #         if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
    #             os.mkdir(DirSavePath)
    #
    #         npyPath_list = glob.glob(DirPath+'/*.npy')#'../npyGen/NPY/Person/jyu/1.npy',...
    #         count = 1
    #         for npyPath in npyPath_list:
    #             npySavePath = npyPath.replace('Person','COG')#'./Cabed_Person/jyu/1.npy'...
    #             npySavePath = npySavePath.replace('.npy','')#'./Cabed_Person/jyu/1'...
    #             person = np.load(npyPath)
    #             output_cabed_COG = COGCla.centorofgravity(person,npySavePath+".npy")
    #             np.save(npySavePath+"_COG.npy", output_cabed_COG)
    #
    #             count = count +1

    # if os.path.isdir('./ED44Cabed_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./ED44Cabed_COG')
    # if os.path.isdir('./ED48Cabed_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./ED48Cabed_COG')
    # if os.path.isdir('./ED84Cabed_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./ED84Cabed_COG')
    # if os.path.isdir('./ED88Cabed_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./ED88Cabed_COG')
    #
    # DirPath_list = glob.glob('./ED*_Person')
    #
    # for DirPath in tqdm(DirPath_list):
    #
    #         DirSavePath = DirPath.replace('Person','COG')#'./ED44Cabed_COG'...
    #         NamePath_list = glob.glob(DirPath+'/*')
    #
    #         for NamePath in NamePath_list:
    #             NameSavePath = NamePath.replace('Person','COG')#'./Cabed_Person/jyu'...
    #             if os.path.isdir(NameSavePath) == False:#なければ保存用のディレクトリ作成
    #                 os.mkdir(NameSavePath)
    #             npyPath_list = glob.glob(NamePath+'/*.npy')
    #             count = 1
    #             for npyPath in npyPath_list:
    #                 numSavePath = npyPath.replace('Person','COG')#'./Cabed_Person/jyu/1.npy'...
    #                 npySavePath = numSavePath.replace('.npy','')#'./Cabed_Person/jyu/1.npy'...
    #
    #                 person = np.load(npyPath)
    #                 output_cabed_COG = COGCla.centorofgravity(person,npySavePath)
    #                 np.save(npySavePath+"_COG.npy", output_cabed_COG)
    #
    #                 count = count +1

    # if os.path.isdir('./ED44Cabed_Dent_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./ED44Cabed_Dent_COG')
    # if os.path.isdir('./ED48Cabed_Dent_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./ED48Cabed_Dent_COG')
    # if os.path.isdir('./ED84Cabed_Dent_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./ED84Cabed_Dent_COG')
    # if os.path.isdir('./ED88Cabed_Dent_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./ED88Cabed_Dent_COG')
    #
    # DirPath_list = glob.glob('./ED*_Dent')
    #
    # for DirPath in tqdm(DirPath_list):
    #
    #         DirSavePath = DirPath.replace('Dent','Dent_COG')#'./ED44Cabed_Dent_COG'...
    #         npyPath_list = glob.glob(DirPath+'/*')
    #         for npyPath in npyPath_list:
    #             npySavePath = npyPath.replace('Dent','Dent_COG')#'./NewCabed_Dent_COG/1956_cabed_all_ED.py',...
    #             npySavePath = npySavePath.replace('.npy','')#'./NewCabed_Dent_COG/1956_cabed_all_ED',...
    #
    #             Dentdata = np.load(npyPath)
    #             output_cabed_COG = COGCla.centorofgravity(Dentdata,npySavePath)
    #             np.save(npySavePath+"_COG.npy", output_cabed_COG)

    # if os.path.isdir('./Row_Dent_COG') == False:#なければ保存用のディレクトリ作成
    #     os.mkdir('./Row_Dent_COG')
    #
    # npyPath_list = glob.glob('../npyGen/NPY/Dentifrice_Cleaned/*.npy')#'../npyGen/NPY/Dentifrice_Cleaned/1964.npy',...
    #
    # for npyPath in npyPath_list:
    #     npySavePath = npyPath.replace('../npyGen/NPY/Dentifrice_Cleaned','./Row_Dent_COG')#'./Row_Dent_COG/1956.py',...
    #     npySavePath = npySavePath.replace('.npy','')#'./NewCabed_Dent_COG/1956',...
    #
    #     Dentdata = np.load(npyPath)
    #     output_cabed_COG = COGCla.centorofgravity(Dentdata,npySavePath)
    #     np.save(npySavePath+"_COG.npy", output_cabed_COG)
