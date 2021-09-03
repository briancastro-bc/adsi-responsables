class Option:

    options: dict = {
        "first": ["\t1. Buscar archivo", "\t0. Salir"],
        "second": ["\t1. Para abrir el archivo", "\t0. Cancelar"],
        "third": ["\t1. Exportar datos", "\t0. Cancelar"]
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
