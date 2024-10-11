class SystemDaoInterface:
    """Una clase data access object (DAO) encargada de un sistema de reservas"""

    def __init__(self, system, path: str) -> None:
        """Crea un nuevo DAO y carga la tabla en caso de no existir
        
            Args:
                Path (str): El camino/dirección del archivo de la base de datos
        """

    def add_booking(self, room: str, booking):
        """
        Agrega una reserva a la base de datos.

        Args:
            room (str): Nombre de la sala.
            booking (Interval): Reserva a agregar.

        Raises:

        """

    def show_bookings(self, room_name: str) -> list:
        """
            Devuelve todas las reservas existentes para una sala específica

            Args:
                room_name (str): El nombre de la sala

            Returns:
                list[Interval]
        """

    def remove_booking(self, room_name: str, interval) -> None:
        """Remueve una reserva de la base de datos"""

    def get_rooms(self) -> list:
        """Devuelve una lista de habitaciones guardadas
        
            Returns:

        """