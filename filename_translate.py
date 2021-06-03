from googletrans import Translator
import sys
import os
import glob
import shutil

translator = Translator()
os.chdir(sys.argv [1])
files = glob.glob('./*')
print(files)
os.mkdir('./translated')
for i in files:
    fileNameExt = os.path.basename(i)
    fileName, fileExt = os.path.splitext(fileNameExt)
    print('翻訳前：' + fileName + fileExt)
    translated = translator.translate(fileName, dest="ja").text
    transFile = translated + fileExt
    print('翻訳後：' + transFile)
    shutil.copy(i, './translated/' + transFile)