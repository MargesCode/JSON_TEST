# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:43:41 2017

@author: marge
"""

import os
import json

#====== 讀取並列出所有的檔名,包含子目錄==============
#取得所有folder name 

#for dirname,dirnames,filenames in os.walk('.'):
#    for subdirname in dirnames:
#        print(os.path.join(dirname,subdirname))
#        print("=============================")
##取得所有folder 下的file name        
#    for filename in filenames:
#        print(os.path.join(dirname,filename))
#==========================================
#print("aaaa")
path = 'TestData/'   

array_AName=[]                   #儲存Agent的名稱
for cagent in os.listdir(path):  #os.listdir(path) 取得路徑下資料夾名稱
    array_AName.append(cagent)
#    print(array_AName)

path_lv1=os.path.join('TestData',array_AName[0],'intents')
#print(path_lv1)


#=============== Main ================
for tops, dirs, files in os.walk(path_lv1):
    for f in files:
        useFile=os.path.join(tops, f)
        print(useFile)    
        if "_en" in useFile:
#        print()
##            print("True")
        rJson(useFile)



#agentName=""
#intentName=""
#entityName=""
#intentStr=""

#print(os.listdir(path))
#print(os.path.abspath('.'))
#itemCount=1
#
#for tops, dirs, files in os.walk(path):
#    for f in files:
#        useFile=os.path.join(tops, f)
#        print(useFile)
#        readJson_1(useFile)

#=======獲取檔名================

#
#def getFileName():
#    cfileList=[]
#    fileSize=0
#    folderCount=0
#    rootdir = 'data'   #root folder define(資料所在的資料夾)
#    names=os.listdir(rootdir)
#    #print(type(names),names)
#    for fileName in names:
#        cfileList.append(fileName);
##        print(fileName)
##        print(len(fileList))
##        print(fileList,"\r\n")
#    return cfileList
##cDIR= os.getcwd()
#print(type(cDIR))

#===============讀取JSON===============
#
#def readJson():
##    readfile=open('data\weather - context_weather - comment_activity_usersays_zh-tw.json','r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
#    readfile=open('Sample.json','r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
#    myData=json.load(readfile)
#    
#    for jasonf in myData:
#        cJson=jasonf['data']
#        cStr=""
#        for myStr in cJson:
#            cStr+=myStr['text']
#        print("str:",cStr)
#        readfile.close()
#=============讀取JSON 帶陣列=====================
def rJson(l_fileList):
    global itemCount
#   
#    readfile=open('data\weather - context_weather - comment_activity_usersays_zh-tw.json','r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
#    readfile=open('Sample.json','r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
    print(l_fileList)
    readfile=open(l_fileList,'r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
    myData=json.load(readfile)
    
    for jasonf in myData:
        cJson=jasonf['data']
        cStr=""
        for myStr in cJson:
            cStr+=myStr['text']
        print(itemCount+","+cStr)
        itemCount+=1
    
    readfile.close()
#=============== 主程式 ====================
#readJson()
#fileList=getFileName()
#print(fileList)
#readJson(fileList)
#readJson()
