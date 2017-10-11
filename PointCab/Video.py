#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tqdm import tqdm
import glob
import os, commands
import os.path
import cv2
import os, commands
import sys
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")

def main():

	if os.path.exists('./Video') == False:
		os.mkdir('./Video')

	Data_DirPath_list = glob.glob('./Image/*')#'./Image/1965',...
	for Data_DirPath in Data_DirPath_list:

		DirSavePath = Data_DirPath.replace('Image','Video')
		if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
			os.mkdir(DirSavePath)

		fourcc = cv2.cv.CV_FOURCC('m','p','4','v')
		video = cv2.VideoWriter(DirSavePath+'/video.mp4', fourcc, 20.0, (640, 480))

		PngPath_list = glob.glob(Data_DirPath+'/*.png')#'./CSV/Convolution/1965/CSP1956000000.csv',...

		for i in range(len(PngPath_list)):
			img = cv2.imread(PngPath_list[i].format(i))
			img = cv2.resize(img, (640,480))
			video.write(img)

	video.release()

if __name__ == '__main__':
    main()
