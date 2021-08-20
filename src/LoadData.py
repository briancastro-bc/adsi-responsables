#!/usr/bin/python
# -*- coding:utf-8 -*-

#Este programa abre un archivo de Excel con X columnas, concatena 3 de ellas y las exporta a un archivo de Excel en la misma carpeta donde se aloja este archivo Python

from os import listdir
from os.path import isfile, join
from numpy import NaN
import os
import pandas as pd
import time


class LoadData:
    
    __folder: str = "C://Users//Swyme//Desktop//adsi-responsables//src//bodega"
    options: dict = {
        "first": ["\t1. Buscar archivo", "\t0. Salir"],
        "second": ["\t1. Para abrir el archivo", "\t0. Cancelar"],
        "third": ["\t1. Exportar datos", "\t0. Cancelar"]
    }
    
    def __init__(self) -> None:
        pass
    
    #Método de entrada al módulo.
    @classmethod
    def input(self) -> None:
        print("\n¡Bienvenido al programa!\n")
        while True:
            option: int = None
            for i in self.options["first"]:
                print(i)
            option = self.validate_option("Selecciona una opción", 2)
            if(option == 0):
                os.system("cls" or "clear")
                break
            elif(option == 1):
                self.files_list()
                break
    
    #Método que muestra la lista de archivos a elegir.
    @classmethod
    def files_list(self) -> None:
        print(f"\n\tLista de archivos en la carpeta {self.__folder}\n")
        files_found = self.count_files(self.__folder)
        file_length: int = 1
        for i in files_found:
            print(f"\t({str(file_length)}): {i}")
            file_length += 1
        self.options["second"][0] = f"\t1 al {str(file_length-1)} . para abrir el archivo." #Modifica el elemento del diccionario.
        for j in self.options["second"]:
            print(j)
        option = self.validate_option("Selecciona una opción", file_length)
        if(option == 0):
            self.input()
        elif(option < file_length):
            self.actions_files(files_found[option-1])
    
    #Método que muestras las opciones para cada archivo excel.
    @classmethod
    def actions_files(self, file: str) -> None:
        print(f"¿Qué desea hacer con el archivo {file}?")
        for i in self.options["third"]:
            print(i)
        option = self.validate_option("Selecciona una opción", 2)
        if(option == 0):
            self.files_list()
        elif(option == 1):
            self.export_data(file)
        
    #Método que se encarga de contar la cantidad de archivos .xls que hay en la carpeta asignada.
    @classmethod
    def count_files(self, route: str=".") -> list:
        files: list = []
        count = [file for file in listdir(route) if isfile(join(route, file))]
        for i in count:
            if('.xls' in i):
                files.append(i.lower())
        return files
    
    #Método que válida las opciones escritas por teclado. En caso de no ser válidas, el bucle se vuelve infinito.
    @classmethod
    def validate_option(self, message: str, limit: int) -> int:
        valid = False
        while valid != True:
            try:
                option = int(input(f"{message}: "))
                if(option>=0 and option<=int(limit)):
                    valid = True
            except ValueError:
                valid = False
        return option
    
    #Método que se encarga de exportar los datos del archivo XLS leido.
    @classmethod
    def export_data(self, file: str):
        start = time.time()
        file = f"{self.__folder}\\{file}"
        dataFrame = pd.read_excel(file, sheet_name="datos_IPS", na_values="")
        temp = (dataFrame.loc[:,('Nombre')]) + str(" ") + (dataFrame.loc[:,('Apellido1')]) + str(" ") + (dataFrame.loc[:, ('Apellido2')].replace(NaN, ""))
        temp.sort_values()
        print(temp)
        self.save_excel(temp)
        print("="*60)
        end = time.time() #Una vez ejecutada la función guardaExcel(param) finaliza el tiempo.
        late = (end - start) #Se calcula el tiempo que se demoró en transformar el archivo.
        print("Termine, termine, acabe con el palo de café!... \ny me demoré:", late ,"segundos exportando ese jurgo de datos (",len(temp),"para ser exactos)") #Muetras el mensaje por pantalla.
        time.sleep(10)
        self.input()
    
    #Método que guarda el archivo excel.
    @classmethod
    def save_excel(self, files_list: str):
        while True:
            try:
                file_name = input("Nombre del archivo excel a exportar")
                dataFrame = pd.DataFrame({'Datos completos': files_list})
                dataFrame.to_excel(f'{file_name}.xlsx', sheet_name='Hoja1', startcol=0, index=False)
                break
            except:
                print("Ha ocurrido un error, reintente.")
    
    @classmethod
    def timer(self):
        pass