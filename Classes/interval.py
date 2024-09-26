"""
    Define la clase intervalo, esta consiste entre dos fechas que conforman un intervalo de tiempo determinado, 
    desde un día a una hora hasta otro día a otra hora
"""

from Classes.datetime import DateTime

class Interval:
    def __init__(self, starting_date: DateTime, ending_date: DateTime):
        self._start = starting_date
        self._end = ending_date

    def __eq__(self, other_interval: "Interval"):
        return self._start == other_interval._start and self._end == other_interval._end

    def overlaps_with(self, other_interval: "Interval") -> bool:
        """Retorna si el intervalo se pisa con otro en alguna parte"""

        return True
