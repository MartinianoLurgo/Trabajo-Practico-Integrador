class Cliente:
    def __init__(self):
        self._idCliente
        self._nombre
        self._dni
        self._telefono
        self._tipoDePago

    #GETTERS
    def get_idCliente(self):
        return self._idCliente
    def get_nombre(self):
        return self._nombre
    def get_dni(self):
        return self._dni
    def get_telefono(self):
        return self._telefono
    def get_tipoDePago(self):
        return self.tipoDePago
    
    #SETTERS 
    def set_idCliente(self, data):
        self._idCliente = data
    def set_nombre(self,data):
        self._nombre = data
    def set_dni(self,data):
        self._dni = data
    def set_telefono(self,data):
        self._telefono = data
    def set_tipoDePago(self,data):
        self._tipoDePago = data
    
    def __str__(self) -> str:
        return print(f"IdCliente: {self._idCliente}, Nombre: {self._nombre}, DNI: {self._dni}, Telefono: {self._telefono}, Tipo de pago: {self._tipoDePago}")