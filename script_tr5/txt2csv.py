# -*- coding: utf-8 -*-
"""
Created on Sat May  5 19:56:15 2018

@author: diego
"""
import sys
import sh
reload(sys)
sys.setdefaultencoding('utf-8')

ar=list(sh.ls("-l"))
txt=[]
for i in range(0,len(ar)):
    if ".txt" in ar[i]:
        txt.append(ar[i])
for i in range(0,len(txt)):    
    txt[i]=txt[i][46:len(txt[i])]
    if " " in txt[i]:
        txt[i]=txt[i][1:len(txt[i])]
for i in range(0,len(txt)):
    sh.cp(txt[i][0:len(txt[i])-1],txt[i][0:len(txt[i])-5]+".csv")
    
     
