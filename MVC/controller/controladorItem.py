from model.item import Item
from view.vistaItem import VistaItem

class ControladorItem:
    def __init__(self):
        self._modelo = Item()
        self._vista = VistaItem()