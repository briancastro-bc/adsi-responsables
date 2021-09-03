from os import listdir
from os.path import isfile, join


class File:
    
    # Función que cuenta los archivos Excel que existen en la ruta por parametro.
    @classmethod
    def count_files(self, route: str=".") -> list:
        files: list = []
        count: list = [file for file in listdir(
            route) if isfile(join(route, file))]
        for i in count:
            if('.xls' in i):
                files.append(i)
        return files

    # Función que se encarga de validar las opciones pasadas por consola.
    @classmethod
    def validate_option(self, message: str, limit: int) -> int:
        valid = False
        while valid != True:
            try:
                option: int(input(f"{message}: "))
                if option >= 0 and option <= int(limit):
                    valid = True
            except Exception as e:
                valid = False
                print(f"{e}")
        return option