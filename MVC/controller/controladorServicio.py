from model.servicio import Servicio
from view.vistaServicio import VistaServicio

class ControladorServicio:
    def __init__(self):
        self._modelo = Servicio()
        self._vista = VistaServicio()
    