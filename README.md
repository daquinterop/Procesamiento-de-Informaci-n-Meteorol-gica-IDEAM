# Procesamiento de Informacion Meteorologica IDEAM
Se propone un programa para procesar y hacer control de calidad de información meteorológica, contenida en archivos en formato tr5 (IDEAM). 

Estado: Versión 1. Avanzando en una nueva versión

Hay varios scripts de Python, que sirven para extraer información desde un archivo tr5 (IDEAM, periodos diarios). Se crean archivos dentro del mismo directorio en formato csv, con la iformación por estación y por variable, en el periodo de tiempo considerado. Se da una estadística descriptiva, y se completan los datos faltantes. La información de esta primera versión se encuentra en la carpeta Script_tr5, en el archivo LEEME.txt, donde se explica detalladamente el funcionamiento de cada programa, y la forma de usarlo. Adicionalmente, se cuenta con un programa para el cálculo de la Evapotranspiración potencial, junto con varios Scripts para generar de los datos procesados entradas para el modelo AquaCrop. Se utilizan los módluos Pandas, Numpy, sh y pyeto. Este último solo es necesario para el programa ETo.py, y se encuentra acá: https://github.com/woodcrafty/PyETo

En la versión 2 se espera sintetizar todo a un solo programa, con la parametrización ingresada en un archivo de texto plano, con un formato establecido. Se espera incluír más metodologías para completar datos faltantes, e incluir un algoritmo para control de calidad de la información.
