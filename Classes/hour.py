"""
    Define la clase Hora
        - No puede ser mas de 23 o menos de 0
        - Solo puede ser un integer
"""

from Classes.basetime import BaseTime
from Classes.exceptions import InvalidDateValue

class Hour(BaseTime):
    """Una hora del día"""

    def __init__(self, value: int) -> None:
        if value < 0 or value > 23:
            raise InvalidDateValue("Hora inválida")

        self.__value = value

    def __str__(self):
        return str(self.__value)
