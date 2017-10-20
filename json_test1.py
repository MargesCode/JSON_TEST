# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:43:41 2017

@author: marge
"""

import json

readfile=open('Sample.json','r', encoding = 'utf8')  # encoding = 'utf8' 解決 cp950的問題
myData=json.load(readfile)
myData_Lev1=myData[0];
myData_Lev2=myData[0]['data']

#print("Type:",type(myData))
#
#print("myData[0]:",myData[0])
#
#print("myData[0]['data']:",myData[0]['data'])

print("Type:",type(myData_Lev2))
print(myData_Lev2)

a=""
for myStr in myData_Lev2:
    a+=myStr['text']
#    a+=a
    print("str:",a)

#
#for d in myData:
#    print(d['data'])  #印出data的資料

#data1=myData[0]['data']
#print(data1['data'])
#print(type(myData[0]['data'])
#myData_Dump=json.dumps(readfile)
#print("mydata_Load:",type(myData_Load))
#print("mydata_Dump:",type(myData_Dump))

