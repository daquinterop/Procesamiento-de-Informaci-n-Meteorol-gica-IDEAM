# -*- coding: utf-8 -*-
"""
Created on Fri May  4 16:30:14 2018

@author: diego
"""
#Calcula la ETo utilizando la ecuación de FAO Penmann-Monteith
#Utiliza el modulo pyeto [https://github.com/woodcrafty/PyETo]
#Utiliza el modulo sh para crear archivos

#NECESITA TENER LOS ARCHIVOS DE TEMPERATURAS MINIMAS(TSmin), MAXIMAS (TSmax), 
#MEDIAS(TS), BRILLO SOLAR(BS) Y VELOCIDAD DEL VIENTO(RV) DE LA SIGUIENTE MANERA:
#CODIGO_VAR.txt. DONDE ESTEN LOS VALORES, UNO CADA FILA

import sys
import pyeto
import pandas as pd

reload(sys)
sys.setdefaultencoding('utf-8')



##########################################################
#---------------INGRESO DE VARIABLES---------------------#
##########################################################
#Lista de codigos de estaciones para las que se calcula la ETo
esta=["21205420"] 
#Lista de latitudes en grados
LAT=[5]  
#Lista de altitudes en msnm
ALT=[2600]
Ano=1981
 

############################################################
##-------------------CALCULO DE ETo------------------------#
############################################################
for i in range(0,len(esta)):
#Apertura de archivos que contienesn las variables
    arch=esta[i]+"_TSmin.csv"
    Tmin=pd.read_csv(arch, names=["0"])
    
    arch=esta[i]+"_TSmax.csv"
    Tmax=pd.read_csv(arch, names=["0"])
    
    arch=esta[i]+"_TS.csv"
    Tmean=pd.read_csv(arch, names=["0"])
    
    arch=esta[i]+"_BS.csv"
    BS=pd.read_csv(arch, names=["0"])
    
    arch=esta[i]+"_VR.csv"
    VV=pd.read_csv(arch, names=["0"])
    
    arch=esta[i]+"_HR.csv"
    HR=pd.read_csv(arch, names=["0"])

      
#Inciacion de los valores de ETo
    lat=LAT[i]
    altitude=ALT[i]
    
    tmin=[]
    tmax=[]
    t=[]
    rh_mean=[]
    ws=[]
    lat=pyeto.deg2rad(lat)
    day=1
    sunshine_hours=[]
    ETO=[]


#Completar los valores de ETo
    for j in range(0,len(Tmean["0"])):
            tmin=(Tmin["0"][j])
            tmink=pyeto.celsius2kelvin(tmin)
            tmax=(Tmax["0"][j])
            tmaxk=pyeto.celsius2kelvin(tmax)
            t=(Tmean["0"][j])
            tk=pyeto.celsius2kelvin(t)
            rh_mean=(HR["0"][j])
            ws=(VV["0"][j])
            lat=pyeto.deg2rad(lat)
            day=day+1
            sunshine_hours=(BS["0"][j])
            #Radiacion neta
            sol_dec=pyeto.sol_dec(day)
            sha=pyeto.sunset_hour_angle(lat,sol_dec)
            daylight_hours=pyeto.daylight_hours(sha)
            ird=pyeto.inv_rel_dist_earth_sun(day)
            et_rad=pyeto.et_rad(lat, sol_dec, sha, ird)
            sol_rad=pyeto.sol_rad_from_sun_hours(daylight_hours,sunshine_hours,et_rad)
            ni_sw_rad=pyeto.net_in_sol_rad(sol_rad, albedo=0.23)
            cs_rad=pyeto.cs_rad(altitude, et_rad)
            svp_tmin=pyeto.svp_from_t(tmin)
            svp_tmax=pyeto.svp_from_t(tmax)
            avp=pyeto.avp_from_rhmean(svp_tmin, svp_tmax, rh_mean)
            no_lw_rad=pyeto.net_out_lw_rad(tmink, tmaxk, sol_rad, cs_rad, avp)
            net_rad=pyeto.net_rad(ni_sw_rad, no_lw_rad)
            #Presion de vapor de saturacion
            svp=pyeto.svp_from_t(t)
            #Delta presion de vapor de saturacion
            delta_svp=pyeto.delta_svp(t)
            #Constante psicrométrica
            atmos_pres=pyeto.atm_pressure(altitude)
            psy=pyeto.psy_const(atmos_pres)
            #Calculo ETo Fao Penman Monteith
            ETo=pyeto.fao56_penman_monteith(net_rad, tk, ws, svp, avp, delta_svp, psy, shf=0.0)
            ETO.append(ETo)        
            if day>=365:
                if Ano%4==0:
                    Ano=Ano+1
                else:
                    day=1
                    if Ano%4!=1:
                        Ano=Ano+1
    ETO=pd.DataFrame.from_dict(ETO)
    pd.DataFrame.to_csv(ETO, esta[i]+"_ETo"+".csv", index=False, header=False)
#Escribo todos los datos en el archivo

               


        
