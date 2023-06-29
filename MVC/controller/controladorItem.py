from model.item import Item
from view.vistaItem import VistaItem

class ControladorItem:
    def __init__(self):
        self._modelo = Item()
        self._vista = VistaItem()
    
    def menu_item(self):
        self._vista.mostrar_menu_item()
        self._vista.mostrar_importe_servicios()
        self._vista.mostrar_iva()
        self._vista.mostrar_importe_total()
    
    