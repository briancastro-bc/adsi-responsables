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
    
    __folder: str
    options: dict = {
        "first": ["\t1. Buscar archivo", "\t0. Salir"]
    }
    
    def __init__(self, folder="bodega") -> None:
        self.__folder = folder
    
    #Método de entrada al módulo.
    @staticmethod
    def input() -> None:
        print("\nWelcome to the program!\n")
        while True:
            option: int = None
            for i in options:
                print(i)
            if(option == 0):
                os.system("cls" or "clear")
                break
    
    #Método que se encarga de contar la cantidad de archivos .xls que hay en la carpeta asignada.
    @staticmethod
    def count_files(route: str=".") -> list:
        files: list = []
        count = [file for file in listdir(route) if isfile(join(route, file))]
        for i in count:
            if('.xls' in i):
                files.append(i.lower())
        return files
    
    #Método que válida las opciones escritas por teclado. En caso de no ser válidas, el bucle se vuelve infinito.
    @staticmethod
    def validate_option(message: str, limit: int) -> int:
        valid = False
        while valid != True:
            try:
                option = int(input(f"{message}: "))
                if(option>=0 and option<=int(limit)):
                    valid = True
            except ValueError:
                valid = False
        return option