class Servicio:
    def __init__(self) -> None:
        self._id 
        self._costo
        self._listaServicios
    #Getters
    def get_id(self):
        return self._id
    def get_costo(self):
        return self._costo
    def get_listaServicios(self):
        return self._listaServicios
    
    #Setters
    def set_id(self,data):
        self._id = data
    def set_costo(self,data):
        self._costo = data
    def set_litaServicios(self,data):
        self._listaServicios = data
    
    def __str__(self) -> str:
        return print(f"Id: {self._id}, Costo: {self._costo}, Lista de servicios: {self._listaServicios}")