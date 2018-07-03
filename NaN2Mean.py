# -*- coding: utf-8 -*-
"""
Created on Sat May  5 18:33:59 2018

@author: diego
"""
#Reemplaza los datos faltantes de una serie por el promedio de toda la serie
#Estructura de datos de entrada= CODIGOEST_VAR.csv, una fila, sin encabezado
import numpy as np
import pandas as pd
#Lista de estaciones
esta=["21205420", "21206550", "21205770", "21205980", "21205710", "21206280"]   
#Lista de varibles 
var=["HR", "TS", "TSmin", "TSmax", "VR", "BS"]
#Reemplazar con el promedio
rm=True  

for l in range(0,len(esta)):
    for j in range(0,len(var)):
    
        arch=esta[l]+"_"+var[j]+".csv"
        data=pd.read_csv(arch, names=[var[j]])
        #Los valores de HR estan multiplicados por 10 en los tr5
        if var[j]=="HR":
            data=data/10
        #Los valores de viento son recorrido del viento, se pasan Velocidad 
        elif var[j]=="VR":
            data=100*data/86400
        else:
            data=data
        if rm:
            mean=np.mean(data[var[j]])
            for i in range (0,len(data)):
                if np.isnan(data[var[j]][i]):
                    data[var[j]][i]=mean
        
        pd.DataFrame.to_csv(data, esta[l]+"_"+var[j]+".csv", index=False, header=False)


        
             