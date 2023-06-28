class VistaItem:
    def mostrar_menu(self):
        print(f"-------MENÚ DE COSTOS-------")
        print("")

    def mostrar_importe(self,servicio):
        return(f"Importe de servicios :{servicio}⛽")
        
    def mostrar_iva(self,iva):
        return (f" IVA total: {iva}😮")
    
    def mostrar_senia(self,senia):
        return(f"La seña que dio el cliente es de: {senia}💵")
    
    def mostrar_total(self,total):
        return (f"El total de servico: {total} 🛒")
    
    def mostrar_devolucion(self,devolucion):
        return (f"Devolucion: {devolucion}👌")
        
    
