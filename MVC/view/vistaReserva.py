import os
import time
class VistaReserva:
    def mostrar_menuprincipal(self):
        print("🔅================🔸🔱🔸================🔅")
        print("       BIENVENIDO AL MENU PRINCIPAL")
        print("🔅================🔸⚜️🔸================🔅")
        print("1 - Menu Reservas 🧉")
        print("2 - Clientes 👨‍🦱")
        print("3 - Servicios 📝")
        print("4 - Salir del programa 👋")
    
    def mostrar_detalles(self,data):
        print(data)

    def pedir_opcion(self):
        return int(input("Ingrese una opción ➡️ "))
    
    def mostrar_menureserva(self):
        print("🔅================🔸🔱🔸================🔅")
        print("       BIENVENIDO AL MENU DE RESERVAS")
        print("🔅================🔸⚜️🔸================🔅")
        print("1 - Realizar Nueva Reserva 😄")
        print("2 - Cosultar Fechas disponibles 🗓️")
        print("4 - Monto Total y su Seña 💰")
        print("5 - Cancelar Reserva ❌")
        print("6 - Volver al menú principal")

    def preguntar_confirmacion(self):
        return input("Quiere confirmar la reserva❓(SI/NO)")
    
    def mostrar_mensaje_confirmar(self):
        return print("Reserva confirmada con exito ✅")
    
    def dato_invalido(self):
        print("Error, dato ingresado no válido ❌.")

    def archivo_noEncontrado(self):
        print("------------------------------------")
        print("El Archivo no se encuenta Disponible")
        print("------------------------------------")
    
    def mostrar_mensaje_continuar(self):
        return input("Presiona enter para continuar ➡️")
    
    def mostrar_precio_gastoAdministrativo(self,data):
        return print(f"Precio actual del gasto administrativo{data}💸")

    def pedir_precio_gastoAdministrativo(self):
        return float(input("Ingrese el nuevo precio💸 -> "))
    
    def mostrar_mensaje_final(self):
        print("🔅================🔸🔱🔸================🔅")
        print("            SALISTE DEL PROGRAMA")
        print("🔅================🔸⚜️🔸================🔅")   
     
    def limpiar_pantalla(self):
        time.sleep(0.5)
        os.system("cls")
    
    def manejo_de_errores(self):
        self.limpiar_pantalla()
        self.dato_invalido()
        self.mostrar_mensaje_continuar