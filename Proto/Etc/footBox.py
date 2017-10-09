#!/usr/bin/env python
#-*- coding:utf-8 -*-
import glob
import os
import os.path
import csv
from tqdm import tqdm

def footBox(csvname):
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
	for row in tqdm(dataReader):
		for i in range(60):
			addx = addx + i*float(row[i])
			addy = addy + col*float(row[i])
			addz = addz + float(row[i])
			if i < 30:
				Laddx = Laddx + i*float(row[i])
				Laddy = Laddy + col*float(row[i])
				Laddz = Laddz + float(row[i])
			else:
				Raddx = Raddx + i*float(row[i])
				Raddy = Raddy + col*float(row[i])
				Raddz = Raddz + float(row[i])

		if col%60 == 0:
			if addx or addy or addz != 0:
				xg=addx/60*60/addz
				yg=addy/60*60/addz
			else:
				xg=0
				yg=0

			if Laddx or Laddy or Laddz != 0:
				Lxg=Laddx/60*60/Laddz
				Lyg=Laddy/60*60/Laddz
			else:
				Lxg=0
				Lyg=0

			if Raddx or Raddy or Raddz != 0:
				Rxg=Raddx/60*60/Raddz
				Ryg=Raddy/60*60/Raddz
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




csvfile = "1956" 
allcsv = './CSV/NEW'+csvfile+'/allcsv.csv'
footBox = './CSV/NEW'+csvfile+'/footBox.csv'
file_out = open(centcsv,"w")
footBox(allcsv)
file_out.close()