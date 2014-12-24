# -*- coding:utf-8 -*-
#   Author:ZedLi
#   Date:2014.12.22
#   Description:解析mainfest.xml文件，获取包名，版本号，代码号
# ---------------------------------
from xml.dom import minidom
import re

MANIFEST_PATH = ".\\project\\products\\engine_android\\AndroidManifest.xml"
GAMECONFIG_PATH = ".\\project\\Resource\\scripts\\hall\\gameConfig.lua"
def doxml():
    global MANIFEST_PATH
    dom = minidom.parse(MANIFEST_PATH)
    root = dom.documentElement
    packageName = root.getAttribute('package')
    versionCode = root.getAttribute('android:versionCode')
    versionName = root.getAttribute('android:versionName')
    return packageName,versionCode,versionName

def dolua():
    global GAMECONFIG_PATH
    f = file(GAMECONFIG_PATH)
    content = f.read()
    f.close()
    hallReg = re.compile(r'gameVersion=(.*?);\n.*?gameName=(.*?);[\s\S]*dependApkVersion="(.*?)";')
    gameReg = re.compile(r'[\s\S]*1] =(.*?);[\s\S]*2] =(.*?);[\s\S]*5] =(.*?);[\s\S]*6] =(.*?);[\s\S]*9] =(.*?);[\s\S]*10] =(.*?);[\s\S]*7] =(.*?);')
    results1 = hallReg.findall(content)
    results2 = gameReg.findall(content)
    return results1,results2

def getApkInfo():
    apkInfo = {}
    apkInfo['packageName'],apkInfo['versionCode'],apkInfo['versionName'] = doxml()
    hallResult,gamesResult = dolua()
    apkInfo['hallVersion'],apkInfo['dependApkVersion'] = hallResult[0][0],hallResult[0][2]
    apkInfo['scmj'],apkInfo['scddz'],apkInfo['eqs'],apkInfo['magu'] = gamesResult[0][1],gamesResult[0][3],gamesResult[0][4],gamesResult[0][5]
    return apkInfo
