"""
    Define una hora del día
"""

from Classes.basetime import BaseTime

class Time:
    """Una hora de cualquier día"""

    def __init__(self, hour: BaseTime, minute: BaseTime) -> None:
        self.__hour = hour
        self.__minute = minute

    def __str__(self) -> str:
        return f"{str(self.__hour)}:{str(self.__minute)}:00"
