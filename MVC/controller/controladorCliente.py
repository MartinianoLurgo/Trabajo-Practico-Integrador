from model.cliente import Cliente
from view.vistaCliente import VistaCliente

class ControladorCliente:
    def __init__(self):
        self._modelo = Cliente()
        self._vista = VistaCliente()