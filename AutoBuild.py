#coding=utf-8
import os
import shutil
import zipfile
import time

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

def renameApk():
    apk = os.listdir(r'.\project\products\Apks') #所有的apks
    if 'scqp.apk' in apk:
        #获取当前时间  
        nowTime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        newName = '.\\project\\products\\Apks\\scqp_'+nowTime+'.apk'
        os.rename(r'.\project\products\Apks\scqp.apk',newName)
        return True,'scqp_'+nowTime+'.apk'
    else:
        return False,'error'
    
def autoBuild():
    updateProject()
    #delApk()
    zipFile()
    moveFile()
    antBuild()
    #flag,name = checkApk()
    flag,name = renameApk()
    if flag: #下载成功
        return {"ret":"1","apkname":name}
    return {"ret":"0"}
    
