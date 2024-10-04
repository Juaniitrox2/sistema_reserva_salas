"""
    Define una fecha (Día, Mes, Año)
"""

from Negocio.day import Day
from Negocio.month import Month
from Negocio.year import Year


class Date:
    """Una fecha de un año del 2024+"""

    def __init__(self, day: int, month: int, year: int) -> None:
        """Genera una fecha de un año específico

            Args:
                - day: Day
                - month: Month
                - year: Year
        """

        self._day = Day(day)
        self._month = Month(month)
        self._year = Year(year)

    def __str__(self) -> str:
        return f"{str(self._day)}/{str(self._month)}/{str(self._year)}"

    def __eq__(self, other: "Date") -> bool:
        return self._day == other._day and self._month == other._month and self._year == other._year

    def __gt__(self, other: "Date") -> bool:
        same_year = (self._year == other._year and self._month > other._month)
        same_month = (self._year == other._year and self._month ==
                      other._month and self._day > other._day)

        return self._year > other._year or same_year or same_month

    def __ge__(self, other: "Date") -> bool:
        return (self == other or self > other)

    def __hash__(self) -> int:
        return hash((self._day, self._month, self._year))
