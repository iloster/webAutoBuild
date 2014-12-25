# -*- coding:utf-8 -*-
#   Author:ZedLi
#   Date:2014.12.22
#   Description:打包
import os
import shutil
import zipfile
import time
from xml.dom import minidom

def updateProject():
    #更新代码
    print 'update project.....'
    path = os.getcwd()
    os.chdir(r'.\project\Resource')
    os.system('svn update')
    os.chdir(path)
    
#gametype:0.全部 1.马股 2.二七十 3.血流成河  4.川味斗地主 5.不内置游戏
def zipFile(gametype):
    print "compressed files....."
    if gametype == 0 or gametype == '0':
        zipFileBatPath = r'.\project\products\engine_android\sync_publish_app_allgames.bat'
    elif gametype == 1 or gametype == '1':
        zipFileBatPath = r'.\project\products\engine_android\sync_publish_app_magu.bat'
    elif gametype == 2 or gametype == '2':
        zipFileBatPath = r'.\project\products\engine_android\sync_publish_app_eqs.bat'
    elif gametype == 3 or gametype == '3':
        zipFileBatPath = r'.\project\products\engine_android\sync_publish_app_xlch.bat'
    elif gametype == 4 or gametype == '4':
        zipFileBatPath = r'.\project\products\engine_android\sync_publish_app_scddz.bat'
    else:
        zipFileBatPath = r'.\project\products\engine_android\sync_publish_app_hall.bat'
    
    os.system(zipFileBatPath)

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

def listApk(path):
    apklist = os.listdir(path)
    if len(apklist) >0:
        return True,apklist
    else:
        return False,'error'
    
def buildProperties(channel,versionName):
    config_channel_zhu = r'.\project\products\channel_config\config_channel_zhu.xml'
    base_build_properties = r'.\project\products\channel_config\base_build.properties'
    final_build_properties = r'.\project\products\engine_android\build.properties'
    #os.remove(final_build_properties)
    f = open(base_build_properties,'r+')
    baseContent = f.read();
    f.close()
    dom = minidom.parse(config_channel_zhu)
    channelList = channel.split('-')
    #获取所有item
    allChannelStr = ''
    items = dom.documentElement.getElementsByTagName('item')
    for i in range(len(channelList)):
        for item in items:
            if channelList[i] == item.getElementsByTagName('channelId')[0].childNodes[0].data:
                appidxml = "appid\=103000;"
                channel_idxml = "channel_id\="+channelList[i] + ";"
                channel_keyxml = "channel_key\="+item.getElementsByTagName('channelKey')[0].childNodes[0].data + ";"
                umeng_channelxml = "umeng_channel\="+ item.getElementsByTagName('umeng_channel')[0].childNodes[0].data + ";"
                apknamexml = "apkname\=" + item.getElementsByTagName('channelOutputName')[0].childNodes[0].data % versionName + ','
                channelStr = appidxml+channel_idxml+channel_keyxml+umeng_channelxml+apknamexml
                
        allChannelStr = allChannelStr + channelStr

    nowTime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    apkOutPathxml = r"E\:\\GitHub\\webBuild\\project\\products\\Apks\\" + nowTime
    apkOutPath = '.\\project\\products\\Apks\\' + nowTime
    os.makedirs(apkOutPath)
    fp = open(final_build_properties,'w')
    fp.write(baseContent + "channel.list=" + allChannelStr+"\n"+"apk.out.dir="+apkOutPathxml)
    fp.close()
    return apkOutPath,nowTime
        
    
#appid:测试还是正式   gametype:0.全部 1.马股 2.二七十 3.血流成河  4.川味斗地主 5.不内置游戏
def autoBuild(appid,gametype,channel,versionName):
    #改写build.properties
    apkOutPath,nowTime= buildProperties(channel,versionName)
    updateProject()
    zipFile(gametype)
    #moveFile()
    antBuild()
    #flag,name = checkApk()
    flag,apklist = listApk(apkOutPath)
    if flag: #下载成功
        return {"ret":"1","apklist":apklist,"nowTime":nowTime}
    return {"ret":"0"}
    
