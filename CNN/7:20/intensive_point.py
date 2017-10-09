#!/usr/bin/env python
#-*- coding:utf-8 -*-
#数値のみが入った60*60から9ポイントづつを集約して20*20のデータに変換
#-----注意-----
#全体の平均からの割合で修正しているが、隅のきちんと取れていない値に引っ張られる可能性あり
#他にいい修正方法あるかも
#------------

import glob
import os
import os.path
import csv
import numpy as np
from tqdm import tqdm


##現在見ている行列から重りを載せた9ポイントを集約
#重りを載せていないところは「考慮していない」
# def Intensive(csvname,line,column):
#     datafile = csvname
#     #対象のファイルと整形後のファイルを開く
#     file_in = np.loadtxt(csvname,delimiter=',',dtype=np.float32)
#     line = (line-1) * 3
#     column = (column-1) * 3
#     add9points=0
#     for i in range(3) :
#         for j in range(3):
#             add9points = add9points + file_in[line+i][column+j]
#
#     # print add9points
#     return add9points#重りを載せた9ポイントの値を返す

##以前計測したデータを9ポイントづつ集約
def Intensive_data(csvname):
    add9points_map = np.zeros([20, 20])
    datafile = csvname
    #対象のファイルと整形後のファイルを開く
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





# ##集約後の行列を作成  'intensive_map.csv'
# intensive_map = np.zeros([20, 20])#集約後の行列
# for line in tqdm(range(1,21)) : #行ごと(ディレクトリ名の)
#     for column in range(1,21) : #列ごと(ディレクトリ名の)
#         list1 = glob.glob('./CSV/NEW'+str(line)+"-"+str(column)+'/*')#各ポイントの２秒間のデータ(10フレーム)をリストに
#         sum9points=0#9ポイントを集約した値の初期化
#         for i in range(len(list1)) :#そのリストを先頭から順に処理
#             sum9points=sum9points+Intensive(list1[i],line,column)#10フレーム分の合計を計算
#         ave9points=(sum9points+1.0)/10.0                                #平均を求め、そのポイントの値とする
#         intensive_map[line-1][column-1] = ave9points                    #集約後の行列に代入
# aveintensive_map = np.average(intensive_map)#集約後の全体の平均
# np.savetxt('intensive_map.csv',intensive_map,delimiter=',', fmt='%2f')
#
# ##集約後の平均からの誤差割合の行列   'intensive_diff.csv'
# intensive_diff = np.zeros([20, 20])#各ポイントの修正割合の行列
# for line in tqdm(range(20)) : #行ごと(ディレクトリ名の)
#     for column in range(20) : #列ごと(ディレクトリ名の)
#         intensive_diff[line][column] = aveintensive_map / intensive_map[line][column] #誤差割合を計算
# np.savetxt('intensive_diff.csv',intensive_diff,delimiter=',', fmt='%2f')

##補正をかける側の以前計測したデータを(60*60)を20*20に集約した行列
# csvnum = 1956
# csvfile = './CSV/NEW' + str(csvnum)
# if os.path.isdir('./CSV/Intensive'+ str(csvnum)) == False:
#     os.mkdir('./CSV/Intensive'+ str(csvnum))
# savefile = './CSV/Intensive'+ str(csvnum)
# list1 = glob.glob(csvfile+'/*')
# data_map = np.zeros([20, 20])#以前計測したデータ(60*60)を集約後の行列
# for i in tqdm(range(len(list1))) :
#     name = list(list1[i])#CSP011600000*部分を切り取り
#     del name[0:14]
#     name = "".join(name)
#     data_map = Intensive_data(list1[i])#以前計測したデータを(60*60)を20*20に集約
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

        data_map = np.zeros([20, 20])#以前計測したデータ(60*60)を集約後の行列
        for k in range(len(dataname_list)) :
            data_name = dataname_list[k][:-4]

            data_map = Intensive_data(datapath_list[k])#以前計測したデータを(60*60)を20*20に集約

            save_path = datapath_list[k].replace('New_', 'Intensive_')

            np.savetxt(save_path,data_map,delimiter=',', fmt='%2f')
