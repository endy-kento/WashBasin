#coding:utf-8
import wave
from pylab import *

if __name__ == "__main__":
    # WAVE�t�@�C������g�`�f�[�^���擾
    wf = np.load('/Users/endy/WashBasin/PointCab/Cabed_Motion_COG/Dentifrice/cabed_all_COG.npy')
    data = wf.readframes(wf.getnframes())
    data = frombuffer(data, dtype="int16")
    length = float(wf.getnframes()) / wf[0].getframerate()  # �g�`�����i�b�j

    # FFT�̃T���v����
    N = 512

    # FFT�ŗp����n�~���O��
    hammingWindow = np.hamming(N)

    # �X�y�N�g���O������`��
    pxx, freqs, bins, im = specgram(data, NFFT=N, Fs=wf.getframerate(), noverlap=0, window=hammingWindow)
    axis([0, length, 0, wf.getframerate() / 2])
    xlabel("time [second]")
    ylabel("frequency [Hz]")

    show()
