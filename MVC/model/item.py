class Item:
    def __init__(self):
        self._importeServicios
        self._iva
        self._importeTotal
        self._importeGastosVarios
    
    #Getters
    def get_importeServicios(self):
        return self._importeServicios 
    def get_iva(self):
        return self._iva
    def get_importeTotal(self):
        return self._importeTotal
    def get_importeGastoVarios(self):
        return self._importeGastosVarios
    
    #Setters
    def set_importeServicios(self, data):
        self._importeServicios = data
    def set_iva(self,data):
        self._iva = data
    def set_importeTotal(self,data):
        self._importeTotal = data
    def set_importeGastosVarios(self,data):
        self._importeGastosVarios = data

    #Calcular IVA
    def calcular_iva(self):
        self.set_iva((self._importeServicios + self._importeGastosVarios)*0.21)

    #Calcular Importe Total
    def calcular_importeTotal(self):
        importeTotal = self.get_iva() + self.get_importeServicios() + self.get_importeGastoVarios()
        self.set_importeTotal(importeTotal)
        return importeTotal
    #Calcular SEÑA
    def calcular_senia(self):
        self._importeTotal * 0.3 