class Calendario:
    def __init__(self):
        self._fecha = str
        self._estado = bool

    #GETTERS
    def get_fecha(self):
        return self._fecha
    def get_estado(self):
        return self._estado
    
    #SETTERS
    def set_fecha(self,data):
        self.fecha = data
    def set_estado(self,data):
        self._estado = data
        
    def __str__(self) -> str:
        return print(f"Fecha: {self._fecha} \nEstado: {self._estado}")