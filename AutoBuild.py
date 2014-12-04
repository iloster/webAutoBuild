#coding=utf-8
import os
import shutil
import zipfile

def updateProject():
    #更新代码
    print 'update project.....'
    path = os.getcwd()
    os.chdir(r'.\project\Resource')
    os.system('svn update')
    os.chdir(path)
    

def zipFile():
    print "compressed files....."
    os.system(r'.\project\products\engine_android\sync_publish_app_allgames.bat')

def moveFile():
    print "move hall.zip to assert..."
    srcZipFile = r'.\project\products\engine_android\gameZips\hall.zip'
    desZipFile = r'.\project\products\engine_android\assets\games\hall.zip'
    shutil.move(srcZipFile,desZipFile)

def antBuild():
    #打开android项目目录
    print "compile....."
    path = os.getcwd()
    os.chdir(r'.\project\products\engine_android')
    os.system('ant')
    #os.system(r'.\project\products\engine_android\antBuild.bat')
    os.chdir(path)
    print "compile.......finish--"+os.getcwd()
    
def delApk():
    #删除Apks文件夹
    shutil.rmtree(r'.\project\products\Apks')
    os.makedirs(r'.\project\products\Apks')
    
def checkApk():
    apk = os.listdir(r'.\project\products\Apks')
    if len(apk) ==0:
        return False,'error'; 
    return True,apk[0]
    
def autoBuild():
    updateProject()
    delApk()
    zipFile()
    moveFile()
    antBuild()
    flag,name = checkApk()
    if flag: #下载成功
        return {"ret":"1","apkname":name}
    return {"ret":"0"}
    
