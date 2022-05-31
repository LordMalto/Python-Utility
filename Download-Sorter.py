import time
import os
import glob
import shutil
from os import path
filename=glob.glob("C:/Users/malte/Downloads/*")
documents=['.pdf','.docx','.doc','.txt', '.excel', '.odt', '.xslx', '.log', '.accdb']
images=['.jpeg','.jpg','.svg','.png','.PNG']
video=['.mp4', '.webm', '.mov', '.ogg', '.mng', '.wmv', '.rm', '.viv', '.amv']
gif =['.gif', '.gifv']
audio = ['.mp3', '.wav', '.m4a', '.flac', '.mp2', '.ac3', '.amr', '.wma', '.la', '.ape', '.thd', '.wma']
setupFiles=['.exe','.msi', '.iso']
compressedFiles=['.zip', '.rar']
DocumentsLocation='D:/Download-Sort-Py/docs'
mediaLocation='D:/Download-Sort-Py/Media'
imagesLocation='D:/Download-Sort-Py/Media/Images'
videosLocation='D:/Download-Sort-Py/Media/Video'
gifLocation='D:/Download-Sort-Py/Media/GIF'
setupFilesLocation='D:/Download-Sort-Py/.exe'
compressedFilesLocation='D:/Download-Sort-Py/.zip'
audioLocation='D:/Download-Sort-Py/Media/Audio'
othersLocation = 'D:/Download-Sort-Py/Others'
for file in filename:

    if os.path.exists(mediaLocation):
        print()
    else:
        os.mkdir(mediaLocation)
        
    elif os.path.splitext(file)[1] in documents:
        if(path.exists(DocumentsLocation)):
            shutil.move(file,DocumentsLocation)
        else:
            os.mkdir(DocumentsLocation)
            shutil.move(file,DocumentsLocation)
    elif os.path.splitext(file)[1] in images:
        if(path.exists(imagesLocation)):
            shutil.move(file,imagesLocation)
        else:
            os.mkdir(imagesLocation)
            shutil.move(file,imagesLocation)
    elif os.path.splitext(file)[1] in setupFiles:
        if(path.exists(setupFilesLocation)):
            shutil.move(file,setupFilesLocation)
        else:
            os.mkdir(setupFilesLocation)
            shutil.move(file,setupFilesLocation)
    elif os.path.splitext(file)[1] in compressedFiles:
        if(path.exists(compressedFilesLocation)):
            shutil.move(file,compressedFilesLocation)
        else:
            os.mkdir(compressedFilesLocation)
            shutil.move(file,compressedFilesLocation)
    elif os.path.splitext(file)[1] in video:
        if(path.exists(videosLocation)):
            shutil.move(file,videosLocation)
        else:
            os.mkdir(videosLocation)
            shutil.move(file,videosLocation)
    elif os.path.splitext(file)[1] in gif:
        if(path.exists(gifLocation)):
            shutil.move(file,gifLocation)
        else:
            os.mkdir(gifLocation)
            shutil.move(file,gifLocation)
    elif os.path.splitext(file)[1] in audio:
        if(path.exists(audioLocation)):
            shutil.move(file,audioLocation)
        else:
            os.mkdir(audioLocation)
            shutil.move(file,audioLocation)
    elif os.path.splitext(file)[1] in audio:
        if(path.exists(audioLocation)):
            shutil.move(file,audioLocation)
        else:
            os.mkdir(audioLocation)
            shutil.move(file,audioLocation)

    elif os.path.exists(othersLocation):
        shutil.move(file, othersLocation)
    else:
        os.mkdir(othersLocation)
        shutil.move(file, othersLocation)

time.sleep(1200)
os.startfile('C:\\Download-Sorter.py') 
