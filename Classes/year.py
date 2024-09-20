"""
    Define la clase año:
        - Tiene que ser un integer
        - No puede ser menor a 2024 (no se puede reservar el pasado)
"""

from Classes.basetime import BaseTime
from Classes.exceptions import InvalidDateValue

class Year(BaseTime):
    """Un mes de un año"""

    def __init__(self, value: int) -> None:
        if value < 2024:
            raise InvalidDateValue("Año inválido")

        self.__value = value

    def __str__(self) -> str:
        return str(self.__value)
