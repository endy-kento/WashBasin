#!/usr/bin/env python
#-*- coding:utf-8 -*-
#4パターンのED処理とSDの高低差による補正を行う

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
class ED_CalibrationClass:

    """ED処理とSDの高低差による補正を行う"""



#SDによる補正を行う
    def SD_Cab(self,Motion,Threshold):
        line,column,frame = Motion.shape
        SD_map = np.zeros([line,column])
        SD_CabedMotion = Motion

        for lines in range(line):
            for columns in range(column):
                SD_map[lines,columns] = np.std(Motion[lines,columns,:])

        index = np.where(SD_map[:,:] > Threshold)

        for frames in range(frame):
            for count in range(len(index[0])):
                if index[0][count] == 0:
                    SD_CabedMotion[index[0],index[1],frames] = 0
                elif index[0][count] == 59:
                    SD_CabedMotion[index[0],index[1],frames] = 0
                elif index[0][count] == None:
                    SD_CabedMotion[index[0],index[1],frames] = 0
                else:
                    SD_CabedMotion[index[0],index[1],frames] = (Motion[index[0]-1,index[1],frames]+Motion[index[0]+1,index[1],frames])/2

        return SD_CabedMotion

#ED処理を行う
    def ED_Cab(self,Motion,npySavePath,ED):#'./Cabed_Motion/Dentifrice'...
        # 4近傍の定義
        neiborhood4 = np.array([[0, 1, 0],
                                [1, 1, 1],
                                [0, 1, 0]],
                                np.uint8)

        # 8近傍の定義
        neiborhood8 = np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]],
                                np.uint8)

        line,column,frame = Motion.shape
        ED_CabedMotion = np.zeros([line,column,frame])
        for frames in range(frame):
            Gray_map = np.zeros([line,column])#元のデータを二値化
            Gray_map[Motion[:,:,frames]>0] = 1


            if ED == 44:
                #ED44
                E_Gray_map = cv2.erode(Gray_map,neiborhood4,iterations=1)
                ED_Gray_map = cv2.dilate(E_Gray_map,neiborhood4,iterations=1)
                ED_CabedMotion[:,:,frames] = Motion[:,:,frames]*ED_Gray_map[:,:]
            elif ED == 48:
                #ED48
                E_Gray_map = cv2.erode(Gray_map,neiborhood4,iterations=1)
                ED_Gray_map = cv2.dilate(E_Gray_map,neiborhood8,iterations=1)
                ED_CabedMotion[:,:,frames] = Motion[:,:,frames]*ED_Gray_map[:,:]
            elif ED == 84:
                #ED84
                E_Gray_map = cv2.erode(Gray_map,neiborhood8,iterations=1)
                ED_Gray_map = cv2.dilate(E_Gray_map,neiborhood4,iterations=1)
                ED_CabedMotion[:,:,frames] = Motion[:,:,frames]*ED_Gray_map[:,:]
            elif ED == 88:
                #ED88
                E_Gray_map = cv2.erode(Gray_map,neiborhood8,iterations=1)
                ED_Gray_map = cv2.dilate(E_Gray_map,neiborhood8,iterations=1)
                ED_CabedMotion[:,:,frames] = Motion[:,:,frames]*ED_Gray_map[:,:]


        #save
        if os.path.isdir(npySavePath+"/ED"+str(ED)) == False:#なければ保存用のディレクトリ作成
            os.mkdir(npySavePath+"/ED"+str(ED))
        if 'all' in npyPath:
            np.save(npySavePath+"/ED"+str(ED)+"/cabed_all.npy", ED_CabedMotion)
        elif 'rep' in npyPath:
            np.save(npySavePath+"/ED"+str(ED)+"/cabed_rep.npy", ED_CabedMotion)


if __name__ == '__main__':
    EDC= ED_CalibrationClass()

    MotionPath_list = glob.glob('./Cabed_Motion/*')#'./Cabed_Motion/Dentifrice'...
    for MotionPath in MotionPath_list:#'./Cabed_Motion/Dentifrice'...
        npyPath_list = glob.glob(MotionPath+'/*.npy')#'Cabed_Motion/Dentifrice/cabed_all.npy'...
        for npyPath in npyPath_list:#'Cabed_Motion/Dentifrice/cabed_all.npy'...
            Motiondata = np.load(npyPath)
            SD_Motiondata = EDC.SD_Cab(Motiondata,2000)

            EDC.ED_Cab(SD_Motiondata,MotionPath,44)
            EDC.ED_Cab(SD_Motiondata,MotionPath,48)
            EDC.ED_Cab(SD_Motiondata,MotionPath,84)
            EDC.ED_Cab(SD_Motiondata,MotionPath,88)
