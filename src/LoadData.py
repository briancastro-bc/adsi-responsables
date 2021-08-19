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
        "second": ["\t1. Para abrir el archivo", "\t0. Cancelar"]
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
    def files_list(self):
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
            pass #TODO://Continuar con el método de opciones del archivo seleccionado.
    
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