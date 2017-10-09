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
        # var_S_map = np.zeros([60, 60])#�W���̍s��̏�����(���U)
        # sd_S_map = np.zeros([60, 60])#�W���̍s��̏�����(�W���΍�)
        # var_M_map = np.zeros([60, 60])#�W���̍s��̏�����(���U)
        # sd_M_map = np.zeros([60, 60])#�W���̍s��̏�����(�W���΍�)
        # var_L_map = np.zeros([60, 60])#�W���̍s��̏�����(���U)
        # sd_L_map = np.zeros([60, 60])#�W���̍s��̏�����(�W���΍�)
        var_jyu_map = np.zeros([60, 60])#�W���̍s��̏�����(���U)
        sd_jyu_map = np.zeros([60, 60])#�W���̍s��̏�����(�W���΍�)


        for line in range(60):
            for column in range(60):

                # #���U
                # var_S_map[line,column] = np.var(S[line,column,:])
                # #�W���΍�
                # sd_S_map[line,column] = np.std(S[line,column,:])
                # #���U
                # var_M_map[line,column] = np.var(M[line,column,:])
                # #�W���΍�
                # sd_M_map[line,column] = np.std(M[line,column,:])
                # #���U
                # var_L_map[line,column] = np.var(L[line,column,:])
                # #�W���΍�
                # sd_L_map[line,column] = np.std(L[line,column,:])
                #���U
                var_jyu_map[line,column] = np.var(jyu[line,column,:])
                #�W���΍�
                sd_jyu_map[line,column] = np.std(jyu[line,column,:])

                if var_jyu_map[line,column] == 0.0:
                    maskSD[line,column] =  1
                if sd_jyu_map[line,column] == 0.0:
                    maskVar[line,column] =  1




        # np.savetxt('var_S_map.csv',var_S_map,delimiter=',')#�W���s���ۑ�(���U)
        # np.savetxt('sd_S_map.csv',sd_S_map,delimiter=',')#�W���s���ۑ�(�W���΍�)
        # np.savetxt('var_M_map.csv',var_M_map,delimiter=',')#�W���s���ۑ�(���U)
        # np.savetxt('sd_M_map.csv',sd_M_map,delimiter=',')#�W���s���ۑ�(�W���΍�)
        # np.savetxt('var_L_map.csv',var_L_map,delimiter=',')#�W���s���ۑ�(���U)
        # np.savetxt('sd_L_map.csv',sd_L_map,delimiter=',')#�W���s���ۑ�(�W���΍�)
        np.savetxt('var_jyu_map.csv',var_jyu_map)#�W���s���ۑ�(���U)
        np.savetxt('sd_jyu_map.csv',sd_jyu_map)#�W���s���ۑ�(�W���΍�)
        np.save('maskSD.npy',maskSD)#�W���s���ۑ�(���U)
        np.save('maskVar.npy',maskVar)#�W���s���ۑ�(�W���΍�)


    def cabed_varSDplot(self):
        # var_S_map = np.zeros([60, 60])#�W���̍s��̏�����(���U)
        # sd_S_map = np.zeros([60, 60])#�W���̍s��̏�����(�W���΍�)
        # var_M_map = np.zeros([60, 60])#�W���̍s��̏�����(���U)
        # sd_M_map = np.zeros([60, 60])#�W���̍s��̏�����(�W���΍�)
        # var_L_map = np.zeros([60, 60])#�W���̍s��̏�����(���U)
        # sd_L_map = np.zeros([60, 60])#�W���̍s��̏�����(�W���΍�)
        var_jyu_4_map = np.zeros([60, 60])#�W���̍s��̏�����(���U)
        sd_jyu_4_map = np.zeros([60, 60])#�W���̍s��̏�����(�W���΍�)
        var_jyu_5_map = np.zeros([60, 60])#�W���̍s��̏�����(���U)
        sd_jyu_5_map = np.zeros([60, 60])#�W���̍s��̏�����(�W���΍�)

        for line in range(60):
            for column in range(60):
                # #���U
                # var_S_map[line,column] = np.var(cabed_S[line,column,:])
                # #�W���΍�
                # sd_S_map[line,column] = np.std(cabed_S[line,column,:])
                # #���U
                # var_M_map[line,column] = np.var(cabed_M[line,column,:])
                # #�W���΍�
                # sd_M_map[line,column] = np.std(cabed_M[line,column,:])
                # #���U
                # var_L_map[line,column] = np.var(cabed_L[line,column,:])
                # #�W���΍�
                # sd_L_map[line,column] = np.std(cabed_L[line,column,:])
                #���U
                var_jyu_4_map[line,column] = np.var(cabed_jyu_4[line,column,:])
                #�W���΍�
                sd_jyu_4_map[line,column] = np.std(cabed_jyu_4[line,column,:])
                #���U
                var_jyu_5_map[line,column] = np.var(cabed_jyu_5[line,column,:])
                #�W���΍�
                sd_jyu_5_map[line,column] = np.std(cabed_jyu_5[line,column,:])

                if var_jyu_4_map[line,column] == 0.0:
                    maskSD_4[line,column] =  1
                if sd_jyu_4_map[line,column] == 0.0:
                    maskVar_4[line,column] =  1
                if var_jyu_5_map[line,column] == 0.0:
                    maskSD_5[line,column] =  1
                if sd_jyu_5_map[line,column] == 0.0:
                    maskVar_5[line,column] =  1

        # np.savetxt('cabed_var_S_map.csv',var_S_map,delimiter=',')#�W���s���ۑ�(���U)
        # np.savetxt('cabed_sd_S_map.csv',sd_S_map,delimiter=',')#�W���s���ۑ�(�W���΍�)
        # np.savetxt('cabed_var_M_map.csv',var_M_map,delimiter=',')#�W���s���ۑ�(���U)
        # np.savetxt('cabed_sd_M_map.csv',sd_M_map,delimiter=',')#�W���s���ۑ�(�W���΍�)
        # np.savetxt('cabed_var_L_map.csv',var_L_map,delimiter=',')#�W���s���ۑ�(���U)
        # np.savetxt('cabed_sd_L_map.csv',sd_L_map,delimiter=',')#�W���s���ۑ�(�W���΍�)
        np.savetxt('cabed_var_jyu_4_map.csv',var_jyu_4_map,delimiter=',')#�W���s���ۑ�(���U)
        np.savetxt('cabed_sd_jyu_4_map.csv',sd_jyu_4_map,delimiter=',')#�W���s���ۑ�(�W���΍�)
        np.savetxt('cabed_var_jyu_5_map.csv',var_jyu_5_map,delimiter=',')#�W���s���ۑ�(���U)
        np.savetxt('cabed_sd_jyu_5_map.csv',sd_jyu_5_map,delimiter=',')#�W���s���ۑ�(�W���΍�)
        np.save('maskSD_4.npy',maskSD_4)#�W���s���ۑ�(���U)
        np.save('maskVar_4.npy',maskVar_4)#�W���s���ۑ�(�W���΍�)
        np.save('maskSD_5.npy',maskSD_5)#�W���s���ۑ�(���U)
        np.save('maskVar_5.npy',maskVar_5)#�W���s���ۑ�(�W���΍�)




VSDP = VarSDplotClass()
VSDP.varSDplot()
VSDP.cabed_varSDplot()
