import os
from model.reserva import Reserva
from view.vistaReserva import VistaReserva
from controller.controladorCalendario import ControladorCalendario
from controller.controladorCliente import ControladorCliente
from controller.controladorItem import ControladorItem
from controller.controladorServicio import ControladorServicio


class ControladorReserva:
    def __init__(self):
        self._modelo = Reserva()
        self._vista = VistaReserva()
        self._controladorCliente = ControladorCliente()

    def mostrar_menu(self):
        opcion = 0
        while opcion != 4:
            os.system("cls")
            self._vista.mostrar_menuprincipal()
            try:
                opcion = self._vista.pedir_opcion()
            except ValueError:
                self._vista.mensaje_error()
                self._vista.mostrar_mensaje_continuar()
            match opcion:
                case 1:
                    self._controladorCliente()
        self._vista.mostrar_mensaje()
