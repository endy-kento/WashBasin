#!/usr/bin/env python
#-*- coding:utf-8 -*-
#�Y��ɂȂ������f�[�^��A��������npy�`���ɕϊ�����N���X
#�����ɑ�� : �A�N�����T�C�Y ��� : �T���v���� ��O : �f�B���N�g����
#ex) python npyGen.py 1.5 100 111.1gp

import glob
import os, commands
import os.path
import numpy as np
from tqdm import tqdm
import sys
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")
np.set_printoptions(threshold=np.inf)
args = sys.argv

if os.path.isdir('./NPY') == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
    os.mkdir('./NPY')



class NpyGenClass:

    """�Y��ɂȂ������f�[�^��A��������npy�`���ɕϊ�"""

    def personNpyGen(self,NamePath_list):
        if os.path.isdir('./NPY/Person') == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
            os.mkdir('./NPY/Person')
        npy_map = np.zeros([60, 60,10])#�W���̍s��̏�����(����)
        for NamePath in tqdm(NamePath_list):
            SaveNamePath = NamePath.replace('CSV','NPY')#'./NPY/Person/jyu,...
            if os.path.isdir(SaveNamePath) == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
                os.mkdir(SaveNamePath)
            TryPath_list = glob.glob(NamePath+'/*')#'./CSV/Person/jyu/1,...
            for TryPath in TryPath_list:
                SaveTryPath = TryPath.replace('CSV','NPY')#'./NPY/Person/jyu/1,...
                CsvPath_list = glob.glob(TryPath+'/*.csv')#'./CSV/Person/jyu/1/CSP1956000000.csv',...
                count = 0
                for CsvPath in CsvPath_list:
                    data = np.loadtxt(CsvPath,delimiter=',')#�Ώۂ̃t�@�C���̃t�@�C�����J��
                    npy_map[:,:,count] = data[:,:]
                    count=count+1
                np.save(SaveTryPath+".npy", npy_map)

    def DentNpyGen(self,NamePath_list):
        if os.path.isdir('./NPY/Dentifrice_Cleaned') == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
            os.mkdir('./NPY/Dentifrice_Cleaned')
        for NamePath in tqdm(NamePath_list):
            SaveNamePath = NamePath.replace('CSV','NPY')#'./NPY/Person/jyu,...
            CsvPath_list = glob.glob(NamePath+'/*')#'./CSV/Person/jyu/1,...
            filelen = len(CsvPath_list)
            npy_map = np.zeros([60, 60,filelen])#�W���̍s��̏�����(����)
            count = 0
            for CsvPath in CsvPath_list:
                data = np.loadtxt(CsvPath,delimiter=',')#�Ώۂ̃t�@�C���̃t�@�C�����J��
                npy_map[:,:,count] = data[:,:]
                count=count+1
            np.save(SaveNamePath+".npy", npy_map)

    def MotionNpyGen(self,NamePath_list):
        if os.path.isdir('./NPY/Motion_Data') == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
            os.mkdir('./NPY/Motion_Data')

        for NamePath in tqdm(NamePath_list):#'./CSV/Cleaned_Motion_Data/Dentifrice',...
            SaveNamePath = NamePath.replace('CSV/Cleaned_','NPY/')#'./NPY/Motion_Data/Dentifrice',...
            CsvPath_list = glob.glob(NamePath+'/*')#'./NPY/Motion_Data/Dentifrice/CSP2156000000.csv',...
            framelen = len(CsvPath_list)#�t���[���̌�
            npy_map = np.zeros([60, 60,framelen])#0�ŏ���������npy�t�@�C���̐��`
            count = 0#�t���[�������J�E���g
            for CsvPath in CsvPath_list:#'./NPY/Motion_Data/Dentifrice/CSP2156000000.csv',...
                data = np.loadtxt(CsvPath,delimiter=',')#�Ώۂ̃t�@�C�����J��
                npy_map[:,:,count] = data[:,:]
                count=count+1
            np.save(SaveNamePath+".npy", npy_map)

    def SampleNpyGen(self,size,zLen,dirName,dirpath_list):
        if zLen == "10":
            npy_map = np.zeros([60, 60,10])#�W���̍s��̏�����(����)
        elif zLen == "100":
            npy_map = np.zeros([60, 60,100])#�W���̍s��̏�����(����)

        for DirPath in tqdm(dirpath_list):

            CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Cleaned/1-1/CSP1956000000.csv',...
            CsvName_list = os.listdir(DirPath)#'CSP1956000000.csv',...
            num = DirPath.replace('./CSV/'+dirName+'/','')
            num=num.split("-")
            line = int(num[0])-1
            column = int(num[1])-1
            count=0
            for CsvPath in CsvPath_list:
                data = np.loadtxt(CsvPath,delimiter=',')#�Ώۂ̃t�@�C���̃t�@�C�����J��
                if size == '1.0':
                    npy_map[line*2,column*2,count]=data[line*2,column*2]
                    npy_map[line*2,column*2+1,count]=data[line*2,column*2+1]
                    npy_map[line*2+1,column*2,count]=data[line*2+1,column*2]
                    npy_map[line*2+1,column*2+1,count]=data[line*2+1,column*2+1]

                elif size == '1.5':
                    npy_map[line*3,column*3,count]=data[line*3,column*3]
                    npy_map[line*3,column*3+1,count]=data[line*3,column*3+1]
                    npy_map[line*3,column*3+2,count]=data[line*3,column*3+2]

                    npy_map[line*3+1,column*3,count]=data[line*3+1,column*3]
                    npy_map[line*3+1,column*3+1,count]=data[line*3+1,column*3+1]
                    npy_map[line*3+1,column*3+2,count]=data[line*3+1,column*3+2]

                    npy_map[line*3+2,column*3,count]=data[line*3+2,column*3]
                    npy_map[line*3+2,column*3+1,count]=data[line*3+2,column*3+1]
                    npy_map[line*3+2,column*3+2,count]=data[line*3+2,column*3+2]

                elif size == '2.0':
                    if column == 7 :
                        npy_map[line*4,column*4,count]=data[line*4,column*4]
                        npy_map[line*4+1,column*4,count]=data[line*4+1,column*4]
                        npy_map[line*4+2,column*4,count]=data[line*4+2,column*4]
                        npy_map[line*4+3,column*4,count]=data[line*4+3,column*4]

                        npy_map[line*4,column*4+1,count]=data[line*4,column*4+1]
                        npy_map[line*4+1,column*4+1,count]=data[line*4+1,column*4+1]
                        npy_map[line*4+2,column*4+1,count]=data[line*4+2,column*4+1]
                        npy_map[line*4+3,column*4+1,count]=data[line*4+3,column*4+1]

                    elif column == 15 :
                        npy_map[line*4,column*4-1,count]=data[line*4,column*4-1]
                        npy_map[line*4+1,column*4-1,count]=data[line*4+1,column*4-1]
                        npy_map[line*4+2,column*4-1,count]=data[line*4+2,column*4-1]
                        npy_map[line*4+3,column*4-1,count]=data[line*4+3,column*4-1]

                        npy_map[line*4,column*4-2,count]=data[line*4,column*4-2]
                        npy_map[line*4+1,column*4-2,count]=data[line*4+1,column*4-2]
                        npy_map[line*4+2,column*4-2,count]=data[line*4+2,column*4-2]
                        npy_map[line*4+3,column*4-2,count]=data[line*4+3,column*4-2]

                    elif column < 7 :
                        npy_map[line*4,column*4,count]=data[line*4,column*4]
                        npy_map[line*4+1,column*4,count]=data[line*4+1,column*4]
                        npy_map[line*4+2,column*4,count]=data[line*4+2,column*4]
                        npy_map[line*4+3,column*4,count]=data[line*4+3,column*4]

                        npy_map[line*4,column*4+1,count]=data[line*4,column*4+1]
                        npy_map[line*4+1,column*4+1,count]=data[line*4+1,column*4+1]
                        npy_map[line*4+2,column*4+1,count]=data[line*4+2,column*4+1]
                        npy_map[line*4+3,column*4+1,count]=data[line*4+3,column*4+1]

                        npy_map[line*4,column*4+2,count]=data[line*4,column*4+2]
                        npy_map[line*4+1,column*4+2,count]=data[line*4+1,column*4+2]
                        npy_map[line*4+2,column*4+2,count]=data[line*4+2,column*4+2]
                        npy_map[line*4+3,column*4+2,count]=data[line*4+3,column*4+2]

                        npy_map[line*4,column*4+3,count]=data[line*4,column*4+3]
                        npy_map[line*4+1,column*4+3,count]=data[line*4+1,column*4+3]
                        npy_map[line*4+2,column*4+3,count]=data[line*4+2,column*4+3]
                        npy_map[line*4+3,column*4+3,count]=data[line*4+3,column*4+3]

                    elif 7 < column <15:
                        npy_map[line*4,column*4,count]=data[line*4,column*4]
                        npy_map[line*4+1,column*4,count]=data[line*4+1,column*4]
                        npy_map[line*4+2,column*4,count]=data[line*4+2,column*4]
                        npy_map[line*4+3,column*4,count]=data[line*4+3,column*4]

                        npy_map[line*4,column*4+1,count]=data[line*4,column*4+1]
                        npy_map[line*4+1,column*4+1,count]=data[line*4+1,column*4+1]
                        npy_map[line*4+2,column*4+1,count]=data[line*4+2,column*4+1]
                        npy_map[line*4+3,column*4+1,count]=data[line*4+3,column*4+1]

                        npy_map[line*4,column*4-1,count]=data[line*4,column*4-1]
                        npy_map[line*4+1,column*4-1,count]=data[line*4+1,column*4-1]
                        npy_map[line*4+2,column*4-1,count]=data[line*4+2,column*4-1]
                        npy_map[line*4+3,column*4-1,count]=data[line*4+3,column*4-1]

                        npy_map[line*4,column*4-2,count]=data[line*4,column*4-2]
                        npy_map[line*4+1,column*4-2,count]=data[line*4+1,column*4-2]
                        npy_map[line*4+2,column*4-2,count]=data[line*4+2,column*4-2]
                        npy_map[line*4+3,column*4-2,count]=data[line*4+3,column*4-2]
                count=count+1
        np.save("./NPY/"+dirName+".npy", npy_map)



NpyGen = NpyGenClass()

#Person
# NamePath_list = glob.glob('./CSV/Dentifrice_Cleaned/*')#'./CSV/Person/jyu',...
# NpyGen.DentNpyGen(NamePath_list)

#50g/point
# dirPath_list = glob.glob('./CSV/'+args[3]+'/*')#'./CSV/50gp/1-1',...
# NpyGen.SampleNpyGen(args[1],args[2],args[3],dirPath_list)

#Motion_Data
dirPath_list = glob.glob('./CSV/Cleaned_Motion_Data/*')#'./CSV/Cleaned_Motion_Data/Dentifrice',...
NpyGen.MotionNpyGen(dirPath_list)
