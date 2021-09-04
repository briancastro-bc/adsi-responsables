from src.options import Option
from src import *
from os import listdir
from os.path import isfile, join
from numpy import NaN
import pandas as pd
import time

class File:
    
    folder: str = "src/database"
    data_to_export: dict[str, list] = {
        "name": [],
        "lastname": [],
        "surname": []
    }
    
    def __init__(self, folder="src/database") -> None:
        self.folder = folder
    
    @classmethod
    def count_excel_files(self, route: str=".") -> list:
        files: list = []
        count: list = [file for file in listdir(route) if isfile(join(route, file))]
        for i in count:
            if('.xls' in i):
                files.append(i)
        return files
    
    @classmethod
    def excel_files_in_folder(self) -> None:
        print(f"\n\tFiles list in the folder {self.folder}\n")
        files_found = self.count_excel_files(self.folder)
        file_length: int = 1
        for i in files_found:
            print(f"\t({str(file_length)}): {i}")
            file_length += 1
        Option.options["second"][0] = f"\t1 al {str(file_length-1)} . para abrir el archivo."
        for j in Option.options["second"]:
            print(j)
        option: int = Option.validate_user_option("Select an option", file_length)
        if(option == 0):
            init()
        elif(option < file_length):
            self.select_file_options(files_found[option-1])
    
    @classmethod
    def select_file_options(self, file: str):
        print(f"What do you want to do with the {file} file?")
        for i in Option.options["third"]:
            print(i)
        option = Option.validate_user_option("Select an option", 2)
        if(option == 0):
            self.excel_files_in_folder()
        elif(option == 1):
            #self.read_data_from_excel_file(file)
            self.take_data_excel_file(file)
    
    # TODO:// Create a new method for age's calculate
    @classmethod
    def calculate_users_age(self, age_list):
        pass
    
    # TODO:// Nuevo método de leer datos desde Excel finalizado.
    # New method to read data from excel.
    @classmethod
    def take_data_excel_file(self, file: str):
        file_path = f"{self.folder}\\{file}" 
        sheet_name = Option.set_excel_sheet()
        dataFrame = pd.read_excel(file_path, sheet_name=sheet_name, na_values="HAVEN'T", keep_default_na=True, 
                                    dtype={
                                        'Nombre': str,
                                        'Apellido1': str,
                                        'Apellido2': str,
                                        'Nacimiento': str
                                    }
        )
        dataFrame.sort_values(by='Nombre', ascending=True)
        for value in dataFrame.values:
            self.data_to_export["name"].append(value[0])
            self.data_to_export["lastname"].append(value[1])
            self.data_to_export["surname"].append(value[2])
        self.save_new_excel_file(self.data_to_export)
        time.sleep(10)
        init()
        
        
    
    @classmethod
    def read_data_from_excel_file(self, file: str):
        start = time.time()
        file_folder = f"{self.folder}\\{file}"
        dataFrame = pd.read_excel(file_folder, sheet_name="datos_IPS")
        temp = (dataFrame.loc[:,('Nombre')]) + str(" ") + (dataFrame.loc[:,('Apellido1')]) + str(" ") + (dataFrame.loc[:, ('Apellido2')].replace(NaN, ""))
        temp = temp.sort_values()
        print(temp)
        self.save_new_excel_file(temp)
        print("="*60)
        end = time.time() #Una vez ejecutada la función guardaExcel(param) finaliza el tiempo.
        late = (end - start) #Se calcula el tiempo que se demoró en transformar el archivo.
        print("Termine, termine, acabe con el palo de café!... \ny me demoré:", late ,"segundos exportando ese jurgo de datos (",len(temp),"para ser exactos)") #Muetras el mensaje por pantalla.
        time.sleep(10)
        init()
    
    @classmethod
    def save_new_excel_file(self, data_list: dict[str, list] or list):
        while True:
            try:
                file_name = input("Nombre del archivo excel a exportar: ")
                dataFrame = pd.DataFrame(data_list)
                dataFrame.to_excel(f'data/{file_name}.xlsx', sheet_name='ejercicio', startcol=0, index=False)
                break
            except:
                print("Ha ocurrido un error.")
                response = input("¿Quieres cancelar?: ")
                if(response == 0):
                    self.excel_files_in_folder()
                    break