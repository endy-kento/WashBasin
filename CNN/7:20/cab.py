#!/usr/bin/env python
#-*- coding:utf-8 -*-
#ここで補正を行う
#事前に計測し20*20に集約されたデータに補正のための行列を使って「一枚づつ」補正を行う
#その後、補正されたデータを連結する

import glob
import os
import os.path
import csv
import numpy as np
from tqdm import tqdm

##データの補正
def Calibration(csvname):
    datafile = csvname
    #対象のデータと補正用の行列を開く
    data = np.loadtxt(csvname,delimiter=',',dtype=np.float32)
    diff = np.loadtxt('./intensive_diff.csv',delimiter=',',dtype=np.float32)
    return diff * data #掛け合わせることによって補正

##一括でcsvを結合する
def csvmerge(csvname):
    datafile = csvname
    file = open(datafile,"r")
    #統合用のcsvに書き加えていく
    line_list = file.readlines()
    for number,line in enumerate(line_list):
            file_out.write(line)
    #開いたものを閉じる
    file.close()

##補正後のデータを保存
# csvnum = 1956
# csvfile = './CSV/Intensive' + str(csvnum)
# #保存用ディレクトリがなければ作成
# if os.path.isdir('./CSV/Cab'+ str(csvnum)) == False:
#     os.mkdir('./CSV/Cab'+ str(csvnum))
# savefile = './CSV/Cab'+ str(csvnum)
#
# list1 = glob.glob(csvfile+'/*')
# cab_map = np.zeros([20, 20])
# for i in tqdm(range(len(list1))) :
#
#     #CSP011600000*部分を切り取り
#     name = list(list1[i])
#     del name[0:20]
#     name = "".join(name)
#
#     cab_map = Calibration(list1[i])
#     np.savetxt(savefile+'/'+str(name),cab_map,delimiter=',', fmt='%2f')


path_list = glob.glob('./Intensive_CSV/*')#'./CSV/jyu', './CSV/kdo',...
name_list = os.listdir('./Intensive_CSV')#'jyu', 'kdo',...

if os.path.isdir('./Cab_CSV') == False:
    os.mkdir('./Cab_CSV')

for i in range(len(name_list)) :

    if os.path.isdir('./Cab_CSV/'+name_list[i]) == False:
        os.mkdir('./Cab_CSV/'+name_list[i])

    numpath_list = glob.glob('./Intensive_CSV/'+name_list[i]+'/*')#'./CSV/jyu/1', './CSV/jyu/2',
    numname_list = os.listdir('./Intensive_CSV/'+name_list[i])#'1', '2', '3',

    for j in range(len(numname_list)) :

        if os.path.isdir('./Cab_CSV/'+name_list[i]+'/'+numname_list[j]) == False:
            os.mkdir('./Cab_CSV/'+name_list[i]+'/'+numname_list[j])

        datapath_list = glob.glob('./Intensive_CSV/'+name_list[i]+'/'+numname_list[j]+'/*')#'./CSV/jyu/1/CSP1427000000.csv', './CSV/jyu/1/CSP1427000001.csv',
        dataname_list = os.listdir('./Intensive_CSV/'+name_list[i]+'/'+numname_list[j])    #'CSP1427000000.csv', 'CSP1427000001.csv',

        cab_map = np.zeros([20, 20])
        for k in range(len(dataname_list)) :
            data_name = dataname_list[k][:-4]
            cab_map = Calibration(datapath_list[k])
            save_path = datapath_list[k].replace('Intensive_', 'Cab_')
            np.savetxt(save_path,cab_map,delimiter=',', fmt='%2f')


path_list = glob.glob('./Cab_CSV/*')#'./CSV/jyu', './CSV/kdo',...
name_list = os.listdir('./Cab_CSV')#'jyu', 'kdo',...

for i in range(len(name_list)) :
    numpath_list = glob.glob('./Cab_CSV/'+name_list[i]+'/*')#'./CSV/jyu/1', './CSV/jyu/2',
    numname_list = os.listdir('./Cab_CSV/'+name_list[i])#'1', '2', '3',


    for j in range(len(numname_list)) :

        datapath_list = glob.glob('./Cab_CSV/'+name_list[i]+'/'+numname_list[j]+'/*')#'./CSV/jyu/1/CSP1427000000.csv', './CSV/jyu/1/CSP1427000001.csv',
        dataname_list = os.listdir('./Cab_CSV/'+name_list[i]+'/'+numname_list[j])    #'CSP1427000000.csv', 'CSP1427000001.csv',

        allcsv_path = numpath_list[j]+'/allcsv.csv'#整形後のcsv名、決定
        file_out = open(allcsv_path,"w")
        for k in range(len(dataname_list)) :
            csvmerge(datapath_list[k])
        file_out.close()

path_list = glob.glob('./New_CSV/*')#'./CSV/jyu', './CSV/kdo',...
name_list = os.listdir('./New_CSV')#'jyu', 'kdo',...

for i in range(len(name_list)) :
    numpath_list = glob.glob('./New_CSV/'+name_list[i]+'/*')#'./CSV/jyu/1', './CSV/jyu/2',
    numname_list = os.listdir('./New_CSV/'+name_list[i])#'1', '2', '3',


    for j in range(len(numname_list)) :

        datapath_list = glob.glob('./New_CSV/'+name_list[i]+'/'+numname_list[j]+'/*')#'./CSV/jyu/1/CSP1427000000.csv', './CSV/jyu/1/CSP1427000001.csv',
        dataname_list = os.listdir('./New_CSV/'+name_list[i]+'/'+numname_list[j])    #'CSP1427000000.csv', 'CSP1427000001.csv',

        allcsv_path = numpath_list[j]+'/allcsv.csv'#整形後のcsv名、決定
        file_out = open(allcsv_path,"w")
        for k in range(len(dataname_list)) :
            csvmerge(datapath_list[k])
        file_out.close()
##補正されたデータを一括連結
# save_path = './CSV/Cab'+str(csvnum)+'/allcsv.csv'#整形後のcsv名、決定
# list2 = glob.glob('./CSV/Cab'+str(csvnum)+'/*')
# file_out = open(savefile,"w")               #結合後のcsv作成
# for i in tqdm(range(len(list2))) :          #整形後のディレクトリ内のファイル数分、回転
#     csvmerge(list2[i])                      #一括でcsvを結合
# file_out.close()                            #整形後のcsvを閉じる
