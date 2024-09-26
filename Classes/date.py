"""
    Define una fecha (Día, Mes, Año)
"""

from Classes.day import Day
from Classes.month import Month
from Classes.year import Year

class Date:
    """Una fecha de un año del 2024+"""

    def __init__(self, day: int, month: int, year: int) -> None:
        """Genera una fecha de un año específico
        
            Args:
                - day: Day
                - month: Month
                - year: Year
        """

        self.__day = Day(day)
        self.__month = Month(month)
        self.__year = Year(year)

    def __str__(self) -> str:
        return f"{str(self.__day)} / {str(self.__month)} / {str(self.__year)}"
