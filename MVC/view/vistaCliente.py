class VistaCliente:
    def mostrar_menu(self):
        print("=====================")
        print(" BIENVENIDO AL MENU ")
        print("=====================")
        print("")
        print("1 - Realizar reserva de fecha ")
        print("2 - Realizar reserva de servicios ")
        print("3 - Mostrar total del importe")
        print("4 - Realizar pago de seña")
        print("5 - Cancelar la reserva")
        print("6 - Salir del programa")
    
    def pedir_opcion(self):
        return int(input("=> "))
    