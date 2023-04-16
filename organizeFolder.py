# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 02:37:20 2023

@author: moham
"""
import os
import shutil
import argparse
import textwrap

current_dir =os.path.dirname(os.path.realpath(__file__))
out_folder=''
def organiztype(filename,types,folderName):
    if filename.endswith(types): 
        if not os.path.exists(os.path.join(current_dir,out_folder)):
                os.mkdir(os.path.join(current_dir,out_folder))
        if not os.path.exists(os.path.join(current_dir,out_folder, folderName)):
                os.mkdir(os.path.join(current_dir,out_folder, folderName))
        shutil.copy(os.path.join(current_dir, filename),os.path.join(current_dir,out_folder, folderName))
        os.remove(os.path.join(current_dir, filename))
        
def organizAllfill():
    #print(current_dir)
    for filename in os.listdir(current_dir):
        print(os.path.join(current_dir,filename))
        filename=filename.lower()
        organiztype(filename,(".pdf"),"Pdf")
        organiztype(filename,(".jpg",".svg","jfif",".png"),"Images")
        organiztype(filename,(".zip",".rar"),"Compress")
        organiztype(filename,(".udl",".txt"),"Text")
        organiztype(filename,(".lnk"),"Links")
        organiztype(filename,(".xls"),"Excel")
        organiztype(filename,(".mp4"),"Video")
        organiztype(filename,(".xml",".json"),"json")
    if out_folder !='':
        dirctors=[ name for name in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, name)) ]
        for d in dirctors:
             if d not in (out_folder,'.vs','__pycache__'):
                    forceMergeFlatDir(os.path.join(current_dir, d),os.path.join(current_dir,out_folder, d))
                    shutil.rmtree(os.path.join(current_dir, d))
             print(d)
    print("done")
def forceMergeFlatDir(srcDir, dstDir):
    if not os.path.exists(dstDir):
        os.makedirs(dstDir)
    for item in os.listdir(srcDir):
        srcFile = os.path.join(srcDir, item)
        dstFile = os.path.join(dstDir, item)
        copyTree(srcFile, dstFile)

def forceCopyFile (sfile, dfile):
    if os.path.isfile(sfile):
        shutil.copy2(sfile, dfile)

def isAFlatDir(sDir):
    for item in os.listdir(sDir):
        sItem = os.path.join(sDir, item)
        if os.path.isdir(sItem):
            return False
    return True


def copyTree(src, dst):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isfile(s):
            if not os.path.exists(dst):
                os.makedirs(dst)
            forceCopyFile(s,d)
        if os.path.isdir(s):
            isRecursive = not isAFlatDir(s)
            if isRecursive:
                copyTree(s, d)
            else:
                forceMergeFlatDir(s, d)


