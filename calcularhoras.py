from datetime import datetime


class CalcularHoras(object):
    times = {}
    _total = 0

    def add(self, start, end):
        """Añadimos las horas ejemplo:
        start = "8:00"
        end = "14:00"
        """
        start_o = self.toDateTime(start)
        end_o = self.toDateTime(end)
        cal = self.calcular(start_o, end_o)
        self._total += cal
        self.times[end + ' - ' + start] = cal

    def calcular(self, start, end):
        date = end - start
        hours = date.seconds // 3600
        minute = (date.seconds % 3600) // 60
        return hours + minute / 60

    def toDateTime(self, str):
        return datetime.strptime(str, '%H:%M')

    @property
    def total(self):
        return self._total
       
       
# Example
# horas = CalcularHoras()
# horas.add("8:00", "9:00")
# horas.total
# Devuelve 1
