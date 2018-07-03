#Toma una archivo de datos tr5 del IDEAM, y los organiza en archivos 
#diferentes por estaciones, variables, y anos. 
#Muestra si la serie de datos esta o no completa

import sh
#Entradas del programa
data="20189050033522.tr5"               #Archivo tr5 
esta=['21190310', '21201060', '21201070', '21201210', '21201270', '21205660', 
'21205420']           #Codigo de estaciones
var=["PT"]        #Variables
Anoi=1981  #Ano inicial (Primer enero)
Anof=2011  #Ano final   (Ano siguiente ultimo diciembre)
col=True   #Organizar en columnas

##############################################################
##                DATOS POR ESTACIONES                     ###
##############################################################
#Copio todos los datos para un archivo para cada estacion
for i in range(0,len(esta)): 
    sh.cp(data,esta[i]+".txt")
    
#Selecciono solo los datos de las estaciones que quiero
for i in range(0,len(esta)):
    arch=esta[i]+".txt"
    f = open(arch,"r")		
    lineas = f.readlines()				
    f.close()
    f = open(arch,"w")
    for linea in lineas:
    	if esta[i] in linea:
    		f.write(linea)
    f.close()
    
##############################################################
##                DATOS POR VARIABLES                      ###
##############################################################
#Creo los archivos para cada variable y estacion
for i in range(0,len(esta)):
    for j in range (0,len(var)):
        sh.cp(esta[i]+".txt",esta[i]+"_"+var[j]+".txt")
        
#Selecciono los datos para cada varaiable que quiero
for i in range(0,len(esta)):
    for j in range(0,len(var)):
        arch=esta[i]+"_"+var[j]+".txt"
        f = open(arch,"r")		
        lineas = f.readlines()				
        f.close()
        f = open(arch,"w")
        for linea in lineas:
        	if var[j] in linea:
        		f.write(linea)
        f.close()

#Creo archivos para temperatura maxima, minima y media
if "TS" in var:    
    for i in range(0,len(esta)):
            sh.cp(esta[i]+"_TS"+".txt",esta[i]+"_TSmin"+".txt")
            sh.cp(esta[i]+"_TS"+".txt",esta[i]+"_TSmax"+".txt")
    
    #Clasifico temperaturas minimas, maximas y medias
    tipe=("   1","   2","   8")
    tipe2=("TS", "TSmax", "TSmin")
    for i in range(0,len(esta)):
        for j in range(0,3): 
            arch=esta[i]+"_"+tipe2[j]+".txt"
            f = open(arch,"r")		
            lineas = f.readlines()				
            f.close()
            f = open(arch,"w")
            for linea in lineas:
                if tipe[j] in linea:
                    f.write(linea)
            f.close()
        
##############################################################
##                    DATOS POR ANOS                       ###
##############################################################
        
Anoss=range(Anoi,Anof)
Anoss=map(str,Anoss)
Anos=Anof-Anoi
#Revisa si hay o no hay Tmin y Tmax
if "TS" in var:
    tipe=var
    tipe.append("TSmin")
    tipe.append("TSmax")
else:
    tipe=var
#Inicia a clasificar los anos que nos interesan
for i in range(0, len(esta)):
    for j in range(0,len(tipe)):
        arch=esta[i]+"_"+tipe[j]+".txt"
        f = open(arch,"r")		
        lineas = f.readlines()				
        f.close()
        
        columnas=range(0,len(lineas))
        
        for k in range(0,len(columnas)):
            columnas[k]=lineas[k][11:15]
            columnas[k]=columnas[k] in Anoss
        
        f = open(arch,"w")
        n=0
        for linea in lineas:
           if  columnas[n]:
                f.write(linea)
           n=n+1
        f.close()
#Revisa si hay series repetidas y las elimina
        if len(lineas)>0:        
            lin=lineas
            x=lineas[0]
            for k in range(0,len(lineas)):
                lin[k]=x in lineas[k]
            x=sum(lin)
            if x>1:
                n=0
                f=open(arch,"r")
                lineas=f.readlines()
                f.close()
                f=open(arch,"w")
                for linea in lineas:
                    if n!=Anos*31:
                        f.write(linea)   
                        n=n+1
#Revisa esta completa o incompleta la serie        
        f=open(arch,"r")
        lineas=f.readlines()
        if len(lineas)<Anos*31:
            print("Datos incompletos para " + arch)
        else:
            print("Datos completos para " + arch)
        f.close()
        
#Llena los datos que faltan en la serie
        Anos=Anof-Anoi
        Anoss=range(Anoi,Anof)
        Anoss=map(str,Anoss)
        x="00000000000000000999990999990999990999990999990999990999990999990999990999990999990999990 \n"
        f=open(arch,"r")
        lineas=f.readlines()
        f.close()        
        f=open(arch,"w")
        n=0
        for k in range(0,Anos*31):
            lineas.append("99990")
        for k in range(0,Anos):
            if Anoss[k] in lineas[n]:
                for l in range(0,31):
                    f.write(lineas[n])
                    n=n+1
            else:
                for l in range(0,31):
                    f.write(x)
        f.close()
