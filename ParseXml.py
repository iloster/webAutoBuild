#-*- coding: UTF-8 -*-
#-----------------------------------
#   python2.7
#   author:loster
#   description:解析xml
#-------------------------------------
import  xml.etree.ElementTree as ET

def getXml(fileName):
    root = ET.fromstring(fileName)#.getroot() #获得根节点
    resultList = []  
    walkXml(root,resultList,root.tag)
    return resultList

def walkXml(root,resultList,tempLists):
    if tempLists == 'root':
        tempLists = ""
    tempList = tempLists+',"'+root.tag+'"'
    resultList.append(tempList)
    children_node = root.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkXml(child,resultList,tempList)
    return

def parseXmlString(xmlStr):
    return getXml(xmlStr),getXmlTag(xmlStr)

def getXmlTag(fileName):
    root = ET.fromstring(fileName)#.getroot() #获得根节点
    resultListTag = []  
    walkXmlTag(root,resultListTag)
    return resultListTag

def walkXmlTag(root,resultListTag):
    tempListTag = root.tag
    resultListTag.append(tempListTag)
    children_node = root.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkXmlTag(child,resultListTag)
    return
#if __name__ == "__main__":
#    file_name = "diamondShopDialog.xml"
#    R = getXml(file_name)
#    for r in R:
#        print "{"+r[8:]+"}"
    
        
