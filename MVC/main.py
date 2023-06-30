"""from controller.controladorReserva import ControladorReserva"""
from controller.controladorCliente import controladorcliente
if __name__=="__main__":
   """print("")
    controlador = ControladorReserva("Archivos\\clientes.txt","Archivos\\fechas.txt","Archivos\\servicios.txt","Archivos\\gastosAdministrativos.txt", )
    controlador.mostrar_menu()"""# fede tuve que comentar esto porque sino no me anda ya q no entiendo lo q vas a ghacvert aca +
   
   control = controladorcliente()
   control.menu()