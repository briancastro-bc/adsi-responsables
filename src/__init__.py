from src.options import options
from src.services.file import File
import os

def input() -> None:
    print("\n¡Bienvenido al programa!\n")
    while True:
        option: int = None
        for i in options["first"]:
            print(i)
        option = File.validate_option("Selecciona una opción", 2)
        if(option == 0):
            os.system("cls" or "clear")
            break
        elif(option == 1):
            #self.files_list()
            break
