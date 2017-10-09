#!/usr/bin/env python
#-*- coding:utf-8 -*-
#いらない部分の除去と各binごとのヒストグラムを求め描画

import glob
import os, commands
import os.path
import csv
import numpy as np
from scipy import stats
from tqdm import tqdm
import matplotlib.pyplot as plt
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")#.DS_Storeファイルを取り除く

class HistogramsClass:

    """いらない部分の除去と各binごとのヒストグラムを求め描画"""

    def histograms(self):

        #平均値で集約したデータのヒストグラムを求める
        mean_map = np.loadtxt('./mean_map.csv',delimiter=',')
        #外周と中央の縁部分を取り除く
        mean_map = np.delete(mean_map, 0, 0)#行削除
        mean_map = np.delete(mean_map, -1, 0)#行削除
        mean_map = np.delete(mean_map, 7, 1)#列削除
        mean_map = np.delete(mean_map, 0, 1)#列削除
        mean_map = np.delete(mean_map, -1, 1)#列削除


        mean_list=mean_map.reshape(-1,)#一次元配列に
        i=mean_list.nonzero()#影響を及ぼさない為に0を取り除く

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

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mean_list, bins=1000)
        plt.savefig('./mean_1000.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mean_list, bins=500)
        plt.savefig('./mean_500.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mean_list, bins=100)
        plt.savefig('./mean_100.png')


        #中央値で集約したデータのヒストグラムを求める
        med_map = np.loadtxt('./med_map.csv',delimiter=',')
        #外周と中央の縁部分を取り除く
        med_map = np.delete(med_map, 0, 0)#行削除
        med_map = np.delete(med_map, -1, 0)#行削除
        med_map = np.delete(med_map, 7, 1)#列削除
        med_map = np.delete(med_map, 0, 1)#列削除
        med_map = np.delete(med_map, -1, 1)#列削除

        med_list = med_map.reshape(-1,)#一次元配列に
        i = med_list.nonzero()#影響を及ぼさない為に0を取り除く

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

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(med_list, bins=1000)
        plt.savefig('./med_1000.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(med_list, bins=500)
        plt.savefig('./med_500.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(med_list, bins=100)
        plt.savefig('./med_100.png')


        #最頻値で集約したデータのヒストグラムを求める
        mod_map = np.loadtxt('./mode_map.csv',delimiter=',')
        #外周と中央の縁部分を取り除く
        mod_map = np.delete(mod_map, 0, 0)#行削除
        mod_map = np.delete(mod_map, -1, 0)#行削除
        mod_map = np.delete(mod_map, 7, 1)#列削除
        mod_map = np.delete(mod_map, 0, 1)#列削除
        mod_map = np.delete(mod_map, -1, 1)#列削除


        mod_list = mod_map.reshape(-1,)#一次元配列に
        i = mod_list.nonzero()#影響を及ぼさない為に0を取り除く

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

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mod_list, bins=1000)
        plt.savefig('./mod_1000.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mod_list, bins=500)
        plt.savefig('./mod_500.png')

        #ヒストグラムの描画
        fig = plt.figure()
        plt.xlim([0,1000])
        plt.hist(mod_list, bins=100)
        plt.savefig('./mod_100.png')

HisCla = HistogramsClass()
#いらない部分の除去と各binごとのヒストグラムを求め描画
HisCla.histograms()
