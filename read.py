# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 22:16:42 2017

@author: marge
"""

import os
import json


path = 'Data2/'   
itemCount=1

for tops, dirs, files in os.walk(path):
    for f in files:
        useFile=os.path.join(tops, f)
#        print(useFile)
        readJson_1(useFile)

def readJson_1(l_fileList):
    global itemCount
#    readfile=open('Sample.json','r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
#    print(l_fileList)
    readfile=open(l_fileList,'r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
    myData=json.load(readfile)
    
    for jasonf in myData:
        cJson=jasonf['data']
        cStr=""
        for myStr in cJson:
            cStr+=myStr['text']
        print("str:",cStr)
        itemCount+=1   
    readfile.close()