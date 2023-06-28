class VistaCliente:
    def mostrar_menu(self):
        print("🔅================🔸🔱🔸================🔅")
        print("       BIENVENIDO AL MENU DE CLIENTES")
        print("🔅================🔸⚜️🔸================🔅") 
        print("")
        print("1 - Mostrar Lista de Clientes ")
        print("2 - Cambiar Datos del Cliente")
        print("3 - Salir del Programa")


    def pedir_opcion(self):
        return input("➡️ ")
    
    def mostrar_clientes(self,cliente):
        return f"{cliente}"

    def archivo_no_encontrado(self):
        print("No se encontró ningún archivo de clientes . Se creará uno nuevo.")
    
    def pedir_nombre(self):
        return input ("escriba el nombre la persona que deceas cambiar ")
    
    def pedir_nombre(self):
        return input("Ingrese el Nombre: ")

    def pedir_apellido(self):
        return input("Ingrese el Apellido: ")

    def pedir_dni(self):
        return int(input("Ingrese el número de DNI del cliente: ")) 

    def pedir_telefono(self):
        return int(input("Ingrese el teléfono 📞: "))

    def pedir_metodo_de_pago(self):
        return input("Ingrese el Metodo de Pago del Cliente💲: ")

    def dato_invalido(self):
        return("Error, dato ingresado no válido ❌.")

    def registro_exitoso(self):
        return("Se Registro el cliente ✅.")

    def cliente_no_encontrado(self):
        return("No se encontró el cliente ❌.")