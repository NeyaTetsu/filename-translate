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
root.geometry('480x190')


#フレーム1（モード選択）
frame1 = tk.Frame(root)
frame1.pack(fill='x')

#ラベル1
modetitle = tk.Label(frame1,text=u'翻訳モード',font=('','20'))
modetitle.pack(side='left',anchor='w',fill='y',ipadx='50')
#ラジオボタン（翻訳モード選択）
mode = tk.IntVar()
mode.set(0)
mode1 = tk.Radiobutton(frame1,text=u'選択したファイル名を翻訳',value=0,variable=mode)
mode1.pack(anchor='nw')
mode2 = tk.Radiobutton(frame1,text=u'選択したディレクトリ内のファイル名を翻訳',value=1,variable=mode)
mode2.pack(anchor='nw')
mode3 = tk.Radiobutton(frame1,text=u'選択したディレクトリ名を翻訳',value=2,variable=mode)
mode3.pack(anchor='nw')


#フレーム2（パス指定）
frame2 = tk.Frame(root)
frame2.pack(fill='x')

#ラベル2
dialogtitle = tk.Label(frame2,text=u'パス',font=('','20'))
dialogtitle.pack(side='left',anchor='w',ipadx='80')
#ボタン（ファイル選択ダイアログを開く）
dialog = tk.Button(frame2,text='参照',command=click1)
dialog.pack(anchor='w',fill='x')


#チェックボックス1（ファイルをコピーするか否か）
copy = tk.BooleanVar()
copy.set(True)
copy0 = tk.Checkbutton(root,text=u'ファイルをサブディレクトリにコピーして、そのファイルを翻訳する。',variable=copy)
copy0.pack()


#フレーム3
frame3 = tk.Frame(root)
frame3.pack(fill='x')

#ラベル3
subtitle = tk.Label(frame3,text=u'サブディレクトリ名',font=('','20'))
subtitle.pack(side='left',anchor='w',ipadx='10')
#テキストボックス2（サブディレクトリ名を指定）
sub = tk.Entry(frame3)
sub.insert(tk.END,'translated')
sub.pack(anchor='w',fill='x')

#ボタン4（処理）
submit = tk.Button(root,text='処理開始',command=click2,font=('','20'))
submit.pack()

root.mainloop()