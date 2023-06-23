class Calendario:
    def __init__(self) -> None:
        self.fecha = []
        self.anio = 2023

    #GETTERS
    def get_fecha(self):
        return self.fecha
    def get_anio(self):
        return self.anio
    
    #SETTERS
    def set_fecha(self,data):
        self.fecha = data
    def set_anio(self,data):
        self.anio = data
    
    def __str__(self) -> str:
        return print(f"Fecha: {self.fecha} \nAnio: {self.anio}")