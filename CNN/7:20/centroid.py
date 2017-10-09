#!/usr/bin/env python
#-*- coding:utf-8 -*-
#重心を求める
#連結されたデータを上から一行づつ読み込んでlines行(1フレーム)ごとに
#全体の重心,片足づつの重心を求めて記録、保存


import glob
import os
import os.path
import csv
from tqdm import tqdm

def centroid(csvname,lines):
	datafile = csvname
	#対象のファイルと整形後のファイルを開く
	file = open(datafile,"r")
	dataReader = csv.reader(file)

	col = 1
	addx = 0
	addy = 0
	addz = 0
	Laddx = 0
	Laddy = 0
	Laddz = 0
	Raddx = 0
	Raddy = 0
	Raddz = 0

	count = 0
	count2=0
	for row in dataReader:

		for i in range(lines):

			addx = addx + i*float(row[i])
			addy = addy + col*float(row[i])
			addz = addz + float(row[i])
			if i < lines/2+1:
				Laddx = Laddx + i*float(row[i])
				Laddy = Laddy + col*float(row[i])
				Laddz = Laddz + float(row[i])
			else:
				Raddx = Raddx + i*float(row[i])
				Raddy = Raddy + col*float(row[i])
				Raddz = Raddz + float(row[i])

		if col%lines == 0:


			if addx or addy or addz != 0:
				xg=addx/lines*lines/addz
				yg=addy/lines*lines/addz
			else:
				xg=0
				yg=0

			if Laddx or Laddy or Laddz != 0:
				Lxg=Laddx/lines*lines/Laddz
				Lyg=Laddy/lines*lines/Laddz
			else:
				Lxg=0
				Lyg=0

			if Raddx or Raddy or Raddz != 0:
				Rxg=Raddx/lines*lines/Raddz
				Ryg=Raddy/lines*lines/Raddz
			else:
				Rxg=0
				Ryg=0

			file_out.write(str(xg)+','+str(yg)+','+str(Lxg)+','+str(Lyg)+','+str(Rxg)+','+str(Ryg)+'\n')
			addx = 0
			addy = 0
			addz = 0
			Laddx = 0
			Laddy = 0
			Laddz = 0
			Raddx = 0
			Raddy = 0
			Raddz = 0
			col = 0
			xg = 0
			yg =0
			Lxg=0
			Lyg=0
			Rxg=0
			Ryg=0

		col = col + 1
	#開いたものを閉じる
	file.close()

path_list = glob.glob('./Cab_CSV/*')#'./CSV/jyu', './CSV/kdo',...
name_list = os.listdir('./Cab_CSV')#'jyu', 'kdo',...
for i in range(len(name_list)) :
	numpath_list = glob.glob('./Cab_CSV/'+name_list[i]+'/*')#'./CSV/jyu/1', './CSV/jyu/2',
	numname_list = os.listdir('./Cab_CSV/'+name_list[i])#'1', '2', '3',
	for j in range(len(numname_list)) :
		allcsv_path = numpath_list[j]+'/allcsv.csv'#整形後のcsv名、決定
		centcsv_path = numpath_list[j]+'/centcsv.csv'#整形後のcsv名、決定
		file_out = open(centcsv_path,"w")
		centroid(allcsv_path,20)
		file_out.close()

path_list = glob.glob('./New_CSV/*')#'./CSV/jyu', './CSV/kdo',...
name_list = os.listdir('./New_CSV')#'jyu', 'kdo',...
for i in range(len(name_list)) :
	numpath_list = glob.glob('./New_CSV/'+name_list[i]+'/*')#'./CSV/jyu/1', './CSV/jyu/2',
	numname_list = os.listdir('./New_CSV/'+name_list[i])#'1', '2', '3',
	for j in range(len(numname_list)) :
		allcsv_path = numpath_list[j]+'/allcsv.csv'#整形後のcsv名、決定
		centcsv_path = numpath_list[j]+'/centcsv.csv'#整形後のcsv名、決定
		file_out = open(centcsv_path,"w")
		centroid(allcsv_path,60)
		file_out.close()
