#!/usr/bin/env python
#-*- coding:utf-8 -*-
#���l�݂̂�������60*60����9�|�C���g�Â��W�񂵂�20*20�̃f�[�^�ɕϊ�
#-----����-----
#�S�̂̕��ς���̊����ŏC�����Ă��邪�A���̂�����Ǝ��Ă��Ȃ��l�Ɉ���������\������
#���ɂ����C�����@���邩��
#------------

import glob
import os
import os.path
import csv
import numpy as np
from tqdm import tqdm


##���݌��Ă���s�񂩂�d����ڂ���9�|�C���g���W��
#�d����ڂ��Ă��Ȃ��Ƃ���́u�l�����Ă��Ȃ��v
# def Intensive(csvname,line,column):
#     datafile = csvname
#     #�Ώۂ̃t�@�C���Ɛ��`��̃t�@�C�����J��
#     file_in = np.loadtxt(csvname,delimiter=',',dtype=np.float32)
#     line = (line-1) * 3
#     column = (column-1) * 3
#     add9points=0
#     for i in range(3) :
#         for j in range(3):
#             add9points = add9points + file_in[line+i][column+j]
#
#     # print add9points
#     return add9points#�d����ڂ���9�|�C���g�̒l��Ԃ�

##�ȑO�v�������f�[�^��9�|�C���g�ÂW��
def Intensive_data(csvname):
    add9points_map = np.zeros([20, 20])
    datafile = csvname
    #�Ώۂ̃t�@�C���Ɛ��`��̃t�@�C�����J��
    data = np.loadtxt(csvname,delimiter=',',dtype=np.float32)

    for line in range(0,19) :
        lines = (line) * 3
        for column in range(0,19) :
            columns = (column) * 3
            add9points=0
            for i in range(3) :
                for j in range(3):
                    add9points = add9points + data[lines+i][columns+j]
            add9points_map[line][column]=add9points
    return add9points_map





# ##�W���̍s����쐬  'intensive_map.csv'
# intensive_map = np.zeros([20, 20])#�W���̍s��
# for line in tqdm(range(1,21)) : #�s����(�f�B���N�g������)
#     for column in range(1,21) : #�񂲂�(�f�B���N�g������)
#         list1 = glob.glob('./CSV/NEW'+str(line)+"-"+str(column)+'/*')#�e�|�C���g�̂Q�b�Ԃ̃f�[�^(10�t���[��)�����X�g��
#         sum9points=0#9�|�C���g���W�񂵂��l�̏�����
#         for i in range(len(list1)) :#���̃��X�g��擪���珇�ɏ���
#             sum9points=sum9points+Intensive(list1[i],line,column)#10�t���[�����̍��v���v�Z
#         ave9points=(sum9points+1.0)/10.0                                #���ς����߁A���̃|�C���g�̒l�Ƃ���
#         intensive_map[line-1][column-1] = ave9points                    #�W���̍s��ɑ��
# aveintensive_map = np.average(intensive_map)#�W���̑S�̂̕���
# np.savetxt('intensive_map.csv',intensive_map,delimiter=',', fmt='%2f')
#
# ##�W���̕��ς���̌덷�����̍s��   'intensive_diff.csv'
# intensive_diff = np.zeros([20, 20])#�e�|�C���g�̏C�������̍s��
# for line in tqdm(range(20)) : #�s����(�f�B���N�g������)
#     for column in range(20) : #�񂲂�(�f�B���N�g������)
#         intensive_diff[line][column] = aveintensive_map / intensive_map[line][column] #�덷�������v�Z
# np.savetxt('intensive_diff.csv',intensive_diff,delimiter=',', fmt='%2f')

##�␳�������鑤�̈ȑO�v�������f�[�^��(60*60)��20*20�ɏW�񂵂��s��
# csvnum = 1956
# csvfile = './CSV/NEW' + str(csvnum)
# if os.path.isdir('./CSV/Intensive'+ str(csvnum)) == False:
#     os.mkdir('./CSV/Intensive'+ str(csvnum))
# savefile = './CSV/Intensive'+ str(csvnum)
# list1 = glob.glob(csvfile+'/*')
# data_map = np.zeros([20, 20])#�ȑO�v�������f�[�^(60*60)���W���̍s��
# for i in tqdm(range(len(list1))) :
#     name = list(list1[i])#CSP011600000*������؂���
#     del name[0:14]
#     name = "".join(name)
#     data_map = Intensive_data(list1[i])#�ȑO�v�������f�[�^��(60*60)��20*20�ɏW��
#     np.savetxt(savefile+'/'+str(name),data_map,delimiter=',', fmt='%2f')



path_list = glob.glob('./New_CSV/*')#'./CSV/jyu', './CSV/kdo',...
name_list = os.listdir('./New_CSV')#'jyu', 'kdo',...

if os.path.isdir('./Intensive_CSV') == False:
    os.mkdir('./Intensive_CSV')

for i in range(len(name_list)) :

    if os.path.isdir('./Intensive_CSV/'+name_list[i]) == False:
        os.mkdir('./Intensive_CSV/'+name_list[i])

    numpath_list = glob.glob('./New_CSV/'+name_list[i]+'/*')#'./CSV/jyu/1', './CSV/jyu/2',
    numname_list = os.listdir('./New_CSV/'+name_list[i])#'1', '2', '3',

    for j in range(len(numname_list)) :

        if os.path.isdir('./Intensive_CSV/'+name_list[i]+'/'+numname_list[j]) == False:
            os.mkdir('./Intensive_CSV/'+name_list[i]+'/'+numname_list[j])


        datapath_list = glob.glob('./New_CSV/'+name_list[i]+'/'+numname_list[j]+'/*')#'./CSV/jyu/1/CSP1427000000.csv', './CSV/jyu/1/CSP1427000001.csv',
        dataname_list = os.listdir('./New_CSV/'+name_list[i]+'/'+numname_list[j])    #'CSP1427000000.csv', 'CSP1427000001.csv',

        data_map = np.zeros([20, 20])#�ȑO�v�������f�[�^(60*60)���W���̍s��
        for k in range(len(dataname_list)) :
            data_name = dataname_list[k][:-4]

            data_map = Intensive_data(datapath_list[k])#�ȑO�v�������f�[�^��(60*60)��20*20�ɏW��

            save_path = datapath_list[k].replace('New_', 'Intensive_')

            np.savetxt(save_path,data_map,delimiter=',', fmt='%2f')
