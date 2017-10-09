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

    def cleaning(self,data_path,save_path):#データをいらない部分を取り除いて整形する
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
DirPath_list = glob.glob('./CSV/Original/*')#'./CSV/Original/jyu',...

if os.path.isdir('./CSV/Cleaned') == False:#なければ保存用のディレクトリ作成
    os.mkdir('./CSV/Cleaned')

for DirPath in DirPath_list :#Original内のディレクトリを先頭から順に

    DirSavePath = DirPath.replace('Original', 'Cleaned')
    if os.path.isdir(DirSavePath) == False:#なければ保存用のディレクトリ作成
        os.mkdir(DirSavePath)

    TryNumPath_list = glob.glob(DirPath+'/*')#'./CSV/Original/jyu/1',...

    for TryNumPath in TryNumPath_list :#試行回数分、回転('1', '2', '3',...)

        TryNumSavePath = TryNumPath.replace('Original', 'Cleaned')
        if os.path.isdir(TryNumSavePath) == False:#なければ保存用のディレクトリ作成
            os.mkdir(TryNumSavePath)

        CsvPath_list = glob.glob(TryNumPath+'/*')#'./CSV/Original/jyu/1/CSP1427000000.csv',...

        for CsvPath in CsvPath_list:#フレーム分、回転('CSP1427000000.csv', 'CSP1427000001.csv',...)
            CsvSavePath = CsvPath.replace('Original', 'Cleaned')
            CleCla.cleaning(CsvPath,CsvSavePath)#生データのいらない部分を削除して整形
