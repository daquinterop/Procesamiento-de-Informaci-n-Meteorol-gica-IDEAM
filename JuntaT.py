# -*- coding: utf-8 -*-
"""
Created on Sun May  6 16:56:50 2018

@author: diego
"""
import pandas as pd

esta=["21205420"]

for i in range(0,len(esta)):
    arch=esta[i]+"_TSmin.csv"
    Tmin=pd.read_csv(arch, names=["Tmin"])
    arch=esta[i]+"_TSmax.csv"
    Tmax=pd.read_csv(arch, names=["Tmax"])
    Tmin["Tmax"]=Tmax
    
    pd.DataFrame.to_csv(Tmin, esta[i]+"_TT.csv",header=False, index=False, sep="\t")