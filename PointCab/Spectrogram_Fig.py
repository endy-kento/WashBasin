#!/usr/bin/env python
#-*- coding:utf-8 -*-
#生の周波数成分と、iirでのハイパスフィルタを通した周波数成分も出力可能

from IIRFilter import IIRFilter
import glob
import os, commands
import os.path
from tqdm import tqdm
from scipy import stats
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys
import seaborn as sns
import cv2
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")
np.set_printoptions(threshold=np.inf)
args = sys.argv

class Spectrogram_FigClass:

    """スペクトル解析用の画像を出力"""

    def normalize(self,data,inmin=0,inmax=60,outmin=-1,outmax=1):
        for i in range(len(data)):
            data[i] =  (data[i] - inmin)*(outmax-outmin)/(inmax-inmin)+(outmin)
        return data

    def ommit(self,data,ommit_value):
        print type(data)
        data_list = []
        for d in data:
            if d != ommit_value:
                data_list.append(d)
        return data_list

    def show_specgram(self,data,spec,freqlist,axse,N=64,fs=37,overlap=16):
        fig, ax = plt.subplots()
        heatmap = ax.pcolor(spec.T, cmap=plt.cm.jet)
        freqlist = np.array(freqlist,dtype=np.int16)
        ax.invert_yaxis()
        ax.xaxis.tick_top()
        plt.gca().invert_yaxis()
        plt.yticks(np.arange(0,freqlist.shape[0]-1,20), freqlist[np.arange(0,freqlist.shape[0]-1,20)])

        # hamming = np.hamming(N)
        # pxx, freqs, bins, im = specgram(data, NFFT=N, Fs=fs, noverlap=overlap, window=hamming,cmap='jet')
        # xlabel("time [second]")
        # ylabel("frequency [Hz]")

        plt.savefig(figSavePath+"/Ana_10lpf_spe_"+axse+".png")

        plt.close()


    def getSpec(self,data,fft_window=512,base_window=64,hop_length=32):
        counter = 0
        window_func = np.hamming(base_window)
        input_vector = np.zeros(fft_window,dtype=np.float64)
        spec_buffer = []
        while counter + base_window < len(data):
            base = data[counter:counter+base_window] * window_func
            input_vector[fft_window/2-base_window/2 : fft_window/2 + base_window/2] = base
            X = np.fft.fft(input_vector)
            spectrum = [np.abs(c.real**2 + c.imag**2) for c in X]
            spec_buffer.append(20*np.log10(spectrum[:(int)(fft_window/2)]))
            counter += hop_length
        return (np.array(spec_buffer), np.fft.fftfreq(fft_window, d=1.0/37)[:(int)(fft_window/2)])



if __name__ == "__main__":
    SFC = Spectrogram_FigClass()

    #注意！内容の変更まだ！
    #Row_Motion
    # npyPath_list = glob.glob('./Row_Motion_COG/*.npy')#'./Row_Motion_COG/Dentifrice.npy',...
    # for npyPath in tqdm(npyPath_list):#'./Row_Motion_COG/Dentifrice.npy',...
    #     figSavePath = npyPath.replace('_COG.npy','')#'Row_Motion_COG/Dentifrice'...
    #     if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
    #             os.mkdir(figSavePath)#'./Row_Motion_COG/Dentifrice'...
    #     COGdata = np.load(npyPath)
    #     COGana.plot_COG_analysis(COGdata,figSavePath)


    #注意！内容の変更まだ！
    # Cabed_Motion
    # MotionPath_list = glob.glob('./Cabed_Motion_COG/*/')#'./Cabed_Motion_COG/Dentifrice'...
    # for MotionPath in tqdm(MotionPath_list):#'./Cabed_Motion_COG/Dentifrice'...
    #     npyPath_list = glob.glob(MotionPath+'/*.npy')#'Cabed_Motion_COG/Dentifrice/cabed_all_COG.npy'...
    #     for npyPath in npyPath_list:#'Cabed_Motion_COG/Dentifrice/cabed_all_COG.npy'...
    #         figSavePath = npyPath.replace('cabed_','')#'Cabed_Motion_COG/Dentifrice/all_COG.npy'...
    #         figSavePath = figSavePath.replace('_COG.npy','')#'Cabed_Motion/Dentifrice/all'...
    #         if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
    #                 os.mkdir(figSavePath)#'./Row_Motion_COG/Dentifrice/Heatmap'...
    #         COGdata = np.load(npyPath)
    #         COGana.plot_COG_analysis(COGdata,figSavePath)




    #Cabed_Motion//Dentifrice/ED44
    MotionPath_list = glob.glob('./Cabed_Motion_COG/*/')#'./Cabed_Motion_COG/Dentifrice'...
    for MotionPath in tqdm(MotionPath_list):#'./Cabed_Motion_COG/Dentifrice'...
        EDPath_list = glob.glob(MotionPath+'/ED*')#'Cabed_Motion_COG/Dentifrice/ED44'...
        for EDPath in EDPath_list:#'Cabed_Motion_COG/Dentifrice/ED44'...
            npyPath_list = glob.glob(EDPath+'/*.npy')#'Cabed_Motion_COG/Dentifrice/ED44/cabed_all_COG.npy'...
            for npyPath in npyPath_list:
                figSavePath = npyPath.replace('cabed_','')#'Cabed_Motion_COG/Dentifrice/ED44/all_COG.npy'...
                figSavePath = figSavePath.replace('_COG.npy','')#'Cabed_Motion/Dentifrice/ED44/all'...
                if os.path.isdir(figSavePath) == False:#なければ保存用のディレクトリ作成
                        os.mkdir(figSavePath)#'./Row_Motion_COG/Dentifrice/ED44/all'...
                COGdata = np.load(npyPath)

                for i in range(9):
                    if i == 0:
                       axes = 'X'
                    elif i == 1:
                       axes = 'Y'
                    elif i == 2:
                       axes = 'Z'
                    elif i == 3:
                       axes = 'LX'
                    elif i == 4:
                       axes = 'LY'
                    elif i == 5:
                       axes = 'LZ'
                    elif i == 6:
                       axes = 'RX'
                    elif i == 7:
                       axes = 'RY'
                    elif i == 8:
                       axes = 'RZ'

                    Sample    = SFC.normalize( SFC.ommit( COGdata.T[i] , 0 ) )

                    fs = 37
                    iir = IIRFilter()
                    # iir.hpf(3,fs)#3Hz以下をカット
                    iir.lpf(10,fs)#3Hz以下をカット
                    Sample = iir.iir(Sample)




                    spec,freqlist   = SFC.getSpec(Sample)


                    SFC.show_specgram(Sample,spec,freqlist,axes)
