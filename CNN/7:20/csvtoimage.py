#!/usr/bin/env python
#-*- coding:utf-8 -*-
#連結されたデータとその重心のデータを元に画像を描画、保存
#-----注意-----
#全連結のデータを使用しているので、1フレームごとの行数は、都度「書き換える」必要あり
#------------

import glob
import os, commands
import os.path
import csv
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import shutil
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")



def main(allcsv_path,centcsv_path,image_path,lines,allimage_path,all_count):
    listlist =[]


    #全連結されたデータを引っ張ってくる
    spamReader = csv.reader(open(allcsv_path, 'rb'), delimiter=',')
    matrix = np.loadtxt(allcsv_path,delimiter=',',dtype=np.float32)

    #重心のデータを引っ張ってくる
    centReader = np.loadtxt(centcsv_path,delimiter=',')

    #全結合データが何フレームでできているのか？
    linenum = sum(1 for line in open(allcsv_path))
    count = linenum/lines

    num = 0

    #カラーバーの上限下限を決めるために、全結合のファイル中、最大と最小
    max=np.max(matrix)
    min=np.min(matrix)

    for i in range(0,count):
        #listlistに先頭から一行ずつ貯めていって、20行たまると描画し、保存
        for row in spamReader:
            #listlistに先頭から、格納
            introw = map(string2int,row)
            print
            listlist.append(introw);
            #numはそのフレームの何行目を処理しているか確認するためのもの
            num = num +1

            #20行(1フレーム)ごとに描画、保存
            if (num%lines == 0):
                #カラーバー含め、描画
                src = np.array(listlist)
                plt.tick_params(labelbottom='off')
                plt.tick_params(labelleft='off')
                plt.imshow(src,cmap=plt.cm.cool,clim=(min,max))
                # plt.colorbar()
                # https://matplotlib.org/examples/color/colormaps_reference.html

                #重心のファイルからそれぞれのデータを持ってくる
                X = centReader[i][0]
                Y = centReader[i][1]
                LX = centReader[i][2]
                LY = centReader[i][3]
                RX = centReader[i][4]
                RY = centReader[i][5]

                #両足の重心
                if X or Y != 0:
                    plt.plot(X, Y,marker="*", markersize=10,color="r")
                #左足の重心
                if LX or LY != 0:
                    plt.plot(LX, LY,marker="*", markersize=10,color="g")
                #右足の重心
                if RX or RY != 0:
                    plt.plot(RX, RY,marker="*", markersize=10,color="y")

                #画像を名前をつけて保存
                filename = image_path+'/'+str(i)+".png"

                plt.savefig(filename,bbox_inches='tight',pad_inches=-0.05)
                shutil.copyfile(filename, allimage_path+'/'+str(all_count)+'.png')
                all_count=all_count+1
                #https://mzmttks.blogspot.jp/2012/01/pylab-2.html
                plt.close()

                #listlistを初期化
                listlist = []
                break
    return all_count


def string2int(str):
    if(str):
        return float(str)
    else:
        return 0

if __name__ == '__main__':
    # csvfile = './intensive_map.csv'
    # main(csvfile)
    # csvfile = './intensive_diff.csv'
    # main(csvfile)
    # csvfile = './intensive_sample.csv'
    # main(csvfile)
    # csvfile = './cab_map.csv'
    # main(csvfile)
    # csvnum = 1956
    # csvfile = './CSV/Cab'+str(csvnum)+'/allcsv.csv'
    # main(csvfile)


    allcount=0
    if os.path.isdir('./Image') == False:
        os.mkdir('./Image')
    if os.path.isdir('./testimage') == False:
        os.mkdir('./testimage')

    path_list = glob.glob('./Cab_CSV/*')#'./CSV/jyu', './CSV/kdo',...
    name_list = os.listdir('./Cab_CSV')#'jyu', 'kdo',...
    for i in tqdm(range(len(name_list))) :
        if os.path.isdir('./Image/'+name_list[i]) == False:
            os.mkdir('./Image/'+name_list[i])
        if os.path.isdir('./testimage/'+name_list[i]) == False:
            os.mkdir('./testimage/'+name_list[i])
    	numpath_list = glob.glob('./Cab_CSV/'+name_list[i]+'/*')#'./CSV/jyu/1', './CSV/jyu/2',
    	numname_list = os.listdir('./Cab_CSV/'+name_list[i])#'1', '2', '3',
    	for j in range(len(numname_list)) :
            if os.path.isdir('./Image/'+name_list[i]+'/'+numname_list[j]) == False:
                os.mkdir('./Image/'+name_list[i]+'/'+numname_list[j])
            allcsv_path = numpath_list[j]+'/allcsv.csv'#整形後のcsv名、決定
            centcsv_path = numpath_list[j]+'/centcsv.csv'#整形後のcsv名、決定
            image_path = numpath_list[j].replace('Cab_CSV', 'Image')
            allimage_path = path_list[i].replace('Cab_CSV', 'testimage')
            allcount=main(allcsv_path,centcsv_path,image_path,20,allimage_path,allcount)
        allcount=0

    allcount=0
    path_list = glob.glob('./New_CSV/*')#'./CSV/jyu', './CSV/kdo',...
    name_list = os.listdir('./New_CSV')#'jyu', 'kdo',...
    if os.path.isdir('./testnaiveimage') == False:
        os.mkdir('./testnaiveimage')
    for i in tqdm(range(len(name_list))) :
        if os.path.isdir('./Image/naive_'+name_list[i]) == False:
            os.mkdir('./Image/naive_'+name_list[i])
        if os.path.isdir('./testnaiveimage/naive_'+name_list[i]) == False:
            os.mkdir('./testnaiveimage/naive_'+name_list[i])
    	numpath_list = glob.glob('./New_CSV/'+name_list[i]+'/*')#'./CSV/jyu/1', './CSV/jyu/2',
    	numname_list = os.listdir('./New_CSV/'+name_list[i])#'1', '2', '3',
    	for j in range(len(numname_list)) :
            if os.path.isdir('./Image/naive_'+name_list[i]+'/'+numname_list[j]) == False:
                os.mkdir('./Image/naive_'+name_list[i]+'/'+numname_list[j])
            allcsv_path = numpath_list[j]+'/allcsv.csv'#整形後のcsv名、決定
            centcsv_path = numpath_list[j]+'/centcsv.csv'#整形後のcsv名、決定
            image_path = numpath_list[j].replace('New_CSV/', 'Image/naive_')
            allimage_path = path_list[i].replace('New_CSV/', 'testnaiveimage/naive_')
            allcount=main(allcsv_path,centcsv_path,image_path,60,allimage_path,allcount)

        allcount=0
