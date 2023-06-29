class Fecha:
    def __init__(self,dia=0,mes=0,anio=0):
        self._dia = dia
        self._mes = mes
        self._anio = anio

    #Getters
    def get_dia(self):
        return self._dia
    def get_mes(self):
        return self._mes
    def get_anio(self):
        return self._anio

    #Setters
    def set_dia(self,data):
        self._dia = data
    def set_mes(self,data):
        self._mes = data
    def set_anio(self,data):
        self._anio = data
    
    def __str__(self) -> str:
        return print(f"Dia: {self._dia}, Mes: {self._mes}, Año: {self._anio}")