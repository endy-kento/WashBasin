#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Convolution_point.py���N���X���������́B
#./CSV/Cleaned/ �ȉ��̃f�[�^��60*60����30*30�ɏW�� ./CSV/Convolution/ �ɕۑ�
#���̃|�C���g��2�b�ԕ�(10�f�[�^)��[����,����,�ŕp,���U,�W���΍�]��30*30��5��csv�t�@�C�����쐬

import glob
import os, commands
import os.path
import csv
import numpy as np
from scipy import stats
from tqdm import tqdm
import matplotlib.pyplot as plt
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")#.DS_Store�t�@�C������菜��


class ConvolutionClass:

    """60*60����30*30�ɏW�񂷂�"""

    # def __init__(self):

    #60*60*10����30*30*10�ɏW��
    def convolution(self,data_path,save_path):
        convolution_map = np.zeros([30, 30])#�W���̍s��̏�����
        data = np.loadtxt(data_path,delimiter=',')#�Ώۂ̃t�@�C���Ɛ��`��̃t�@�C�����J��

        for line in range(30):
            for column in range(30) :
                if np.sum(data[line*2:line*2+2,column*2:column*2+2]) == 0:
                    ave = 0
                else:
                    ave = np.mean(data[line*2:line*2+2,column*2:column*2+2])

                convolution_map[line][column] = ave #4�}�X�̕��ςŏ�ݍ���

        np.savetxt(save_path,convolution_map,delimiter=',')#�W���s���ۑ�

    #30*30*10����30*30�ɏW��
    def calibrationMapGenerator(self,dirpath_list):
        mean_map = np.zeros([30, 30])#�W���̍s��̏�����(����)
        med_map = np.zeros([30, 30])#�W���̍s��̏�����(����)
        mode_map = np.zeros([30, 30])#�W���̍s��̏�����(�ŕp�l)
        var_map = np.zeros([30, 30])#�W���̍s��̏�����(���U)
        sd_map = np.zeros([30, 30])#�W���̍s��̏�����(�W���΍�)

        for DirPath in dirpath_list:#1-1,1-2,...��

            CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Convolution/1-1/CSP1956000000.csv',...
            CsvName_list = os.listdir(DirPath)#'CSP1956000000.csv',...
            num = DirPath.replace('./CSV/Convolution/','')#'1-1/CSP1956000000.csv',...
            num=num.split("-")#[1] [1/CSP1956000000.csv],...
            line = int(num[0])-1#[1]-1
            column = int(num[1])-1#[1(/CSP1956000000.csv)]-1,...
            holder = np.array([])#���̃|�C���g��2�b�ԕ�(10�f�[�^)���i�[����z��̏�����

            for CsvPath in CsvPath_list:#CSP1956000000.csv,...��
                data = np.loadtxt(CsvPath,delimiter=',')#�Ώۂ̃t�@�C���̃t�@�C�����J��
                holder = np.append(holder,data[line,column])#���̃|�C���g��2�b�ԕ�(10�f�[�^)���i�[

            #���ϒl
            mean_map[line,column] = np.average(holder)
            #�����l
            med_map[line,column] = np.median(holder)
            #�ŕp�l
            mode_map[line,column] = stats.mode(holder)[0]
            #���U
            var_map[line,column] = np.var(holder)
            #�W���΍�
            sd_map[line,column] = np.std(holder)

        np.savetxt('mean_map.csv',mean_map,delimiter=',')#�W���s���ۑ�(����)
        np.savetxt('med_map.csv',med_map,delimiter=',')#�W���s���ۑ�(����)
        np.savetxt('mode_map.csv',mode_map,delimiter=',')#�W���s���ۑ�(�ŕp�l)
        np.savetxt('var_map.csv',var_map,delimiter=',')#�W���s���ۑ�(���U)
        np.savetxt('sd_map.csv',sd_map,delimiter=',')#�W���s���ۑ�(�W���΍�)




ConCla = ConvolutionClass()
DirPath_list = glob.glob('./CSV/Cleaned/*')#'./CSV/Cleaned/1-1',...

if os.path.isdir('./CSV/Convolution') == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
    os.mkdir('./CSV/Convolution')

for DirPath in tqdm(DirPath_list):

    DirSavePath = DirPath.replace('Cleaned','Convolution')
    if os.path.isdir(DirSavePath) == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
        os.mkdir(DirSavePath)

    CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Cleaned/1-1/CSP1956000000.csv',...

    for CsvPath in CsvPath_list:

        CsvSavePath = CsvPath.replace('Cleaned','Convolution')#'./CSV/Convolution/1-1/CSP1956000000.csv',...
        #./CSV/Cleaned/ �ȉ��̃f�[�^��60*60����30*30�ɏW�� ./CSV/Convolution/ �ɕۑ�
        ConCla.convolution(CsvPath,CsvSavePath)

DirPath_list = glob.glob('./CSV/Convolution/*')#'./CSV/Convolution/1-1',...
#���̃|�C���g��2�b�ԕ�(10�f�[�^)��[����,����,�ŕp,���U,�W���΍�]��30*30��5��csv�t�@�C�����쐬
ConCla.calibrationMapGenerator(DirPath_list)
