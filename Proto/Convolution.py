#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Convolution_point.py���N���X���������́B
#���؃f�[�^(�d����悹�Ă����ē����f�[�^)���瓾��ꂽ�W��f�[�^�y�ь덷�����f�[�^�̎Z�o�͍s��Ȃ��B
#���łɁA�덷�����f�[�^�����߂Ă�����̂Ƃ���
#�̂ŁA�����ł͐��l�݂̂�������60*60����9�|�C���g�Â��W�񂵂�20*20�̃f�[�^�ɕϊ����邾���̃v���O�����ł���B

import glob
import os, commands
import os.path
import csv
import numpy as np
from tqdm import tqdm
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")


class ConvolutionClass:

    """60*60����20*20�ɏW�񂷂�"""

    # def __init__(self):

    def convolution(self,data_path,save_path):#60*60����20*20�ɏW�񂷂�
        convolution_map = np.zeros([20, 20])#�W���̍s��̏�����
        data = np.loadtxt(data_path,delimiter=',')#�Ώۂ̃t�@�C���Ɛ��`��̃t�@�C�����J��
        for line in range(20):
            for column in range(20) :

                if np.sum(data[line*3:line*3+3,column*3:column*3+3]) == 0:
                    ave = 0
                else:
                    ave = np.mean(data[line*3:line*3+3,column*3:column*3+3])

                convolution_map[line][column] = ave

        np.savetxt(save_path,convolution_map,delimiter=',')#�W���s���ۑ�



ConCla = ConvolutionClass()
DirPath_list = glob.glob('./CSV/Cleaned/*')#'./CSV/Cleaned/1965',...

if os.path.isdir('./CSV/Convolution') == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
    os.mkdir('./CSV/Convolution')

for DirPath in tqdm(DirPath_list):

    DirSavePath = DirPath.replace('Cleaned','Convolution')
    if os.path.isdir(DirSavePath) == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
        os.mkdir(DirSavePath)

    CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Cleaned/1965/CSP1956000000.csv',...

    for CsvPath in tqdm(CsvPath_list):

        CsvSavePath = CsvPath.replace('Cleaned','Convolution')#'./CSV/Convolution/1965/CSP1956000000.csv',...
        ConCla.convolution(CsvPath,CsvSavePath)#60*60����20*20�ɏW��
