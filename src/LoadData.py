#!/usr/bin/python
# -*- coding:utf-8 -*-

#Este programa abre un archivo de Excel con X columnas, concatena 3 de ellas y las exporta a un archivo de Excel en la misma carpeta donde se aloja este archivo Python

from os import listdir
from os.path import isfile, join
from numpy import NaN, number
import os
import pandas as pd
import time


class LoadData:
    
    def __init__(self, folder="bodega") -> None:
        self.__folder = folder
    
    #Método de entrada al módulo.
    @staticmethod
    def input() -> None:
        print("Hello World!")
    
    #Método que se encarga de contar la cantidad de archivos .xls que hay en la carpeta asignada.
    @staticmethod
    def count_files(route: str=".") -> list:
        files: list = []
        count = [file for file in listdir(route) if isfile(join(route, file))]
        for i in count:
            if('.xls' in i):
                files.append(i.lower())
        return files
    
    @staticmethod
    def validate_choice(message: str, option: number):
        pass #TODO:// continuar con la refactorización del código.

    __folder: str