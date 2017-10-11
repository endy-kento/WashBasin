#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tqdm import tqdm
import glob
import os, commands
import os.path
import cv2
import os, commands
import sys
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")
args = sys.argv

class Video_GenClass:

    def Video_Gen(self,AorRPath,pngPath_list):
        if os.path.isdir(AorRPath+'/video.mp4') == True:#なければ保存用のディレクトリ作成
            os.remove(AorRPath+'/video.mp4')
        fs = 37.0
        fourcc = cv2.cv.CV_FOURCC('m','p','4','v')
        video = cv2.VideoWriter(AorRPath+'/video.mp4', fourcc, fs, (640, 480))

        print range(len(pngPath_list))
        for i in tqdm(range(len(pngPath_list))):
            img = cv2.imread(AorRPath+'/heatmap/'+str(i)+'.png')
            img = cv2.resize(img, (640,480))
            video.write(img)

        cv2.destroyAllWindows()
        video.release()

if __name__ == '__main__':
    VG = Video_GenClass()

    # #Row_Motion
    # npyPath_list = glob.glob('./Row_Motion/*.npy')#'./Row_Motion_COG/Dentifrice.npy',...
    # for npyPath in tqdm(npyPath_list):#'./Row_Motion_COG/Dentifrice.npy',...
    #     figSavePath = npyPath.replace('_COG.npy','')#'Row_Motion_COG/Dentifrice'...
    #     if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
    #             os.mkdir(figSavePath)#'./Row_Motion_COG/Dentifrice'...
    #
    #             VG.Video_Genlysis(COGdata,figSavePath)
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
    #
    #                 VG.Video_Genlysis(COGdata,figSavePath)


    #Cabed_Motion//Dentifrice/ED44
    MotionPath_list = glob.glob('./Cabed_Motion/*/')#'./Cabed_Motion/Dentifrice'...
    for MotionPath in tqdm(MotionPath_list):#'./Cabed_Motion/Dentifrice'...
        EDPath_list = glob.glob(MotionPath+'/ED*/')#'Cabed_Motion/Dentifrice/ED44'...
        for EDPath in EDPath_list:#'Cabed_Motion/Dentifrice/ED44'...
            AorRPath_list = glob.glob(EDPath+'/*/')#'Cabed_Motion/Dentifrice/ED44/all'...
            for AorRPath in AorRPath_list:
                pngPath_list = AorRPath+'/heatmap/*.png'#'Cabed_Motion/Dentifrice/ED44/all/heatmap/0.png'...
                VG.Video_Gen(AorRPath,pngPath_list)
