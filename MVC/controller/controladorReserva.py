from model.reserva import Reserva
from view.vistaReserva import VistaReserva

class ControladorReserva:
    def __init__(self):
        self._modelo = Reserva()
        self._vista = VistaReserva()