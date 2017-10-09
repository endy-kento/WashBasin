#!/usr/bin/env python
#-*- coding:utf-8 -*-
#�����ŕ␳���s��
#���O�Ɍv����20*20�ɏW�񂳂ꂽ�f�[�^�ɕ␳�̂��߂̍s����g���āu�ꖇ�Âv�␳���s��
#���̌�A�␳���ꂽ�f�[�^��A������

import glob
import os,commands
import os.path
import csv
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
DirPath_list = glob.glob('./CSV/Convolution/*')#'./CSV/Convolution/jyu',...

if os.path.isdir('./CSV/Calibration') == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
    os.mkdir('./CSV/Calibration')

for DirPath in DirPath_list:

    DirSavePath = DirPath.replace('Convolution','Calibration')
    if os.path.isdir(DirSavePath) == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
        os.mkdir(DirSavePath)

    TryNumPath_list = glob.glob(DirPath+'/*')#'./CSV/Convolution/jyu/1',...

    for TryNumPath in TryNumPath_list :#���s�񐔕��A��]('1', '2', '3',...)

        TryNumSavePath = TryNumPath.replace('Convolution','Calibration')
        if os.path.isdir(TryNumSavePath) == False:#�Ȃ���Εۑ��p�̃f�B���N�g���쐬
            os.mkdir(TryNumSavePath)

        CsvPath_list = glob.glob(TryNumPath+'/*')#'./CSV/Convolution/jyu/1/CSP1427000000.csv',...

        for CsvPath in CsvPath_list:#�t���[�����A��]('CSP1427000000.csv', 'CSP1427000001.csv',...)
            CsvSavePath = CsvPath.replace('Convolution','Calibration')
            CalCla.calibration(CsvPath,CsvSavePath)#�f�[�^�̕␳
