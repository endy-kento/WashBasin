#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Convolution_point.pyをクラス化したもの。
#./CSV/Cleaned/ 以下のデータを60*60から30*30に集約し ./CSV/Convolution/ に保存
#そのポイントの2秒間分(10データ)を[平均,中央,最頻,分散,標準偏差]の30*30の5つのcsvファイルを作成

import glob
import os, commands
import os.path
import csv
import numpy as np
from scipy import stats
from tqdm import tqdm
import matplotlib.pyplot as plt
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")#.DS_Storeファイルを取り除く

jyu = np.load("../npyGen/NPY/Person/jyu/1.npy")

S = np.load("../npyGen/NPY/50gp.npy")
M = np.load("../npyGen/NPY/55.5gp.npy")
L = np.load("../npyGen/NPY/62.5gp.npy")
P = np.load("../npyGen/NPY/93.75gp.npy")
N = np.load("../npyGen/NPY/111.1gp.npy")


# cabed_S = np.load("./all_cabed_S_map.npy")
# cabed_M = np.load("./all_cabed_M_map.npy")
# cabed_L = np.load("./all_cabed_L_map.npy")
cabed_jyu_4 = np.load("../PointCab/Conclusion_4/all_cabed_jyu_map.npy")
cabed_jyu_5 = np.load("../PointCab/Conclusion_5/all_cabed_jyu_map.npy")

maskSD = np.tile(0,(60,60))
maskVar = np.tile(0,(60,60))
maskSD_4 = np.tile(0,(60,60))
maskVar_4 = np.tile(0,(60,60))
maskSD_5 = np.tile(0,(60,60))
maskVar_5 = np.tile(0,(60,60))


