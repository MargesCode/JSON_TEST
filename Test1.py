# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:35:06 2017

@author: marge
"""
#l1={}
mylist2=[{'id':1,'data':"AAA"}]
print("before:",mylist2)

co=0
a=1
for co in range(5):
    
#    l1={'id':a,'data':"Data"+str(a)}
    l1={}
    l1['id']=a
    l1['data']="Data"+str(a)
    mylist2.append(l1)
    print(str(a)," st:",mylist2)
    a+=1

#mylist2.append(l1)
#print("1 st:",mylist2)
#l1={'id':3,'data':"CCC"}
#
#mylist2.append(l1)
#print("2 nd:",mylist2)
#t1={}
#
#co=0
#a=1
#for co in range(5):
#    t1['id']=a
#    t1['Data']="Data="+str(a)
#    mylist+t1
#    a+=1
    
    