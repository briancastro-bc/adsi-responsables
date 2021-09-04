class Option:

    options: dict = {
        "first": ["\t1. Buscar archivo", "\t0. Salir"],
        "second": ["\t1. Para abrir el archivo", "\t0. Cancelar"],
        "third": ["\t1. Exportar datos", "\t0. Cancelar"],
        "affirmative_responses": ["si", "asi es", "por supuesto", "claro", "sii", "ye", "yes", "yea", "yeah", "of course"]
    }
    
    # Función que se encarga de validar las opciones pasadas por consola.
    @classmethod
    def validate_user_option(self, message: str, limit: int) -> int:
        valid = False
        while valid != True:
            try:
                option: int = int(input(f"{message}: "))
                if option >= 0 and option <= int(limit):
                    valid = True
            except Exception as e:
                valid = False
                print(f"{e}")
        return option
    
    @classmethod
    def set_excel_sheet(self) -> str:
        request: bool = False
        sheet_name = "datos_IPS"
        while request != True:
            try:
                response: str = input("\n¿Desea leer una hoja específica de su archivo Excel? ").lower()
                if(response in Option.options["affirmative_responses"]):
                    sheet_name = input("\n¿Cuál hoja de su archivo Excel desea leer? ")
                    request = True
                else:
                    print("\nLa hoja que se leerá es: {0}\n".format(sheet_name))
                    break
            except:
                print("\nWrong option, please try again.\n")
        return sheet_name
