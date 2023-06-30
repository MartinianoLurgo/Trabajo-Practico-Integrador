from controller.controladorReserva import ControladorReserva

if __name__=="__main__":
    controlador = ControladorReserva("Archivos\\reserva.txt","Archivos\\clientes.txt","Archivos\\fechas.txt","Archivos\\servicios.txt")
    controlador.mostrar_menu_principal()
