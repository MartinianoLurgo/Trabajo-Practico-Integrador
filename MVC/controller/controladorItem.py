from model.item import Item
from view.vistaItem import VistaItem

class ControladorItem:
    def __init__(self,archivo):
        self._modelo = Item()
        self._vista = VistaItem()
        self._archivo = archivo
        self._lista_archivo =  []
    def menu_item(self):
        self._vista.mostrar_menu_item()
        self._vista.mostrar_importe_servicios()
        self._vista.mostrar_iva()
        self._vista.mostrar_importe_total()

    def cargarcostos(self):
        with open(self.archivos, "r", encoding="utf-8") as file:
            for linea in archivo.readlines():
                linea = linea.strip().split(";")
                _lista_archivo = 



