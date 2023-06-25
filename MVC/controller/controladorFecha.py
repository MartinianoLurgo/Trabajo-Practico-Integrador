from model.fecha import Fecha
from view.vistaFecha import VistaFecha

class ControladorFecha:
    def __init__(self):
        self._modelo = Fecha()
        self._vista = VistaFecha()