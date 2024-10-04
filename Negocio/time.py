"""
    Define una hora del día
"""

from Negocio.basetime import BaseTime

class Time:
    """Una hora de cualquier día"""

    def __init__(self, hour: BaseTime, minute: BaseTime) -> None:
        self._hour = hour
        self._minute = minute

    def __str__(self) -> str:
        return f"{str(self._hour).zfill(2)}:{str(self._minute).zfill(2)}"
    
    def __gt__(self, other: "Time") -> bool:
        return self._hour > other._hour or (self._hour == other._hour and self._minute > other._minute)
    
    def __eq__(self, other: "Time") -> bool:
        return self._hour == other._hour and self._minute == other._minute
    
    def __ge__(self, other: "Time") -> bool:
        return (self == other or self > other)
    
    def __hash__(self) -> int:
        return hash((self._hour, self._minute))
