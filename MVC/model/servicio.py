class Servicio:
    def __init__(self,id = 0,tipoServicio ="",descripcion ="",costo=0,estado=None):
        self._idServico = id
        self._tipoServicio = tipoServicio
        self._costo = costo
        self._estado = estado
        self._listaServicios = []
    #Getters
    def get_id(self):
        return self._idServicio
    def get_tipoServicio(self):
        return self._tipoServicio
    def get_descripcion(self):
        return self._descripcion
    def get_costo(self):
        return self._costo
    def get_estado(self):
        return self._estado
    def get_listaServicios(self):
        return self._listaServicios
    
    #Setters
    def set_id(self,data):
        self._idServicio = data
    def set_tipoServicio(self,data):
        self._tipoServicio = data
    def set_descripcion(self,data):
        self._descripcion = data
    def set_costo(self,data):
        self._costo = data
    def set_estado(self,data):
        self._estado = data
    def set_litaServicios(self,data):
        self._listaServicios = data
    
    def __str__(self) -> str:
        return print(f"Id: {self._idServicio}, Tipo de servicio: {self._tipoServicio}, Descripcion: {self._descripcion}, Costo: {self._costo}, Estado: {self._estado}, Lista de servicios: {self._listaServicios}")