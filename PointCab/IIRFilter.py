# -*- coding:utf-8 -*-
import numpy as np

class IIRFilter:
    """
    IIRフィルタを取り扱うクラス
    """

    def __init__(self):
        """
        初期化．フィルタ係数を定義する
        """
        self.a = np.zeros(3)
        self.b = np.zeros(3)

    def hpf(self,cFreq,fs):
        """
        HPF用の係数を作成する

        cFreq : カットオフ周波数

        fs : サンプリングレート
        """
        fc = np.tan(cFreq * np.pi / fs) / (2 * np.pi)
        denom = 1 + (2 * np.sqrt(2) * np.pi * fc) + 4 * np.pi**2 * fc**2
        self.b[0] = 1.0/denom
        self.b[1] = -2.0/denom
        self.b[2] = 1.0/denom
        self.a[0] = 1.0
        self.a[1] = (8 * np.pi**2 * fc**2 - 2)/denom
        self.a[2] = (1 - (2 * np.sqrt(2) * np.pi * fc) + 4 * np.pi**2 * fc**2) / denom

    def lpf(self,cFreq,fs):
        """
        LPF用の係数を作成する

        cFreq : カットオフ周波数

        fs : サンプリングレート
        """
        fc = np.tan(cFreq * np.pi / fs) / (2 * np.pi)
        denom = 1 + (2 * np.sqrt(2) * np.pi * fc) + 4 * np.pi**2 * fc**2
        self.b[0] = (4 * np.pi**2 * fc**2) / denom
        self.b[1] = (8 * np.pi**2 * fc**2) / denom
        self.b[2] = (4 * np.pi**2 * fc**2) / denom
        self.a[0] = 1.0
        self.a[1] = (8 * np.pi**2 * fc**2 - 2) / denom
        self.a[2] = (1 - (2 * np.sqrt(2) * np.pi * fc) + 4 * np.pi**2 * fc**2) / denom



    def bpf(self,cFreq1,cFreq2,fs):
        """
        BPF用の係数を作成する

        cFreq1 : カットオフ周波数の下限

        cFreq2 : カットオフ周波数の上限

        fs : サンプリングレート
        """
        fc1 = np.tan(cFreq1 * np.pi / fs) / (2 * np.pi)
        fc2 = np.tan(cFreq2 * np.pi / fs) / (2 * np.pi)
        denom = 1 + 2 * np.pi * (fc2 - fc1) + 4 * np.pi**2 * fc1 * fc2
        self.b[0] = (2 * np.pi * (fc2 - fc1)) / denom
        self.b[1] = 0.0
        self.b[2] = - 2 * np.pi * (fc2 - fc1) / denom
        self.a[0] = 1.0
        self.a[1] = (8 * np.pi**2 * fc1 * fc2 - 2) / denom
        self.a[2] = (1.0 - 2 * np.pi * (fc2 - fc1) + 4 * np.pi**2 * fc1 * fc2) / denom

    def bsf(self,cFreq1,cFreq2,fs):
        """
        BSF用の係数を作成する

        cFreq1 : カットオフ周波数の下限

        cFreq2 : カットオフ周波数の上限

        fs : サンプリングレート
        """
        fc1 = np.tan(cFreq1 * np.pi / fs) / (2 * np.pi)
        fc2 = np.tan(cFreq2 * np.pi / fs) / (2 * np.pi)
        denom = 1 + 2 * np.pi * (fc2 - fc1) + 4 * np.pi**2 * fc1 * fc2
        self.b[0] = (4 * np.pi**2 * fc1 * fc2 + 1) / denom
        self.b[1] = (8 * np.pi**2 * fc1 * fc2 - 2) / denom
        self.b[2] = (4 * np.pi**2 * fc1 * fc2 + 1) / denom
        self.a[0] = 1.0
        self.a[1] = (8 * np.pi**2 * fc1 * fc2 - 2) / denom
        self.a[2] = (1 - 2 * np.pi * (fc2 - fc1) + 4 * np.pi**2 * fc1 * fc2) / denom


    def iir(self,data):
        """
        入力データに対してフィルタリングを実行する

        data : 入力データ
        """
        y = np.zeros(len(data))
        Q = len(self.a)-1
        P = len(self.b)-1
        for n in range(len(data)):
            for i in range(0, P + 1):
                if n - i >= 0:
                    y[n] += self.b[i] * data[n - i]
            for j in range(1, Q + 1):
                if n - j >= 0:
                    y[n] -= self.a[j] * y[n - j]
        return y
