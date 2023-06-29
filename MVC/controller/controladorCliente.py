from model.cliente import Cliente
from view.vistaCliente import VistaCliente
from view.vistaReserva import VistaReserva

class ControladorCliente:
    def __init__(self):
<<<<<<< Updated upstream
        self._modelo = Cliente()
        self._vista = VistaCliente()
        self._clientes = []
    def arbrirarchivo(self):
        with open("Clientes.txt","r")as f:
            for line in f.readlines():
                vector = line.strip().split(";")
                self._modelo = Cliente(vector[0],vector[1],vector[2],vector[3],vector[4],vector[5])
                self._clientes.append(self._modelo)
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
                        print("Finalizo")
                        break
                opcion = self._vista.pedir_opcion()
    
    def mostrar_clientes(self):
        for cliente in self._clientes:
            print (cliente)
            
        

           
    
   
                
       

            


        




            



                
                
                
                
                
                

=======
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
>>>>>>> Stashed changes
