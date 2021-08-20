#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Este programa abre un archivo de Excel con X columnas, concatena 3 de ellas y las exporta a un archivo de Excel en la misma carpeta donde se aloja este archivo Python


Material de consulta:
https://aprendeconalf.es/docencia/python/manual/pandas/

https://datascienceparichay.com/article/pandas-save-dataframe-to-an-excel-file/

https://dapre.presidencia.gov.co/normativa/normativa/DECRETO%20466%20DEL%208%20DE%20MAYO%20DE%202021.pdf

'''

#Para leer archivos de una carpeta
from os import listdir
import os
from os.path import isfile, join
from numpy import NaN
#Para usar y manipular datos rapidamente: pandas
import pandas as pd
#para manipular tiempo
import time

#----------------------------------------------------------------------------------------------
#variable global donde se indica en que carpeta se almacenan los archivos
carpeta="bodega"

#Función que cuenta los archivos con formato Excel que existen.
#----------------------------------------------------------------------------------------------
#Funcion para saber cuantos archivos de asistencia hay
def ls(ruta = '.'):
    lista=[]
    archivos= [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]
    for a in archivos:
        if(".xls" in a):
            lista.append(a.lower())
    return lista

#----------------------------------------------------------------------------------------------
#Crea y guarda en un archivo de excel la lista entregada por parametros
def guardaExcel(lista):
    #anexo un titulo a la columna
    df = pd.DataFrame({'Nombres completos': lista})
    df.to_excel('Mi_archivo_excel.xlsx', sheet_name = 'Mi_hojaHHHH',startcol = 0,index=False) #Convierte los datos a un archivo excel y le asigna un nombre de hoja.

#----------------------------------------------------------------------------------------------
#Abre el archivo seleccionado y extrae los nombres, aprellido1 y apellido2 y los une en una sola cadena
#Ademas los ordena
def exportaNombres(archivo):
    inicio = time.time() #Inicializa el temporizador.
    archivo=carpeta+"\\"+archivo #Asigna el path donde está guardado el archivo con los datos.
    nombres=[]
    #Abro el archivo con los datos completos
    df = pd.read_excel(archivo, sheet_name="datos_IPS", na_values="No tiene")
    temporal=(df.loc[:,('Nombre')]) + str(" ") + (df.loc[:,('Apellido1')]) + str(" ") + (df.loc[:, ('Apellido2')].replace(NaN, "")) #En caso de no tener APELLIDO2, se remplaza por un mensaje.
    temporal=temporal.sort_values() #Acomoda los datos recibidos del archivo excel-
    print(temporal)
    guardaExcel(temporal) #Llama a la función que transforma los datos en un archivo excel.
    print("="*60)
    fin = time.time() #Una vez ejecutada la función guardaExcel(param) finaliza el tiempo.
    tardo=(fin-inicio) #Se calcula el tiempo que se demoró en transformar el archivo.
    print("Termine, termine, acabe con el palo de café!... \ny me demoré:",tardo,"segundos exportando ese jurgo de datos (",len(temporal),"para ser exactos)") #Muetras el mensaje por pantalla.
    time.sleep(10)
    menuP()

#----------------------------------------------------------------------------------------------
#menu inicial para el usuario
def menuP():
    opcion=100
    while opcion!=1:
        if opcion==0:
            os.system("cls")
            break
            
        mensaje="Bienvenido al menú principal"
        os.system("cls")
        print("╔"+"═"*80+"╗")
        a=int(((80/2)-(len(mensaje)/2)))
        print("║"+" "*a+mensaje+" "*a+"║")
        print("╚"+"═"*80+"╝")
        print("")
        print("\t\tOPCIONES:")
        print("\t1. Buscar archivo.")
        print("\t0. Salir.")
        print("")
        opcion=validaOpciones("\t\t\tIngrese opción",2)
    if(opcion==1):
        menuC()

#----------------------------------------------------------------------------------------------
#menu para seleccionar el archivoa trabajar, la arpeta por defecto es bodega
def menuC():
        mensaje="Lista de archivos existentes en la carpeta "+carpeta
        os.system("cls")
        print("┌"+"─"*80+"┐")
        a=int(((80/2)-(len(mensaje)/2)))
        print("|"+" "*a+mensaje+" "*a+" |")
        print("└"+"─"*80+"┘")
        print("")
        listadeArchivos=ls(carpeta) #Verifica el número de archivos con extensión .xls
        b=1
        for a in listadeArchivos:
            print("\t"+"("+str(b)+"):"+a) #Devuelve la posición del archivo y el nombre del mismo.
            b+=1
        print("")
        print("\t\tOPCIONES:")
        print("\t1 al "+str(b-1)+" . para abrir el archivo.")
        print("\t0. Cancelar.")
        print("")
        opcion=validaOpciones("\t\t\tIngrese opción: ",b)
        if opcion==0:
            menuP()
        elif opcion <b:
            menuA(listadeArchivos[opcion-1]) #Llama a la función que recibe una ruta de archivo el cual recuperamos el valor en la parte de arriba.

#----------------------------------------------------------------------------------------------
#Opciones a realizar con el archivo seleccionado
def menuA(archivo):
        mensaje="Acciones a realizar con el archivo: "+archivo
        os.system("cls")
        print("┌"+"─"*80+"┐")
        a=int(((80/2)-(len(mensaje)/2)))
        print("|"+" "*a+mensaje+" "*a+" |")
        print("└"+"─"*80+"┘")
        print("")
        print("\t\tOPCIONES:")
        print("\t1: Exportar nombres.")
        print("\t2: Calcular edades.")
        print("\t0. Cancelar.")
        print("")
        opcion=validaOpciones("\t\t\tIngrese opción: ",2)
        if opcion==0:
            menuC()
        elif opcion==1:
            exportaNombres(archivo) #Llama a la función que se encarga de realizar el proceso de exportación.
        elif opcion==2:
            print("TODO-Coming soon")

#Función que valida si la opción pasada por consola existe en las posibles respuestas, de no ser así, genera un bucle infinito.
#----------------------------------------------------------------------------------------------
def validaOpciones(mensaje,limite):
    valida=False
    while valida==False:
        cadenaTeclado=input(mensaje+": ")
        try: 
            a=int(cadenaTeclado)
            if(a>=0 and a <= int(limite)): #Verifica que la opción esté entre 0 y N, en caso de ser así, la variable se convierte a True.
                valida= True
        except ValueError:
            valida= False
    return a

# Función de arranque del módulo.
#----------------------------------------------------------------------------------------------
def inicio():
    menuP()

#Validación del arranque
#----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    inicio()
