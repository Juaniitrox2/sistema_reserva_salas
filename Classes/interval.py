"""
    Define la clase intervalo, esta consiste entre dos fechas que conforman 
    un intervalo de tiempo determinado, desde un día a una hora 
    hasta otro día a otra hora
"""

from Classes.datetime import DateTime
from Classes.exceptions import InvalidTimeFrame

class Interval:
    """Un intervalo de tiempo de dos fechas, inicio y fin"""

    def __init__(self, starting_date: DateTime, ending_date: DateTime):
        if ending_date < starting_date:
            raise InvalidTimeFrame

        self.__start = starting_date
        self.__end = ending_date

    @property
    def start(self):
        """La fecha inicial de un intervalo de tiempo"""
        return self.__start
    
    @property
    def end(self):
        """La fecha final de un intervalo de tiempo"""
        return self.__end
    
    def __str__(self) -> str:
        return f"{str(self.start)} | {str(self.end)}"

    def __eq__(self, other_interval: "Interval"):
        return self.start == other_interval.start and self.end == other_interval.end

    def overlaps_with(self, other_interval: "Interval") -> bool:
        """Retorna si el intervalo se pisa con otro en alguna parte"""
        return (self.end > other_interval.start or self.start < other_interval.end) # pylint: disable=W0212
    
    def contains_date(self, date: DateTime) -> bool:
        return date >= self.start and date <= self.end 
