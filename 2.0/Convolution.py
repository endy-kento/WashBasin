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

    """60*60����15*16�ɏW�񂷂�"""

    # def __init__(self):

    #60*60*10����30*30*10�ɏW��
    def convolution(self,data_path,save_path):
        convolution_map = np.zeros([15, 16])#�W���̍s��̏�����
        data = np.loadtxt(data_path,delimiter=',')#�Ώۂ̃t�@�C���Ɛ��`��̃t�@�C�����J��

        for line in range(15):
            for column in range(16) :
                if np.sum(data[line*4:line*4+4,column*4:column*4+4]) == 0:
                    ave = 0
                else:
                    ave = np.mean(data[line*4:line*4+4,column*4:column*4+4])

                convolution_map[line][column] = ave#16�}�X�̕��ςŏ�ݍ���

        np.savetxt(save_path,convolution_map,delimiter=',')#�W���s���ۑ�

    #15*16*10����15*16�ɏW��
    def calibrationMapGenerator(self,dirpath_list):
        mean_map = np.zeros([15, 16])#�W���̍s��̏�����(����)
        med_map = np.zeros([15, 16])#�W���̍s��̏�����(����)
        mode_map = np.zeros([15, 16])#�W���̍s��̏�����(�ŕp�l)
        var_map = np.zeros([15, 16])#�W���̍s��̏�����(���U)
        sd_map = np.zeros([15, 16])#�W���̍s��̏�����(�W���΍�)

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

        mean_map = np.loadtxt('./mean_map.csv',delimiter=',')
        #�O���ƒ����̉���������菜��
        mean_map = np.delete(mean_map, 0, 0)#�s�폜
        mean_map = np.delete(mean_map, -1, 0)#�s�폜
        mean_map = np.delete(mean_map, 7, 1)#��폜
        mean_map = np.delete(mean_map, 0, 1)#��폜
        mean_map = np.delete(mean_map, -1, 1)#��폜

        mean_list=mean_map.reshape(-1,)#�ꎟ���z���
        i=mean_list.nonzero()#0�ȊO����菜��
        print stats.mode(mean_list[i])
        mean_hist_1000_hist = np.c_[np.append(np.histogram(mean_list[i], bins=1000)[0], 0 ), np.histogram(mean_list[i], bins=1000)[1]]
        np.savetxt('mean_hist_1000_hist.csv',mean_hist_1000_hist,delimiter=',', fmt='%d')
        print mean_hist_1000_hist[np.argmax(mean_hist_1000_hist[:,0]),1]
        # print np.argmax(mean_hist_1000_hist[:,0])
        mean_hist_500_hist = np.c_[np.append(np.histogram(mean_list[i], bins=500)[0], 0 ), np.histogram(mean_list[i], bins=500)[1]]
        np.savetxt('mean_hist_500_hist.csv',mean_hist_500_hist,delimiter=',', fmt='%d')
        print mean_hist_500_hist[np.argmax(mean_hist_500_hist[:,0]),1]
        # print np.argmax(mean_hist_500_hist[:,0])
        mean_hist_100_hist = np.c_[np.append(np.histogram(mean_list[i], bins=100)[0], 0 ), np.histogram(mean_list[i], bins=100)[1]]
        np.savetxt('mean_hist_100_hist.csv',mean_hist_100_hist,delimiter=',', fmt='%d')
        print mean_hist_100_hist[np.argmax(mean_hist_100_hist[:,0]),1]
        # print np.argmax(mean_hist_100_hist[:,0])


        #�q�X�g�O�����̕`��
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mean_list, bins=1000)
        plt.savefig('./mean_1000.png')

        #�q�X�g�O�����̕`��
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mean_list, bins=500)
        plt.savefig('./mean_500.png')

        #�q�X�g�O�����̕`��
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mean_list, bins=100)
        plt.savefig('./mean_100.png')

        med_map = np.loadtxt('./med_map.csv',delimiter=',')
        #�O���ƒ����̉���������菜��
        med_map = np.delete(med_map, 0, 0)#�s�폜
        med_map = np.delete(med_map, -1, 0)#�s�폜
        med_map = np.delete(med_map, 7, 1)#��폜
        med_map = np.delete(med_map, 0, 1)#��폜
        med_map = np.delete(med_map, -1, 1)#��폜

        med_list = med_map.reshape(-1,)#�ꎟ���z���
        i = med_list.nonzero()#0�ȊO����菜��
        print stats.mode(med_list[i])
        med_hist_1000_hist = np.c_[np.append(np.histogram(med_list[i], bins=1000)[0], 0 ), np.histogram(med_list[i], bins=1000)[1]]
        np.savetxt('med_hist_1000_hist.csv',med_hist_1000_hist,delimiter=',', fmt='%d')
        print med_hist_1000_hist[np.argmax(med_hist_1000_hist[:,0]),1]
        # print np.argmax(med_hist_1000_hist[:,0])
        med_hist_500_hist = np.c_[np.append(np.histogram(med_list[i], bins=500)[0], 0 ), np.histogram(med_list[i], bins=500)[1]]
        np.savetxt('med_hist_500_hist.csv',med_hist_500_hist,delimiter=',', fmt='%d')
        print med_hist_500_hist[np.argmax(med_hist_500_hist[:,0]),1]
        # print np.argmax(med_hist_500_hist[:,0])
        med_hist_100_hist = np.c_[np.append(np.histogram(med_list[i], bins=100)[0], 0 ), np.histogram(med_list[i], bins=100)[1]]
        np.savetxt('med_hist_100_hist.csv',med_hist_100_hist,delimiter=',', fmt='%d')
        print med_hist_100_hist[np.argmax(med_hist_100_hist[:,0]),1]
        # print np.argmax(med_hist_100_hist[:,0])

        #�q�X�g�O�����̕`��
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(med_list, bins=1000)
        plt.savefig('./med_1000.png')

        #�q�X�g�O�����̕`��
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(med_list, bins=500)
        plt.savefig('./med_500.png')

        #�q�X�g�O�����̕`��
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(med_list, bins=100)
        plt.savefig('./med_100.png')

        mod_map = np.loadtxt('./mode_map.csv',delimiter=',')
        #�O���ƒ����̉���������菜��
        mod_map = np.delete(mod_map, 0, 0)#�s�폜
        mod_map = np.delete(mod_map, -1, 0)#�s�폜
        mod_map = np.delete(mod_map, 7, 1)#��폜
        mod_map = np.delete(mod_map, 0, 1)#��폜
        mod_map = np.delete(mod_map, -1, 1)#��폜

        mod_list = mod_map.reshape(-1,)#�ꎟ���z���
        i = mod_list.nonzero()#0�ȊO����菜��
        print stats.mode(mod_list[i])
        mod_hist_1000_hist = np.c_[np.append(np.histogram(mod_list[i], bins=1000)[0], 0 ), np.histogram(mod_list[i], bins=1000)[1]]
        np.savetxt('mod_hist_1000_hist.csv',mod_hist_1000_hist,delimiter=',', fmt='%d')
        print mod_hist_1000_hist[np.argmax(mod_hist_1000_hist[:,0]),1]
        # print np.argmax(mod_hist_1000_hist[:,0])
        mod_hist_500_hist = np.c_[np.append(np.histogram(mod_list[i], bins=500)[0], 0 ), np.histogram(mod_list[i], bins=500)[1]]
        np.savetxt('mod_hist_500_hist.csv',mod_hist_500_hist,delimiter=',', fmt='%d')
        print mod_hist_500_hist[np.argmax(mod_hist_500_hist[:,0]),1]
        # print np.argmax(mod_hist_500_hist[:,0])
        mod_hist_100_hist = np.c_[np.append(np.histogram(mod_list[i], bins=100)[0], 0 ), np.histogram(mod_list[i], bins=100)[1]]
        np.savetxt('mod_hist_100_hist.csv',mod_hist_100_hist,delimiter=',', fmt='%d')
        print mod_hist_100_hist[np.argmax(mod_hist_100_hist[:,0]),1]
        # print np.argmax(mod_hist_100_hist[:,0])

        #�q�X�g�O�����̕`��
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mod_list, bins=1000)
        plt.savefig('./mod_1000.png')

        #�q�X�g�O�����̕`��
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mod_list, bins=500)
        plt.savefig('./mod_500.png')

        #�q�X�g�O�����̕`��
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mod_list, bins=100)
        plt.savefig('./mod_100.png')


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
