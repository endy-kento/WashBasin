#!/usr/bin/env python
#-*- coding:utf-8 -*-
#cleaning.pyをクラス化したもの。
#生データの先頭部分と最後の部分を取り除く
#60*60だけのcsvデータに


import glob
import os, commands
import os.path
commands.getoutput("find . -name '.DS_Store' -type f -ls -delete")


class CleaningClass:

    """生データをいらない部分を取り除いて整形する"""

    def cleaning(self,data_path,save_path):
        #対象のファイルと整形後のファイルを開く
        file_in = open(data_path,"r")
        file_out = open(save_path,"w")
        #読み込んで、先頭と最後のいらない部分を削除
        line_list = file_in.readlines()
        del line_list[0:3]#先頭三行
        del line_list[-1]#最後一行
        #それ以外を書き込み
        for number,line in enumerate(line_list):
                file_out.write(line)
        #開いたものを閉じる
        file_in.close()
        file_out.close()

    ##一括でcsvを結合する
    # def csvmerge(csvname):
    #     datafile = csvname
    #     file = open(datafile,"r")
    #     #統合用のcsvに書き加えていく
    #     line_list = file.readlines()
    #     for number,line in enumerate(line_list):
    #             file_out.write(line)
    #     #開いたものを閉じる
    #     file.close()



CleCla = CleaningClass()
DirPath_list = glob.glob('./CSV/Original/*')#'./CSV/Original/1956',...

if os.path.isdir('./CSV/Cleaned') == False:#なければ整形後のディレクトリ作成
    os.mkdir('./CSV/Cleaned')

for DirPath in DirPath_list:#Original内のディレクトリを先頭から順に
    DirSavePath = DirPath.replace('Original', 'Cleaned')
    if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
        os.mkdir(DirSavePath)

    CsvPath_list = glob.glob(DirPath+'/*.csv')#'./CSV/Original/1956/CSP1956000000.csv',...
    for CsvPath in CsvPath_list:

        CsvSavePath = CsvPath.replace('Original', 'Cleaned')#'./CSV/Cleaned/1956/CSP1956000000.csv',...
        CleCla.cleaning(CsvPath,CsvSavePath)#生データのいらない部分を削除して整形
