from model.cliente import Cliente
from view.vistaCliente import VistaCliente

class ControladorCliente:
    def __init__(self):
        self._modelo = Cliente()
        self._vista = VistaCliente()
        self._clientes = []
    def arbrirarchivo(self):
        with open("Clientes.txt","r")as f:
            for line in f.readlines():
                vector = line.strip().split(";")
                self._vista = Cliente(vector[0],vector[1],vector[2],vector[3],vector[4],vector[5],vector[6])
                self._clientes.append(self._vista)
    def menu(self):
        try: 
            self.arbrirarchivo()
        except FileNotFoundError:
           self._vista.archivo_no_encontrado()

        opcion = self._vista.pedir_opcion()
        
        while opcion < 1 or opcion>  3:
            self._vista. dato_invalido()
            opcion = self._vista.pedir_opcion()
            while opcion < 4 and opcion > 0:
                match opcion :
                    case 1:
                        self.mostrar_clientes()
                    case 2 :
                        self.cambiar_datos_clientes()
                    case 3 :
                        print("Finalizo ")
                        break
                opcion = self._vista.pedir_opcion()
    
    def mostrar_clientes(self):
        for cliente in self._clientes:
            self._vista.mostrar_clientes(cliente.get_nombre)
    
    def cambiar_datos_clientes(self):
        for cliente in self._clientes:
            nombre= self._vista.pedir_nombre()
            if cliente.get_nombre == nombre:
                eleccion = self._vista.pedir_cambio()
                if eleccion == "nombre":
                    self._cliente.set_nombre(self.vista.pedir_nombre())
                elif eleccion == "apellido":
                    self._cliente.set_apellido(self._vista.pedir_apellido())
                elif eleccion == "dni":
                    self._cliente.set_dni(self._vista.pedir_dni())
                elif eleccion == "telefono":
                    self.cliente.set_telefono(self._vista.pedir_telefono)
                elif eleccion == "pago":
                    self._cliente.set_metodoDePago(self._vista.pedir_metodo_de_pago())
                
            


        




            



                
                
                
                
                
                

