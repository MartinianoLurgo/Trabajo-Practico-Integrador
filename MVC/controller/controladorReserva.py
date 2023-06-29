import os
from model.reserva import Reserva
from view.vistaReserva import VistaReserva
from controller.controladorCalendario import ControladorCalendario
from controller.controladorCliente import ControladorCliente
from controller.controladorItem import ControladorItem
from controller.controladorServicio import ControladorServicio


class ControladorReserva:
    def __init__(self, archivoClientes, archivoFechas, archivoServicios, archivoGastosAdministrativos):
        self._modelo = Reserva()
        self._vista = VistaReserva()
        self._listaReservas = []
        self._archivoClientes = archivoClientes
        self._archivoFechas = archivoFechas
        self._archivoServicios = archivoServicios
        self._archivoGastosAdministrativos = archivoGastosAdministrativos
        self._controladorCliente = ControladorCliente()
        self._controladorServicio = ControladorServicio(self._archivoServicios)

    def mostrar_menu(self):
        opcion = 0
        while opcion != 4:
            self._vista.limpiar_pantalla()
            self._vista.mostrar_menuprincipal()
            try:
                opcion = self._vista.pedir_opcion()
                if opcion < 1 or opcion > 4:
                    self._vista.limpiar_pantalla()
                    self._vista.dato_invalido()
                    self._vista.mostrar_mensaje_continuar()
            except ValueError:
                self._vista.limpiar_pantalla()
                self._vista.dato_invalido()
                self._vista.mostrar_mensaje_continuar()
            match opcion:
                case 1:
                    return
                case 2:
                    self._controladorCliente.menu_clientes()
                case 3:
                    opcion = 0
                    while opcion != 4:
                        self._vista.limpiar_pantalla()
                        self._controladorServicio.menu_servicios()
                        try:
                            opcion = self._vista.pedir_opcion()
                            if opcion < 1 or opcion > 4:
                                self._vista.limpiar_pantalla()
                                self._vista.dato_invalido()
                                self._vista.mostrar_mensaje_continuar()
                        except ValueError:
                            self._vista.limpiar_pantalla()
                            self._vista.dato_invalido()
                            self._vista.mostrar_mensaje_continuar()
        self._vista.limpiar_pantalla()
        self._vista.mostrar_mensaje_final()
