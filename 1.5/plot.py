#!/usr/bin/env python
#-*- coding:utf-8 -*-
#_mapと名のつくファイルを描画をヒートマップで描画

import glob
import os, commands
import os.path
from tqdm import tqdm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")#.DS_Storeファイルを取り除く

def draw_heatmap(data, row_labels, column_labels,savepath):
    # 描画する
    fig, ax = plt.subplots()
    # heatmap = ax.pcolor(data, cmap=plt.cm.Blues,vmin=0,vmax=10000)
    heatmap = ax.pcolor(data, cmap=plt.cm.Blues)



    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)

    ax.invert_yaxis()
    ax.xaxis.tick_top()

    ax.set_xticklabels(row_labels, minor=False)
    ax.set_yticklabels(column_labels, minor=False)
    fig.colorbar(heatmap )
    plt.title(savepath)
    plt.savefig(savepath)

def readCsv(dirpath):
    files = glob.glob(dirpath)
    buf=[]

    for f in files:
        # print f
        buf.append(np.loadtxt(f,delimiter=','))
    return np.array(buf)



if __name__ == '__main__':
    dirpath = './*_map.csv'#_mapと名のつくファイルを描画
    # dirpath = './mode_map.csv'
    label = np.arange(20)#20*20の目盛り
    data = readCsv(dirpath)
    count = 0
    DirPath_list = glob.glob('./*_map.csv')
    for d in data:
        # draw_heatmap(d,label,label,dirpath.replace('*.csv',str(count)+'.png'))
        draw_heatmap(d,label,label,dirpath.replace('*_map.csv',str(DirPath_list[count])+'.png'))
        count +=1
