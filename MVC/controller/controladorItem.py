from model.item import Item
from view.vistaItem import VistaItem

class ControladorItem:
    def __init__(self):
        self._modelo = Item()
        self._vista = VistaItem()
    
    def mostrar_datos(self):
        self._vista.mostrar_datos()
        self._vista.mostrar_importe(self._modelo.get_importeServicios())
        self._vista.mostrar_iva(self._modelo.calcular_iva())
        self._vista.mostrar_senia(self._modelo.calcular_senia())
        self._vista.mostrar_total(self._modelo.calcular_importeTotal())

    