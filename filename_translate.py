#初期設定
from googletrans import Translator
import sys
import os
import glob
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

translator = Translator()

#開始。
def click2():
    subdir = './' + sub.get()
    #選択したファイル名を翻訳
    if mode.get() == 0:
        for i in paths:
            #翻訳するファイルがあるディレクトリに移動
            os.chdir(os.path.dirname(i))
            #ファイル名だけ抽出してファイル名と拡張子を分離
            fileNameExt = os.path.basename(i)
            fileName, fileExt = os.path.splitext(fileNameExt)
            #ファイル名を翻訳
            translated = translator.translate(fileName, dest="ja").text
            #翻訳したファイル名と拡張子を結合
            transFile = translated + fileExt
            #もしチェックボックスにチェックされていたら
            if copy.get():
                #指定されたサブディレクトリが無ければ作成
                if not os.path.exists(subdir):
                    os.mkdir(subdir)
                #ファイルをコピー
                shutil.copy(fileNameExt, subdir + '/' + transFile)
            #されていなければファイル名を変更
            else:
                shutil.move(fileNameExt, transFile)
    
    #選択したディレクトリ内のファイル名を翻訳
    elif mode.get() == 1:
        #選択されたディレクトリに移動
        os.chdir(paths)
        #ディレクト内のすべてのファイル名を取得
        files = glob.glob('./*')
        print(files)
        #もしチェックボックスにチェックが入っていて、指定されたサブディレクトリが無ければ作成
        if copy.get() and not os.path.exists(subdir):
            os.mkdir(subdir)
        #取得したファイルを順番に処理
        for i in files:
            #ファイル名だけ抽出してファイル名と拡張子を分離
            fileNameExt = os.path.basename(i)
            fileName, fileExt = os.path.splitext(fileNameExt)
            #ファイル名を翻訳
            translated = translator.translate(fileName, dest="ja").text
            #翻訳したファイル名と拡張子を結合
            transFile = translated + fileExt
            #もしチェックボックスにチェックされていたらファイルをコピー
            if copy.get():
                shutil.copy(fileNameExt, subdir + '/' + transFile)
            #されていなければファイル名を変更
            else:
                shutil.move(fileNameExt, transFile)
    
    #選択したディレクトリ名を翻訳
    elif mode.get() == 2:
        #翻訳するディレクトリまでのパスと翻訳するディレクトリ名を分離
        dirHead, dirTail = os.path.split(paths)
        #翻訳するディレクトリまでのパスに移動
        os.chdir(dirHead)
        #ディレクトリ名を翻訳
        translated = translator.translate(dirTail, dest='ja').text
        #ディレクトリ名を変更
        shutil.move(dirTail, translated)
    messagebox.showinfo(u'Successful!','処理が完了しました。')

#終了。



#ファイル選択
def click1():
    global paths
    if mode.get() == 0:
        paths = filedialog.askopenfilenames(initialdir=os.path.abspath(os.path.dirname(__file__)))
    else:
        paths = filedialog.askdirectory(initialdir=os.path.abspath(os.path.dirname(__file__)))
    print(paths)

#GUI

#メインウィンドウ
root = tk.Tk()
root.title(u'FileName Translate')
root.geometry('640x480')

#ラベル1
modetitle = tk.Label(text=u'翻訳モード')
modetitle.pack()
#ラジオボタン（翻訳モード選択）
mode = tk.IntVar()
mode.set(0)
mode1 = tk.Radiobutton(root,text=u'選択したファイル名を翻訳',value=0,variable=mode)
mode1.pack()
mode2 = tk.Radiobutton(root,text=u'選択したディレクトリ内のファイル名を翻訳',value=1,variable=mode)
mode2.pack()
mode3 = tk.Radiobutton(root,text=u'選択したディレクトリ名を翻訳',value=2,variable=mode)
mode3.pack()

#ラベル2
dialogtitle = tk.Label(text=u'パス')
dialogtitle.pack()
#ボタン（ファイル選択ダイアログを開く）
dialog = tk.Button(root,text='参照',command=click1)
dialog.pack()

#チェックボックス1（ファイルをコピーするか否か）
copy = tk.BooleanVar()
copy.set(True)
copy0 = tk.Checkbutton(root,text=u'ファイルをサブディレクトリにコピーして、そのファイルを翻訳する。',variable=copy)
copy0.pack()

#ラベル3
subtitle = tk.Label(text=u'サブディレクトリ名')
subtitle.pack()
#テキストボックス2（サブディレクトリ名を指定）
sub = tk.Entry(root)
sub.insert(tk.END,'translated')
sub.pack()

#ボタン4（処理）
submit = tk.Button(root,text='処理開始',command=click2)
submit.pack()

root.mainloop()