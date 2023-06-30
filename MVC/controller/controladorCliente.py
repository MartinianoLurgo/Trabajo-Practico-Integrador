from model.cliente import Cliente
from view.vistaCliente import vistacliente

class controladorcliente:
    def __init__(self):
        self.vista = vistacliente()
        self.modelo = Cliente()
        self.lista_cliente = []
        self.opcion = 0
    def abrirarchivo(self):
        with open("MVC\\Archivos\\clientes.txt" , "r")as f:
            for line in f.readlines():
                vector = line.strip().split(";")
                self.modelo = Cliente(vector[0],vector[1],vector[2],vector[3],vector[4],vector[5])
                self.lista_cliente.append(self.modelo)
    def menu(self):
        self.abrirarchivo()
        while  True:
            self.opcion = self.vista.mostrar_menu()
            if self.opcion == "1":
                self.mostrarclientes()
            elif self.opcion == "2":
                self.cambiartdatoscliente()
            elif self.opcion =="3":
                break
            
    def mostrarclientes(self,):
        for i in self.lista_cliente:
            self.vista.mostrar(i.get_idCliente(),i.get_nombre(),i.get_apellido(),i.get_dni(),i.get_telefono(),i.get_metodoDePago())
     
    def cambiartdatoscliente(self):
        persona=self.vista.cambiar_nombre()
        for i in self.lista_cliente:
            if persona == i.get_nombre():
                atributos = self.vista.cambiar_atributos()
                if atributos == "1":
                    i.set_idCliente(self.vista.cambiar_id())
                elif atributos == "2":
                    i.set_nombre(self.vista.cambiar_nombre())
                elif atributos == "3":
                    i.set_apellido(self.vista.cambiar_apellido())
                elif atributos == "4":
                    i.set_dni(self.vista.cambiar_dni())
                elif atributos == "5":
                    i.set_telefono(self.vista.cambiar_telefono())
                elif atributos == "6":
                    i.set_metodoDePago(self.vista.cambiar_metodo_pago())
