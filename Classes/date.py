"""
    Define una fecha (Día, Mes, Año)
"""

from Classes.basetime import BaseTime

class Date:
    """Una fecha de un año del 2024+"""

    def __init__(self, day: BaseTime, month: BaseTime, year: BaseTime) -> None:
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self) -> str:
        return f"{str(self.__day)} / {str(self.__month)} / {str(self.__year)}"
