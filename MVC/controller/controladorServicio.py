from model.servicio import Servicio
from view.vistaServicio import VistaServicio

class ControladorServicio:
    def __init__(self):
        self._modelo = Servicio()
        self._vista = VistaServicio()
        self._archivo = []


    def abrirarchivo(self):
        try:
            with open("C:/Users/marti/OneDrive/Documents/GitHub/Trabajo-Practico-Integrador/Servicios.txt","r") as File:
                for line in File.readlines():
                    lineas = line.strip().split(",")
                    self._archivo.append(lineas)
        except FileNotFoundError:
                self._vista.MSJError()

    def seleccionar_servicio(self):
        self._vista.mostrar_listaServicios(self._archivo)
        opcion = self._vista.elegir_servicio()
        while opcion < 1 or opcion > 7:
            self._vista.elegir_servicio()
        else:
            match opcion:
                case 1:Servicio(self_id(self._archivo))

    def menu_servicios(self):
        self._vista.mostrar_listaServicios()