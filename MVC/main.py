from controller.controladorReserva import ControladorReserva
if __name__=="__main__":
    print("")
    controlador = ControladorReserva("Archivos\\clientes.txt","Archivos\\fechas.txt","Archivos\\servicios.txt","Archivos\\gastosAdministrativos.txt", )
    controlador.mostrar_menu()
