#!/usr/bin/env python
#-*- coding:utf-8 -*-
#�����ŕ␳���s��
#���O�Ɍv����20*20�ɏW�񂳂ꂽ�f�[�^�ɕ␳�̂��߂̍s����g���āu�ꖇ�Âv�␳���s��
#���̌�A�␳���ꂽ�f�[�^��A������

import glob
import os,commands
import os.path
import numpy as np
from tqdm import tqdm
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")

class CalibrationClass:

    """�f�[�^�̕␳���s��"""

    # def __init__(self):

    def calibration(self,data_path,save_path):
        cal_map = np.zeros([20, 20])

        #�Ώۂ̃f�[�^�ƕ␳�p�̍s����J��
        data = np.loadtxt(data_path,delimiter=',')
        calibration_map = np.loadtxt('./calibration_map.csv',delimiter=',')
        cal_map = calibration_map * data#�|�����킹�邱�Ƃɂ���ĕ␳

        np.savetxt(save_path,cal_map,delimiter=',')#�C����s���ۑ�


#�f�[�^�̕␳���s��
CalCla = CalibrationClass()
DirPath_list = glob.glob('./CSV/Convolution/*')#'./CSV/Convolution/1965',...

if os.path.isdir('./CSV/Calibration') == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
    os.mkdir('./CSV/Calibration')

for DirPath in DirPath_list:

        DirSavePath = DirPath.replace('Convolution','Calibration')#'./CSV/Calibration/1965',...
        if os.path.isdir(DirSavePath) == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
            os.mkdir(DirSavePath)

        CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Convolution/1965/CSP1956000000.csv',...

        for CsvPath in CsvPath_list:

            CsvSavePath = CsvPath.replace('Convolution','Calibration')#'./CSV/Calibration/1965/CSP1956000000.csv',...
            CalCla.calibration(CsvPath,CsvSavePath)#�f�[�^�̕␳
