from model.cliente import Cliente
from view.vistaCliente import VistaCliente
from view.vistaReserva import VistaReserva

class ControladorCliente:
    def __init__(self):
        self._modelo = Cliente(idCliente=0,nombre="",apellido="",dni=0,telefono=0,metodoDePago="")
        self._vistaCliente = VistaCliente()
        self._vistaReserva = VistaReserva()
        # self._archivo = archivo
        self._listaClientes = []
    
    def cargar_archivo_clientes(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                for lineas in archivo.readlines():
                    linea = lineas.strip().split(",")
                    self._modelo = Cliente(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5])
                    self._listaClientes.append(self._modelo)
        except FileNotFoundError:
            self._vista.archivo_noEncontrado()
    
    def menu_clientes(self):
        opcion = 0
        while opcion != 3:
            self._vistaReserva.limpiar_pantalla()
            self._vistaCliente.mostrar_menu_clientes()
            try:
                opcion = self._vistaCliente.pedir_opcion()
                if opcion < 1 or opcion > 3:
                    self._vistaReserva.limpiar_pantalla()
                    self._vistaCliente.dato_invalido()
                    self._vistaReserva.mostrar_mensaje_continuar()
            except ValueError:
                self._vistaReserva.limpiar_pantalla()
                self._vistaCliente.dato_invalido()
                self._vistaReserva.mostrar_mensaje_continuar()
            match opcion:
                case 1:
                    with open(self._archivo,"r") as archivo:
                        lineas = archivo.readlines()
                        for linea in lineas:
                            linea = lineas.strip().split(",")
                            print(linea)
