from src.options import Option
from os import listdir
from os.path import isfile, join
import src
import pandas as pd
import time
import datetime

class File:
    
    folder: str = "src/database"
    _data_to_export: dict[str, list] = { #TODO:// Solucionar el error de incremento de datos al leer otro archivo.
        "name": [],
        "lastname": [],
        "surname": [],
        "age": [],
        "profession": [],
        "disease": []
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
        Option.options["second"][0] = f"\n\t1 al {str(file_length-1)} . para abrir el archivo."
        for j in Option.options["second"]:
            print(j)
        option: int = Option.validate_user_option("Select an option", file_length)
        if(option == 0):
            src.init()
        elif(option < file_length):
            self.select_file_options(files_found[option-1])
    
    @classmethod
    def select_file_options(self, file: str):
        print(f"\nWhat do you want to do with the {file} file?")
        for i in Option.options["third"]:
            print(i)
        option = Option.validate_user_option("Select an option", 2)
        if(option == 0):
            self.excel_files_in_folder()
        elif(option == 1):
            self.take_data_from_excel_file(file)
    
    @classmethod
    def calculate_users_age(self, age_list) -> int:
        ages: int = None
        try:
            dates_to_calculate = pd.to_datetime(age_list)
            result = datetime.datetime.now() - dates_to_calculate
            ages = int(result.days / 365)
        except Exception as e:
            pass
        return ages
    
    # New method to read data from excel.
    @classmethod
    def take_data_from_excel_file(self, file: str):
        start = time.time()
        file_path = f"{self.folder}\\{file}" 
        sheet_name = Option.set_excel_sheet()
        dataFrame = pd.read_excel(file_path, sheet_name=sheet_name, na_values="HAVEN'T", keep_default_na=True, 
                                    dtype={
                                        'Nombre': str,
                                        'Apellido1': str,
                                        'Apellido2': str,
                                        'Nacimiento': datetime.date,
                                        'Profesion': str,
                                        'Enfermedad': str
                                    }
        )
        dataFrame = dataFrame.applymap(Option.remove_spaces)
        dataFrame = dataFrame.applymap(Option.upper_nouns)
        dataFrame = dataFrame.sort_values(by=['Nombre'], axis=0, ascending=True)
        for value in dataFrame.values:
            self._data_to_export["name"].append(value[0])
            self._data_to_export["lastname"].append(value[1])
            self._data_to_export["surname"].append(value[2])
            self._data_to_export["age"].append(self.calculate_users_age(value[3]))
            self._data_to_export["profession"].append(value[4])
            self._data_to_export["disease"].append(value[5])
        self.save_new_excel_file(self._data_to_export)
        print("="*60)
        end = time.time()
        late = (end - start)
        print(f"\nTermine, termine, acabe con el palo de café!... \ny me demoré: {late} segundos exportando ese jurgo de datos (",len(self._data_to_export["name"]),"para ser exactos)\n")
        time.sleep(10)
        src.init()
    
    @classmethod
    def save_new_excel_file(self, data_list: dict[str, list] or list):
        while True:
            try:
                file_name = input("\nNombre del archivo excel a exportar: ")
                dataFrame = pd.DataFrame(data_list)
                dataFrame.to_excel(f'data/{file_name}.xlsx', sheet_name='ejercicio', startcol=0, index=False)
                break
            except Exception as e:
                print(f"{e}")
                response = input("¿Quieres cancelar? 0. Cancelar: ")
                if(response == 0):
                    self.excel_files_in_folder()
                    break