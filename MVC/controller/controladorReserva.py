import os
from model.reserva import Reserva
from model.item import Item
from view.vistaReserva import VistaReserva
from view.vistaServicio import VistaServicio
from controller.controladorCalendario import ControladorCalendario
from controller.controladorCliente import ControladorCliente
from controller.controladorItem import ControladorItem
from controller.controladorServicio import ControladorServicio


class ControladorReserva:
    def __init__(self,archivoReservas,archivoClientes, archivoFechas, archivoServicios, archivoGastosAdministrativos):
        self._archivoReservas = archivoReservas
        self._archivoClientes = archivoClientes
        self._archivoFechas = archivoFechas
        self._archivoServicios = archivoServicios
        self._archivoGastosAdministrativos = archivoGastosAdministrativos
        self._modelo = Reserva()
        self._vista = VistaReserva()
        self._item = Item()
        self._vistaServicio = VistaServicio()
        self._listaReservas = []

    #Cargar archivo de reservas 
    def cargar_archivo_reservas(self):
        try:
            with open(self._archivoReservas, "r", encoding="utf-8") as archivo:
                for lineas in archivo.readlines():
                    linea = lineas.strip().split(";")
                    reserva = Reserva(linea[0], linea[1], linea[2], linea[3], linea[4])
                    self.listaEventos.append(reserva)
        except FileNotFoundError:
            self._vista.archivo_noEncontrado()
            
    #Cargar archivo de gastos administrativos
    def cargar_archivo_gastosAdministrativos(self):
        try:
            with open(self._archivoGastosAdministrativos , "r", encoding="utf-8") as archivo:
                for linea in archivo.readlines():
                    self._item.set_importeAdministrativo(float(linea))
        except FileNotFoundError:
            self._vista.archivo_noEncontrado()
        
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
                    controladorServicio = ControladorServicio()
                    opcion = 0
                    while opcion != 4:
                        self._vista.limpiar_pantalla()
                        self._vistaServicio.mostrar_menu_servicios()
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
                                self._vista.limpiar_pantalla()
                                controladorServicio.mostrar_lista_servicios()
                                self._vista.mostrar_mensaje_continuar()
                            case 2:
                                try:
                                    controladorServicio.cargar_archivo_servicios()
                                except FileNotFoundError:
                                    self._vista.archivo_noEncontrado()
                                controladorServicio.modificar_precio_servicios()      
        self._vista.limpiar_pantalla()
        self._vista.mostrar_mensaje_final()
