import calendar
class VistaCalendario:
    def mostrar_calendario(self):
        calendario = calendar.TextCalendar(calendar.SUNDAY)
        calen = calendario.prmonth(2023,10)
        return calen
    