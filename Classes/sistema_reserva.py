"""
    Define la clase Sala y la clase Sistema de Reservas

"""

class Room:
    """Una sala con un proposito único"""
    def __init__(self, name: str, maximum_capacity: int) -> None:
        self.__name = name
        self.__bookings = []
        self.__maximum_capacity = maximum_capacity

    @property
    def room_name(self):
        """Retorna el nombre de la sala"""
        return self.__name

    @property
    def capacity(self):
        return self.__maximum_capacity

    def book(self, date_time):
        self.__bookings.append(date_time)

    def date_is_occupied(self, date_time):

        pass

class BookingSystem:
    def __init__(self):
        self.__salas = {}
