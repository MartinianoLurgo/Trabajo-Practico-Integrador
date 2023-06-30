class Item:
    def __init__(self, cliente="",fecha="",servicios ={},importeServicios = 0.0, iva=0.0, importeTotal = 0.0, importeAdministrativos=0.0):
        self._cliente = cliente
        self._fecha = fecha
        self._servicios = servicios
        self._importeServicios = importeServicios
        self._iva = iva
        self._importeTotal = importeTotal
        self._importeAdministrativo = importeAdministrativos
    
    #Getters
    def get_cliente(self):
        return self._cliente
    def get_fecha(self):
        return self._fecha
    def get_servicios(self):
        return self._servicios
    def get_importeServicios(self):
        return self._importeServicios 
    def get_iva(self):
        return self._iva
    def get_importeTotal(self):
        return self._importeTotal
    def get_importeAdministrativo(self):
        return self._importeAdministrativo
    
    #Setters
    def set_cliente(self,data):
        self._cliente = data
    def set_fecha(self,data):
        self._fecha = data
    def set_servicios(self,data):
        self._servicios = data
    def set_importeServicios(self, data):
        self._importeServicios = data
    def set_iva(self,data):
        self._iva = data
    def set_importeTotal(self,data):
        self._importeTotal = data
    def set_importeAdministrativo(self,data):
        self._importeAdministrativo = data

    #Calcular IVA
    def calcular_iva(self):
        self.set_iva((self._importeServicios + self._importeAdministrativo)*0.21)

    #Calcular Importe Total
    def calcular_importeTotal(self):
        importeTotal = self.get_iva() + self.get_importeServicios() + self.get_importeAdministrativo()
        self.set_importeTotal(importeTotal)
        return importeTotal
    
    #Calcular SEÑA
    def calcular_senia(self):
        self._importeTotal * 0.3 