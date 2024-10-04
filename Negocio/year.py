"""
    Define la clase año:
        - Tiene que ser un integer
        - No puede ser menor a 2024 (no se puede reservar el pasado)
"""

from Negocio.basetime import BaseTime
from Negocio.exceptions import InvalidDateValue

class Year(BaseTime):
    """Un mes de un año"""

    def __init__(self, value: int) -> None:
        if value < 2024:
            raise InvalidDateValue("Año inválido")

        self._value = value

    def __str__(self) -> str:
        return str(self._value)
