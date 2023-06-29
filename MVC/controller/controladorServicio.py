from model.servicio import Servicio
from view.vistaServicio import VistaServicio
from view.vistaReserva import VistaReserva
class ControladorServicio:
    def __init__(self):
        self._modelo = Servicio()
        self._vistaServicio = VistaServicio()
        self._vistaReserva = VistaReserva()
        self._archivo = "MVC\\Archivos\\servicios.txt"
        self._listaServicios = []

    def cargar_archivo_servicios(self):
        try:
            with open(self._archivo, "r", encoding="utf-8") as archivo:
                for lineas in archivo.readlines():
                    linea = lineas.strip().split(",")
                    self._modelo = Servicio(int(linea[0]), linea[1], linea[2], float(linea[3]), bool(linea[4]))
                    self._listaServicios.append(self._modelo)
        except FileNotFoundError:
            self._vistaServicio.archivo_noEncontrado()

    def mostrar_lista_servicios(self):
        self._vistaReserva.limpiar_pantalla()
        self._vistaServicio.mostrar_lista_servicios()
        with open("MVC\\Archivos\\servicios.txt", "r") as archivo:
            for lineas in archivo.readlines():
                linea = lineas.strip().split(",")
                print(linea[0] + " | " + linea[1] +" - " + linea[2] + " - " + linea[3])

    def seleccionar_servicios_reserva(self):
        for servicio in self._listaServicios:
            if servicio.getEstado() == True:
                self._vistaServicio.mostrar_servicios((str(servicio.get_idServicio()) + " - " + servicio.get_tipoServicio() + " - " + servicio.get_descripcion() + " - " + servicio.get_costo()))
        opcion = 1
        while opcion != 0:
            try:
                opcionServicio = self._vistaServicio.elegir_servicio()
                opcion = 0
            except ValueError:
                self._vistaReserva.limpiar_pantalla()
                self._vistaReserva.dato_invalido()
                self._vistaReserva.mostrar_mensaje_continuar()
        return opcionServicio

    def modificar_precio_servicios(self):
        self.cargar_archivo_servicios()
        self._vistaReserva.limpiar_pantalla()
        for servicio in self._listaServicios:
            self._vistaServicio.mostrar_servicios(str(servicio.get_idServicio()) + " - " + servicio.get_tipoServicio() + " - " + servicio.get_descripcion() + " - $" + str(servicio.get_costo()))
        opcion = self._vistaServicio.elegir_modificar_servicio()
        for servicio in self._listaServicios:
            if int(opcion) == servicio.get_idServicio():
                servicio.set_costo(self._vistaServicio.modificar_precio())

    def guardarArchivo(self):
        with open(self._archivo, "w", encoding="utf-8") as archivo:
            for servicio in self._listaServicios:
                archivo.write(str(servicio))
                archivo.write("\n")
