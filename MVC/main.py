"""from controller.controladorReserva import ControladorReserva"""
from controller.controladorCliente import controladorcliente
if __name__=="__main__":
   """ print("")
    controlador = ControladorReserva("Archivos\\clientes.txt","Archivos\\fechas.txt","Archivos\\servicios.txt","Archivos\\gastosAdministrativos.txt", )
    controlador.mostrar_menu()"""
   control = controladorcliente()
   control.menu()