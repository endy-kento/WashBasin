#!/usr/bin/env python
#-*- coding:utf-8 -*-
#cleaning.pyをクラス化したもの。
#生データ(./CSV/* 以下)の先頭部分と最後の部分を取り除く
#60*60だけのcsvデータを(./CSV/*gp 以下)保存
#引数に第一 : 元のディレクトリ名 第二 : 保存用のディレクトリ名
#ex) python Cleaning.py 111.1 111.1gp

import glob
import os
import commands
import sys

commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")#.DS_Storeファイルを取り除く
args = sys.argv


class CleaningClass:

    """生データをいらない部分を取り除いて整形する"""

    def cleaning(self,data_path,save_path):
        #対象のファイルと整形後のファイルを開く
        file_in = open(data_path,"r")
        file_out = open(save_path,"w")
        #読み込んで、先頭と最後のいらない部分を削除
        line_list = file_in.readlines()
        del line_list[0:3]
        del line_list[-1]
        #それ以外を書き込み
        for number,line in enumerate(line_list):
                file_out.write(line)
        #開いたものを閉じる
        file_in.close()
        file_out.close()


CleCla = CleaningClass()
DirPath_list = glob.glob('./CSV/'+str(args[1])+'/*')#'./CSV/111.1/1-1',...

if os.path.isdir('./CSV/'+str(args[2])) == False:#なければ保存用のディレクトリ作成
    os.mkdir('./CSV/'+str(args[2]))

for DirPath in DirPath_list:
    if os.path.isdir(DirPath.replace(str(args[1]),str(args[2]))) == False:#なければ保存用のディレクトリ作成
        os.mkdir(DirPath.replace(str(args[1]),str(args[2])))

    CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/111.1/1-1/CSP1956000000.csv',...
    for CsvPath in CsvPath_list:
        CleCla.cleaning(CsvPath,CsvPath.replace(str(args[1]),str(args[2])))#生データのいらない部分を削除して整形
