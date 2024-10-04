
import os
import tempfile
import unittest

from Persistencia.systemdao import BookingSystemDAO
from Negocio.system import BookingSystem, Room
from Negocio.interval import Interval
from Negocio.datetime import DateTime

class TestsSistemaDao(unittest.TestCase):
    def setUp(self):
        # asd
        self.temp_db = tempfile.NamedTemporaryFile(delete=False)  # pylint: disable=R1732
        self.system = BookingSystem()
        self.room1 = Room("A1", 5)
        self.room2 = Room("A2", 5)

        self.system.add_room(self.room1)
        self.system.add_room(self.room2)

        self.booking1 = Interval(DateTime(2024, 12, 1, 15, 00), DateTime(2024, 12, 1, 22, 00))
        self.booking2 = Interval(DateTime(2024, 11, 1, 15, 00), DateTime(2024, 11, 1, 22, 00))
        self.booking3 = Interval(DateTime(2024, 10, 1, 15, 00), DateTime(2024, 10, 1, 22, 00))

        
        self.daosystem = BookingSystemDAO(self.system, self.temp_db.name)

    def tearDown(self):
        self.temp_db.close()
        #os.remove(self.temp_db.name)

    def test01_can_book_room(self):
        self.daosystem.add_booking(self.room1.room_name, self.booking1)
        self.daosystem.add_booking(self.room1.room_name, self.booking2)

        reservas = self.daosystem.show_bookings(self.room1.room_name)

        
        self.assertEqual([self.booking1, self.booking2], reservas)

    def test02_can_remove_booking(self):
        self.daosystem.remove_booking(self.room1.room_name, self.booking1)

        reservas = self.daosystem.show_bookings(self.room1.room_name)

        self.assertEqual([], reservas)

    def test03_reserva_invalida_no_es_agregada(self):
        self.daosystem.add_booking(self.room2.room_name, self.booking1)
        self.daosystem.add_booking(self.room2.room_name, self.booking1)

        reservas = self.daosystem.show_bookings(self.room2.room_name)

        self.assertEqual([self.booking1], reservas)

if __name__ == "__main__":
    unittest.main()