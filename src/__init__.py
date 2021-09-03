from src.options import Option
from src.services.file import File
import os

def init() -> None:
    print("\nWelcome to the program!\n")
    while True:
        option: int = None
        for i in Option.options["first"]:
            print(i)
        option: int = Option.validate_user_option("Select an option", 2)
        if(option == 0):
            os.system("cls" or "clear")
            break
        elif(option == 1):
            File.excel_files_in_list()
            break
