from model.calendario import Calendario
from view.vistaCalendario import VistaCalendario

class ControladorCalendario:
    def __init__(self):
        self._modelo = Calendario()
        self._vista = VistaCalendario()