# -*- coding: utf-8 -*-
"""
Created on Sun May  6 13:15:40 2018

@author: diego
"""
#########################################################################
##--CALCULA EL MAXIMO, MINIMO, MEDIA Y PORCENTAJE DE DATOS FALTANTES---##
#########################################################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Lista de estaciones
esta=['21190310', '21190310', '21201060', '21201070', '21201210', '21201270', '21205660'] 
#Lista de varibles 
var=["PT"]
graf=False   #Para graficar

for j in range(0,len(esta)):
    Max=[]
    Min=[]
    Mean=[]
    Nan=[]
    for i in range(0,len(var)):
        arch=esta[j]+"_"+var[i]+".csv"
        data=pd.read_csv(arch, names=[""])
        Max.append(np.max(data[""]))
        Min.append(np.min(data[""]))
        Mean.append(np.mean(data[""]))
        Nan.append(100.00*(sum(np.isnan(data[""])))/len(data[""]))
    #Crea un vector de valores    
    Min=['Minimo']+ Min
    Max=['Maximo']+ Max
    Mean=['Media']+ Mean
    Nan=['Sin Datos(%)']+ Nan
    records=[Min,Max,Mean,Nan]
    col=["Dato"]+var
    #Crea el DataFrame
    DesSta=pd.DataFrame.from_records(records, columns=col)
    #Crea el archivo csv
    pd.DataFrame.to_csv(DesSta, esta[j]+"_DSta.csv",index=False)
    print("*************"+esta[j]+"***************")    
    print(DesSta)
    
    if graf:
        for i in range(0,len(var)):
            x=np.arange(3)
            plt.bar(x,height=DesSta[var[i]][0:3], align="center", width=0.5) 
            plt.axhline(color="k")
            plt.xticks(x, ["Minimo", "Maximo", "Media"])
            plt.title("Valores de " +var[i]+" en la estacion " + esta[j])
            plt.savefig(esta[j]+"_"+var[i]+".png", dpi=500)
            plt.show()
            plt.close()
        
        x=np.arange(0,len(var))
        plt.bar(x,height=Nan[1:len(Nan)], align="center", width=0.3, color="r")
        plt.xticks(x, var)
        plt.title("Porcentaje de datos faltantes por variable para \n la estacion "+esta[j])
        plt.savefig(esta[j]+"_NaN.png", dpi=500)
        plt.show()
        plt.close()
    
