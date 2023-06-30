class vistacliente:
    def mostrar_menu(self):
        print("🔅================🔸🔱🔸================🔅")
        print("       BIENVENIDO AL MENU DE CLIENTES")
        print("🔅================🔸⚜️🔸================🔅") 
        print("")
        print("1 - Mostrar Lista de Clientes ")
        print("2 - Cambiar Datos del Cliente")
        print("3 - Salir del Programa")
        return input("elije la opcion <--")
    
    def mostrar(self,idd,nombre,apellido,dni,telefono,pago):
        print(f"{idd} - {nombre} - {apellido} - {dni} - {telefono} - {pago}")
        
    def cambiar_nombre(self):
        return input (f"escribe el nombre que deseas cambiar su atriburto")
    
    def cambiar_atributos(self):
        print("--- cambiar atributos de el usuario---")
        print("1 -  id")
        print("2 - nombre")
        print("3 - apellido ")
        print("4 - dni")
        print("5 - telefono")
        print("6 - metodo de pago ")
        return input("--que queires cambiar del usuario--")
    
    def cambiar_id(self):
        return input("escribe el id que deseas: ")
    
    def cambiar_nombre(self):
        return input("escribe el nombre que deseas cambiar:")
    
    def cambiar_apellido(self):
        return input("escribe el apellido que deseas cambiar: ")
    
    def cambiar_dni(self):
        return input("escribe el dni que deseas cambiar:")
    
    def cambiar_telefono(self):
        return input("escribe el nuevo telefono:")
    
    def cambiar_metodo_pago(self):
        return input("escribe el metodo de pago que deseas  a cambiar")