class VarSDplotClass:


    def varSDplot(self):
        # var_S_map = np.zeros([60, 60])#集約後の行列の初期化(分散)
        # sd_S_map = np.zeros([60, 60])#集約後の行列の初期化(標準偏差)
        # var_M_map = np.zeros([60, 60])#集約後の行列の初期化(分散)
        # sd_M_map = np.zeros([60, 60])#集約後の行列の初期化(標準偏差)
        # var_L_map = np.zeros([60, 60])#集約後の行列の初期化(分散)
        # sd_L_map = np.zeros([60, 60])#集約後の行列の初期化(標準偏差)
        var_jyu_map = np.zeros([60, 60])#集約後の行列の初期化(分散)
        sd_jyu_map = np.zeros([60, 60])#集約後の行列の初期化(標準偏差)


        for line in range(60):
            for column in range(60):

                # #分散
                # var_S_map[line,column] = np.var(S[line,column,:])
                # #標準偏差
                # sd_S_map[line,column] = np.std(S[line,column,:])
                # #分散
                # var_M_map[line,column] = np.var(M[line,column,:])
                # #標準偏差
                # sd_M_map[line,column] = np.std(M[line,column,:])
                # #分散
                # var_L_map[line,column] = np.var(L[line,column,:])
                # #標準偏差
                # sd_L_map[line,column] = np.std(L[line,column,:])
                #分散
                var_jyu_map[line,column] = np.var(jyu[line,column,:])
                #標準偏差
                sd_jyu_map[line,column] = np.std(jyu[line,column,:])

                if var_jyu_map[line,column] == 0.0:
                    maskSD[line,column] =  1
                if sd_jyu_map[line,column] == 0.0:
                    maskVar[line,column] =  1




        # np.savetxt('var_S_map.csv',var_S_map,delimiter=',')#集約後行列を保存(分散)
        # np.savetxt('sd_S_map.csv',sd_S_map,delimiter=',')#集約後行列を保存(標準偏差)
        # np.savetxt('var_M_map.csv',var_M_map,delimiter=',')#集約後行列を保存(分散)
        # np.savetxt('sd_M_map.csv',sd_M_map,delimiter=',')#集約後行列を保存(標準偏差)
        # np.savetxt('var_L_map.csv',var_L_map,delimiter=',')#集約後行列を保存(分散)
        # np.savetxt('sd_L_map.csv',sd_L_map,delimiter=',')#集約後行列を保存(標準偏差)
        np.savetxt('var_jyu_map.csv',var_jyu_map)#集約後行列を保存(分散)
        np.savetxt('sd_jyu_map.csv',sd_jyu_map)#集約後行列を保存(標準偏差)
        np.save('maskSD.npy',maskSD)#集約後行列を保存(分散)
        np.save('maskVar.npy',maskVar)#集約後行列を保存(標準偏差)


    def cabed_varSDplot(self):
        # var_S_map = np.zeros([60, 60])#集約後の行列の初期化(分散)
        # sd_S_map = np.zeros([60, 60])#集約後の行列の初期化(標準偏差)
        # var_M_map = np.zeros([60, 60])#集約後の行列の初期化(分散)
        # sd_M_map = np.zeros([60, 60])#集約後の行列の初期化(標準偏差)
        # var_L_map = np.zeros([60, 60])#集約後の行列の初期化(分散)
        # sd_L_map = np.zeros([60, 60])#集約後の行列の初期化(標準偏差)
        var_jyu_4_map = np.zeros([60, 60])#集約後の行列の初期化(分散)
        sd_jyu_4_map = np.zeros([60, 60])#集約後の行列の初期化(標準偏差)
        var_jyu_5_map = np.zeros([60, 60])#集約後の行列の初期化(分散)
        sd_jyu_5_map = np.zeros([60, 60])#集約後の行列の初期化(標準偏差)

        for line in range(60):
            for column in range(60):
                # #分散
                # var_S_map[line,column] = np.var(cabed_S[line,column,:])
                # #標準偏差
                # sd_S_map[line,column] = np.std(cabed_S[line,column,:])
                # #分散
                # var_M_map[line,column] = np.var(cabed_M[line,column,:])
                # #標準偏差
                # sd_M_map[line,column] = np.std(cabed_M[line,column,:])
                # #分散
                # var_L_map[line,column] = np.var(cabed_L[line,column,:])
                # #標準偏差
                # sd_L_map[line,column] = np.std(cabed_L[line,column,:])
                #分散
                var_jyu_4_map[line,column] = np.var(cabed_jyu_4[line,column,:])
                #標準偏差
                sd_jyu_4_map[line,column] = np.std(cabed_jyu_4[line,column,:])
                #分散
                var_jyu_5_map[line,column] = np.var(cabed_jyu_5[line,column,:])
                #標準偏差
                sd_jyu_5_map[line,column] = np.std(cabed_jyu_5[line,column,:])

                if var_jyu_4_map[line,column] == 0.0:
                    maskSD_4[line,column] =  1
                if sd_jyu_4_map[line,column] == 0.0:
                    maskVar_4[line,column] =  1
                if var_jyu_5_map[line,column] == 0.0:
                    maskSD_5[line,column] =  1
                if sd_jyu_5_map[line,column] == 0.0:
                    maskVar_5[line,column] =  1

        # np.savetxt('cabed_var_S_map.csv',var_S_map,delimiter=',')#集約後行列を保存(分散)
        # np.savetxt('cabed_sd_S_map.csv',sd_S_map,delimiter=',')#集約後行列を保存(標準偏差)
        # np.savetxt('cabed_var_M_map.csv',var_M_map,delimiter=',')#集約後行列を保存(分散)
        # np.savetxt('cabed_sd_M_map.csv',sd_M_map,delimiter=',')#集約後行列を保存(標準偏差)
        # np.savetxt('cabed_var_L_map.csv',var_L_map,delimiter=',')#集約後行列を保存(分散)
        # np.savetxt('cabed_sd_L_map.csv',sd_L_map,delimiter=',')#集約後行列を保存(標準偏差)
        np.savetxt('cabed_var_jyu_4_map.csv',var_jyu_4_map,delimiter=',')#集約後行列を保存(分散)
        np.savetxt('cabed_sd_jyu_4_map.csv',sd_jyu_4_map,delimiter=',')#集約後行列を保存(標準偏差)
        np.savetxt('cabed_var_jyu_5_map.csv',var_jyu_5_map,delimiter=',')#集約後行列を保存(分散)
        np.savetxt('cabed_sd_jyu_5_map.csv',sd_jyu_5_map,delimiter=',')#集約後行列を保存(標準偏差)
        np.save('maskSD_4.npy',maskSD_4)#集約後行列を保存(分散)
        np.save('maskVar_4.npy',maskVar_4)#集約後行列を保存(標準偏差)
        np.save('maskSD_5.npy',maskSD_5)#集約後行列を保存(分散)
        np.save('maskVar_5.npy',maskVar_5)#集約後行列を保存(標準偏差)




VSDP = VarSDplotClass()
VSDP.varSDplot()
VSDP.cabed_varSDplot()
