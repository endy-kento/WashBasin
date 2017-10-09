#!/usr/bin/env python
#-*- coding:utf-8 -*-
#[行-列]の名前で保存された1.5*1.5の面積のデータのいらない先頭部分と末尾部分を取り除く
#取り除いたデータは「全連結させず」一枚づつ保存
#-----注意-------
#ここで扱うデータは単位面積ごとに重さを乗せているが、csvの内容は60*60である
#このプログラムで、いらない部分を取り除き、[intensive_point.py]で20*20に集約する

import glob
import os
import os.path

##先頭と最後のいらない部分を削除
def deleteSecureNode(data_path,data_name):

    save_path = list(data_path)
    save_path.insert(2,"New_")
    save_path = "".join(save_path)


    #対象のファイルと整形後のファイルを開く
    file_in = open(data_path,"r")
    file_out = open(save_path,"w")
    #読み込んで、先頭と最後のいらない部分を削除
    line_list = file_in.readlines()
    del line_list[0:3]
    del line_list[-1]
    #それ以外を書き込み
    for number,line in enumerate(line_list):
            file_out.write(line)
    #開いたものを閉じる
    file_in.close()
    file_out.close()

#####################################################

path_list = glob.glob('./CSV/*')#'./CSV/jyu', './CSV/kdo',...
name_list = os.listdir('./CSV')#'jyu', 'kdo',...

if os.path.isdir('./New_CSV') == False:
    os.mkdir('./New_CSV')

for i in range(len(name_list)) :

    if os.path.isdir('./New_CSV/'+name_list[i]) == False:
        os.mkdir('./New_CSV/'+name_list[i])

    numpath_list = glob.glob(path_list[i]+'/*')#'./CSV/jyu/1', './CSV/jyu/2',
    numname_list = os.listdir(path_list[i])#'1', '2', '3',

    for j in range(len(numname_list)) :

        if os.path.isdir('./New_CSV/'+name_list[i]+'/'+numname_list[j]) == False:
            os.mkdir('./New_CSV/'+name_list[i]+'/'+numname_list[j])

        datapath_list = glob.glob(numpath_list[j]+'/*')#'./CSV/jyu/1/CSP1427000000.csv', './CSV/jyu/1/CSP1427000001.csv',
        dataname_list = os.listdir(numpath_list[j])#'CSP1427000000.csv', 'CSP1427000001.csv',

        for k in range(len(dataname_list)) :
            data_name = dataname_list[k][:-4]#'CSP1427000000','CSP1427000001',
            deleteSecureNode(datapath_list[k],data_name)
