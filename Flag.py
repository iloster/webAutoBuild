import os
FLAG_PATH = r'.\isExist.flag'
#创建一个Flag文件
def createFlag():
    global FLAG_PATH
    if os.path.exists(FLAG_PATH):
        os.remove(FLAG_PATH)
    else:
        f = open(FLAG_PATH,'w')
        f.close()

#删除Flag文件
def deleteFlag():
    global FLAG_PATH
    if os.path.exists(FLAG_PATH):
        os.remove(FLAG_PATH)

#检查Flag是否存在
def checkFlag():
    global FLAG_PATH
    if os.path.exists(FLAG_PATH):
        return True
    else:
        return False
