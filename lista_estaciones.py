# -*- coding: utf-8 -*-
"""
Created on Mon May  7 14:06:01 2018

@author: diego
"""

f=open("20189050033522.tr5","r")
lines=f.readlines()
f.close()

for i in range(0,len(lines)):
    lines[i]=lines[i][1:9]

estaciones=[lines[0]]
for i in range(1,len(lines)):
    if lines[i] not in estaciones:
        estaciones.append(lines[i])
for i in range(1,len(estaciones)):
    print("'"+estaciones[i]+"',")

        