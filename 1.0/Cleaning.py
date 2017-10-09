#!/usr/bin/env python
#-*- coding:utf-8 -*-
#cleaning.pyをクラス化したもの。
#生データ(./CSV/Original/ 以下)の先頭部分と最後の部分を取り除く
#60*60だけのcsvデータを(./CSV/Cleaned/ 以下)保存

import glob
import os, commands
import os.path
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")#.DS_Storeファイルを取り除く


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
DirPath_list = glob.glob('./CSV/Original/*')#'./CSV/Original/1-1',...

if os.path.isdir('./CSV/Cleaned') == False:#なければ保存用のディレクトリ作成
    os.mkdir('./CSV/Cleaned')

for DirPath in DirPath_list:
    DirSavePath = DirPath.replace('Original', 'Cleaned')
    if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
        os.mkdir(DirSavePath)

    CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Original/1-1/CSP1956000000.csv',...
    for CsvPath in CsvPath_list:

        CsvSavePath = CsvPath.replace('Original', 'Cleaned')#'./CSV/Cleaned/1-1/CSP1956000000.csv',...
        CleCla.cleaning(CsvPath,CsvSavePath)#生データのいらない部分を削除して整形
