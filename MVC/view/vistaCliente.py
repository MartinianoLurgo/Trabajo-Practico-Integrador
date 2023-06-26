
class VistaCliente:
    def mostrar_menu(self):
        print("🔅================🔸🔱🔸================🔅")
        print("       BIENVENIDO AL MENU DE CLIENTES")
        print("🔅================🔸⚜️🔸================🔅") 
        print("")
        print("1 - Mostrar Lista de Clientes ")
        print("2 - Cambiar Datos del Cliente")
        print("2 - Salir del Programa")
    
    
    def pedir_opcion(self):
        return int(input("➡️ "))
    
    def archivo_no_encontrado(self):
        print("No se encontró ningún archivo de clientes . Se creará uno nuevo.")
    
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
        print("Error, dato ingresado no válido ❌.")
    
    def registro_exitoso(self):
        print("Se Registro el cliente ✅.")
    
    def cliente_no_encontrado(self):
        print("No se encontró el cliente ❌.")
        
        
        