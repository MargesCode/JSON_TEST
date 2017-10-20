# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:43:41 2017

@author: marge
"""

import os
import json
import csv

#===========定義變數=========================
path = 'TestData/'   
agentName=""        #Agent Name
intentName=""       #Intent Name
entityName=""       #Entity Name
intentStr=""        #Entity string
itemCount=1
array_list_info=[]
#list_info={'ID':'','Agent Name':'','Intent Name':'','Eng String':''}
#=============== 寫入csv ============
def writecsv(carry_info):

#    with open('testdata.csv', 'w') as csvfile:
#        fieldnames = ['ID', 'Agent Name','Intent Name','Eng Sting']
#        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#        writer.writeheader()
#        for cdata in carry_info:
#            print("start write:",cdata)
#            writer.writerow(cdata)
   
    
        csvfile = open('testdata_Eng.csv','a',newline="", encoding = 'utf8')
        fieldnames = ['ID', 'Agent Name','Intent Name','Eng String']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for cdata in carry_info:
            print("start write:",cdata)
            writer.writerow(cdata)
            
        csvfile.close()
#    
#    wfile=csv.writer(outfile)
    
#    print(cwriteInfo)
#    wfile.writeheader()
#    for cdata in carry_info:
#        print("start write:",cdata)
#        wfile.writerow(cdata) 
#    


#=============獲取檔案資訊 ====================
def getinfo(cPath):
    global intentName
    for tops, dirs, files in os.walk(cPath):
        for f in files:
            useFile=os.path.join(tops, f)     
            if "_en" in useFile:
    #            print(f)        #黨案名稱
    #            print(useFile)   #整個path的名稱
                intentName=f[0:f.find("_en")]
                Test1(useFile)
            else:
                continue

#=============讀取JSON ====================
def Test1(l_fileList):
#    a=1
#    test1=[]
#    t1=[{'id':'aa','data':'bb','cc':'cc'}]
#    t2=[{'id':'11','data':'22','cc':'33'}]
#    test1.append(t1)
#    print("a."+str(len(test1)))
#    test1.append(t2)
#    print("b."+str(len(test1)))
#    print("aaa===",type(test1))
#    print("Descript1:",str(test1[0]))
#    print("Descript2:",str(test1[1]))
#    for da in test1:  
#        print(str(a)+"."+ da[0]['id'])
##        print(str(a)+"."+ da[1]['id'])
#        a+=1
    
    
#    array_list_info=[]
#    list_info={'ID':'','Agent Name':'','Intent Name':'','Eng String_API.AI':''}
#    arry_info=['ID','Agent Name','Intent Name','Eng String']
    global itemCount
#    global array_list_info
#    global intentName
#   
#    readfile=open('data\weather - context_weather - comment_activity_usersays_zh-tw.json','r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
#    readfile=open('Sample.json','r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
#    print(l_fileList)
    readfile=open(l_fileList,'r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
    myData=json.load(readfile)
#    list_info={'ID':'','Agent Name':'','Intent Name':'','Eng String_API.AI':''}
    for jasonf in myData:
        cJson=jasonf['data']
        cStr=""
        for myStr in cJson:
            cStr+=myStr['text']
        list_info={'ID':'','Agent Name':'','Intent Name':'','Eng String':''}
        list_info['ID']=str(itemCount)
        list_info['Agent Name']=agentName
        list_info['Intent Name']=intentName
        list_info['Eng String']=cStr
#        print(list_info)
#        print("1. list_info['ID']=",list_info['ID'])
        array_list_info.append(list_info)
        
#        print("2. list_info['ID']=",list_info['ID'])
#        print(array_list_info)
#        print("list length=====",len(array_list_info))
        
#        writeInfo=str(itemCount)+","+agentName+","+intentName+","+cStr #定義要寫入的字串
#        writecsv(array_list_info)
#        print(str(itemCount)+","+agentName+","+intentName+","+cStr)
#        print(str(itemCount))
        itemCount+=1
#       
    
    readfile.close()
#    for dd in array_list_info:
#        print("CID="+dd['ID'])
#


#=========== Main Start=========================
array_AName=[]                   #儲存Agent的名稱
for cagent in os.listdir(path):  #os.listdir(path) 取得路徑下資料夾名稱
    array_AName.append(cagent)

for CAName in array_AName:
    agentName=CAName
    path_lv1=os.path.join('TestData',CAName,'intents') #取得路徑
    getinfo(path_lv1)
    
#print("Total Data:",len(array_list_info))
#print(array_list_info)
writecsv(array_list_info)

#print("=====================================")
print("  Finished!!!   ^_^")
#=========== Main End=========================
    
#    agentName=array_AName[0]
#    path_lv1=os.path.join('TestData',array_AName[0],'intents')


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

#=============== 主程式 ====================
#readJson()
#fileList=getFileName()
#print(fileList)
#readJson(fileList)
#readJson()
