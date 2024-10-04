"""Define la clase de BookingSystemDAO"""
import sqlite3

from Negocio.system import BookingSystem, Room
from Negocio.interval import Interval
from Negocio.exceptions import InvalidRoom, OccupiedRoom
from Negocio.datetime import DateTime

class BookingSystemDAO:
    """Una clase data access object (DAO) encargada de un sistema de reservas"""

    def __init__(self, system: BookingSystem, path: str) -> None:
        """Crea un nuevo DAO y carga la tabla en caso de no existir
        
            Args:
                Path (str): El camino/dirección del archivo de la base de datos
        """
        self.__db_path = path
        self.__system = system
        self.__create_table()

    def __create_table(self) -> None:
        with sqlite3.connect(self.__db_path) as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS reservas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sala_nombre INTEGER NOT NULL,
                    inicio TEXT NOT NULL,
                    fin TEXT NOT NULL,
                    FOREIGN KEY (sala_nombre) REFERENCES salas(nombre)
                )"""
            )

    def add_booking(self, room: str, booking: Interval):
        """
        Agrega una reserva a la base de datos.

        Args:
            room (str): Nombre de la sala.
            booking (Interval): Reserva a agregar.

        Raises:

        """

        try:  
            reserved_room = self.__system.book_room(room, booking)

            with sqlite3.connect(self.__db_path) as connection:
                connection.execute(
                    "INSERT INTO reservas (sala_nombre, inicio, fin) VALUES (?, ?, ?)",
                    (room, str(booking.start), str(booking.end)),
                )
        except OccupiedRoom:
            print("Sala ya ocupada en esa fecha")

    def show_bookings(self, room_name: str) -> list[Interval]:
        """
            Devuelve todas las reservas existentes para una sala específica

            Args:
                room_name (str): El nombre de la sala

            Returns:
                list[Interval]
        """

        with sqlite3.connect(self.__db_path) as connection:
            cursor = connection.execute(
                "SELECT inicio, fin FROM reservas WHERE sala_nombre = ?",
                (room_name,),
            )

            bookings = cursor.fetchall()

        return [
            Interval(starting_date=DateTime.from_string(row[0]), ending_date=DateTime.from_string(row[1])) for row in bookings
        ]
    
    def remove_booking(self, room_name: str, interval: Interval) -> None:
        """Remueve una reserva de la base de datos"""

        try:
            self.__system.remove_booking(room_name, interval)

            with sqlite3.connect(self.__db_path) as connection:
                connection.execute(
                    "DELETE FROM reservas WHERE sala_nombre = ? and inicio = ? and fin = ?",
                    (room_name, str(interval.start), str(interval.end))
                )
        except:
            print("que ha salido mal macho")

    def get_rooms(self) -> list[Room]:
        return self.__system.available_rooms()
            
        