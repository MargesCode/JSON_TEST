# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:16:42 2017

@author: marge
"""

import os
import json


path = 'Data2/'   
itemCount=1


def readJson_1(l_fileList):
#    print("find position:",l_fileList.find("."))
#    pStart=l_fileList.find("/")+1
#    pEnd=l_fileList.find(".")
#    print("intent Name:",l_fileList[pStart:pEnd])
    
    
    global itemCount
#    readfile=open('Sample.json','r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
#    print(l_fileList)
    readfile=open(l_fileList,'r', encoding = 'utf8') 
    myData=json.load(readfile)
    
    for jasonf in myData:
        cJson=jasonf['data']
        cStr=""
        for myStr in cJson:
            cStr+=myStr['text']
        print(str(itemCount)+","+str(getInit(l_fileList))+","+cStr)
        itemCount+=1   
    readfile.close()
    

def getInit(l_initName):
    pStart=l_initName.find("/")+1
    pEnd=l_initName.find(".")
    strInitName=l_initName[pStart:pEnd]
    return strInitName
    
    
#getintentName("abc.123")

#=============== Main ================
for tops, dirs, files in os.walk(path):
    for f in files:
        useFile=os.path.join(tops, f)
#        print(useFile)
        readJson_1(useFile)