# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:14:47 2018

@author: diego
"""
##########################################################################
##---------------CALCULA VALORES FALTANTES DE PRECIPITACION-------------##
##------------------USANDO CORRELACION LINEAL PONDERADA-----------------##
##########################################################################
#P(t)=[(P1*r1)+(P2*r2)+...+(Pn*rn)]/(r1+r2+...+rn)
#P(t)=Valor de precipitacion a calcular
#Pn=Valor de la precipitacion el mismo dia en estacion vecina
#rn=Coeficiente de correlacion entre las estaciones calculado con la
#precipitacion normalizada mensualmente
import pandas as pd
import numpy as np

#Lista de estaciones vecinas
esta=['21190310', '21201060', '21201070', '21201210', '21201270',
      '21205660','21205420'] 
#Ano inicial (Pirmer enero) y Año final (Siguiente a ulitmo diciembre)
Anoi=1981
Anof=2011

#Carga los datos en un DataFrame
df=pd.read_csv(esta[0]+"_PT.csv", names=[esta[0]] )
for i in range(1,len(esta)):
    df[esta[i]]=pd.read_csv(esta[i]+"_PT.csv")
    
#Normaliza las variables mensualmente

normal=df

for l in range(0,len(esta)):
    n=0
    dia=0
    Ano=Anoi
    #Enero
    for j in range(0,Anof-Anoi):
        n=31
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Febrero
        if Ano%4==0:
            n=29
        else:
            n=28
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Marzo
        n=31
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Abril
        n=30
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Mayo
        n=31
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Junio
        n=30
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Julio
        n=31
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Agosto
        n=31
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Septiembre
        n=30
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Octubre
        n=31
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Noviembre
        n=30
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
    #Diciembre
        n=31
        mean=np.mean(df[esta[l]][dia:dia+n])
        x=dia
        for i in range(x,x+n):
            normal[esta[l]][i]=(df[esta[l]][i])/mean
            dia=dia+1
        Ano=Ano+1
    print("Estacion " +esta[l]+" normalizada")
    
df=pd.read_csv(esta[0]+"_PT.csv", names=[esta[0]] )
for i in range(1,len(esta)):
    df[esta[i]]=pd.read_csv(esta[i]+"_PT.csv")

#Matriz de correlacion 
cor_mat=pd.DataFrame.corr(normal)
#Calculo el valor faltante con Correlacion lineal ponderada
df_com=df
for l in range(0,len(esta)):
    for j in range(0,len(df[esta[l]])):
        num=[]
        den=[]
        if np.isnan(df_com[esta[l]][j]):
            for k in range(0, len(esta)):
                num.append(normal[esta[k]][j]*cor_mat[esta[k]][l])
                den.append(cor_mat[esta[k]][l])
            df_com[esta[l]][j]=(np.nansum(num)/np.nansum(den))
    print("Estacion " +esta[l]+" sin datos faltantes")

for l in range(0,len(esta)):
    for i in range(0,len(df_com[esta[l]])):
        df_com[esta[l]][i]=round(df_com[esta[l]][i],1)
        
for i in range(0, len(esta)):
    DF=df_com[esta[i]]
    DF=pd.DataFrame.from_dict(DF)
    pd.DataFrame.to_csv(DF, esta[i]+"_PTc.csv", header=False, index=False)
    print(esta[i]+"_PTc.csv creado")

            

