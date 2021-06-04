from googletrans import Translator
import sys
import os
import glob
import shutil
import tkinter as tk

translator = Translator()

#引数に指定されたディレクトリに移動
os.chdir(sys.argv [1])

#ファイル名を取得
files = glob.glob('./*')
print(files)

#翻訳後ファイルを置くディレクトリを作成
os.mkdir('./translated')

#順番に翻訳していく
for i in files:
    #ファイル名と拡張子だけを取得
    fileNameExt = os.path.basename(i)
    #ファイル名と拡張子を分離
    fileName, fileExt = os.path.splitext(fileNameExt)
    print('翻訳前：' + fileName + fileExt)
    #ファイル名を翻訳
    translated = translator.translate(fileName, dest="ja").text
    #翻訳したファイル名と拡張子を結合
    transFile = translated + fileExt
    print('翻訳後：' + transFile)
    #元のファイル名のファイルを、結合したやつの名前でファイルをコピー
    shutil.copy(i, './translated/' + transFile)
#終了

#GUI
root = tk.Tk()
root.title(u'FileName Translate')
root.geometry('640x480')
Static1 = tk.Label(text=u'test')
Static1.pack()
root.mainloop()