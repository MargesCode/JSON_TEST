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

        csvfile = open('Testdata_Eng_1.csv','a',newline="", encoding = 'utf8')
        fieldnames = ['ID', 'Agent Name','Intent Name','Eng String']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for cdata in carry_info:
            print("start write:",cdata)
            writer.writerow(cdata)
            
        csvfile.close()

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

    global itemCount

    readfile=open(l_fileList,'r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
    myData=json.load(readfile)

    for jasonf in myData:
        cJson=jasonf['data']
        cStr=""
        for myStr in cJson:
            cStr+=myStr['text']
#        list_info={'ID':'','Agent Name':'','Intent Name':'','Eng String':''}
        list_info={}
        list_info['ID']=str(itemCount)
        list_info['Agent Name']=agentName
        list_info['Intent Name']=intentName
        list_info['Eng String']=cStr

        array_list_info.append(list_info)
        itemCount+=1
    
    readfile.close()

#=========== Main Start=========================
array_AName=[]                   #儲存Agent的名稱
for cagent in os.listdir(path):  #os.listdir(path) 取得路徑下資料夾名稱
    array_AName.append(cagent)

for CAName in array_AName:
    agentName=CAName
    path_lv1=os.path.join('TestData',CAName,'intents') #取得路徑
    getinfo(path_lv1)

writecsv(array_list_info)


print("  Finished!!!   ^_^")
