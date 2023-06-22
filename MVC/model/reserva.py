class Reserva:
    def __init__(self) -> None:
        self._id
        self._cliente 
        self._fecha
        self._servicios
        self._importe

    # GETTERS
    def get_id(self):
        return self._id
    def get_cliente(self):
        return self._cliente
    def get_servicios(self):
        return self._servicios
    def get_totalImporte(self):
        return self._totalImporte
    
    #Setters
    def set_id(self,data):
        self._id = data
    def set_cliente(self,data):
        self._cliente = data
    def set_servicios(self,data):
        self._servicios = data
    def set_totalImporte(self,data):
        self._totalImporte = data
    
    # Métodos
    def calcular_importe_total(self):
        senia = 30 / 100
        total = self._importe + self.calcular_senia()
        return total
    
    def calcular_senia(self):
        senia = self._importe * 0.3
        return senia
    
    def calcular_devolucion(self):
        devolucion = self.calcular_senia * 0.2
        return devolucion
    
    def __str__(self) -> str:
        return print(f"Id: {self._id}, Cliente: {self._cliente}, Servicios: {self._servicios}, Importe: {self._importe}")