##############################################################
##                DATOS EN UNA COLUMNA                     ###
##############################################################
#Comentar todo de aca para abajo si no se desean en columnas
if col:
    inchar=18  #Inicio de los valores, es decir fila donde inician datos
    #Cuento cuantos anos bisiestos hay
    Anoss=range(Anoi,Anof)
    for i in range(0,len(Anoss)):
        Anoss[i]=Anoss[i]%4
        Anoss[i]=Anoss[i]==0
        Anosbi=sum(Anoss)
        
        Anos=Anof-Anoi
        Ano=Anoi
    
    for l in range(0, len(esta)):
        for j in range(0,len(tipe)):
            arch=esta[l]+"_"+tipe[j]+".txt"         
            f=open(arch,"r")
            lines=f.readlines()
            f.close()
            dia=0        
            lin=0
            columnas=range(0,(Anos-Anosbi)*365+Anosbi*366+1)
            
            for k in range(0,Anos):
                mes=1
                #Enero
                for i in range(0,31):
                    columnas[dia]=lines[i+lin][inchar*mes:inchar+mes*5]
                    dia=dia+1
                #Febrero
                mes=mes+1        
                if Ano%4==0:
                    for i in range(0,29):
                        columnas[dia]=lines[i+lin][inchar+(mes-1)*5+1:inchar+mes*5+1]
                        dia=dia+1
                else:
                    for i in range(0,28):
                        columnas[dia]=lines[i+lin][inchar+(mes-1)*5+1:inchar+mes*5+1]
                        dia=dia+1
                #Marzo
                mes=mes+1
                for i in range(0,31):
                    columnas[dia]=lines[i+lin][inchar+(mes-1)*5+2:inchar+mes*5+2]
                    dia=dia+1
                #Abril
                mes=mes+1
                for i in range(0,30):
                    columnas[dia]=lines[i+lin][inchar+(mes-1)*5+3:inchar+mes*5+3]
                    dia=dia+1
                #Mayo
                mes=mes+1
                for i in range(0,31):
                    columnas[dia]=lines[i+lin][inchar+(mes-1)*5+4:inchar+mes*5+4]
                    dia=dia+1
                #Junio
                mes=mes+1
                for i in range(0,30):
                    columnas[dia]=lines[i+lin][inchar+(mes-1)*5+5:inchar+mes*5+5]
                    dia=dia+1
                #Julio
                mes=mes+1
                for i in range(0,31):
                    columnas[dia]=lines[i+lin][inchar+(mes-1)*5+6:inchar+mes*5+6]
                    dia=dia+1
                #MAgosto
                mes=mes+1
                for i in range(0,31):
                    columnas[dia]=lines[i+lin][inchar+(mes-1)*5+7:inchar+mes*5+7]
                    dia=dia+1
                #Septiembre
                mes=mes+1
                for i in range(0,30):
                    columnas[dia]=lines[i+lin][inchar+(mes-1)*5+8:inchar+mes*5+8]
                    dia=dia+1
                #Octubre
                mes=mes+1
                for i in range(0,31):
                    columnas[dia]=lines[i+lin][inchar+(mes-1)*5+9:inchar+mes*5+9]
                    dia=dia+1
                #Noviembre
                mes=mes+1
                for i in range(0,30):
                    columnas[dia]=lines[i+lin][inchar+(mes-1)*5+10:inchar+mes*5+10]
                    dia=dia+1
                #Diciembre
                mes=mes+1
                for i in range(0,31):
                    columnas[dia]=lines[i+lin][inchar+(mes-1)*5+11:inchar+mes*5+11]
                    dia=dia+1
                Ano=Ano+1
                lin=lin+31
            
            #Paso todo a una sola columna
            f=open(arch,"w")
            for i in range(0,len(columnas)):
                f.write(str(columnas[i])+"\n")
            f.close()

            #Reemplazo valores que faltan con None
            f=open(arch,"r")
            lines=f.readlines()
            f.close()
            last=str(len(lines)-1)
            for i in range(0,len(lines)):
                if lines[i]=='99990\n':
                    lines[i]="NaN"
                elif "9999B\n" in lines[i]:
                    lines[i]="NaN"
                elif "B\n" in lines[i]:
                    lines[i]="NaN"
                elif "9999" in lines[i]:
                    lines[i]="NaN"
                elif lines[i]=="":
                    lines[i]="NaN"  
                elif lines[i]==" ":
                    lines[i]="NaN"
                elif lines[i]==last+"\n":
                    lines[i]="NaN"
                else:
                    lines[i]=float(lines[i])
            lines=lines[0:len(lines)-1]
            
            f=open(arch,"w")
            for i in range (0,len(lines)):
                f.write(str(lines[i]) +"\n")
            f.close()
                    
