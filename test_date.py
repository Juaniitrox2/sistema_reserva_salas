#pylint: skip-file
import unittest

from Classes.year import Year
from Classes.month import Month
from Classes.day import Day
from Classes.hour import Hour
from Classes.minute import Minute
from Classes.time import Time
from Classes.date import Date
from Classes.datetime import DateTime
from Classes.exceptions import InvalidDateValue

class TestDate(unittest.TestCase):
    def test_año_menor_a_2024_tira_error(self):
        with self.assertRaises(InvalidDateValue):
            Year(1995)
    
    def test_dia_menor_a_1_tira_error(self):
        with self.assertRaises(InvalidDateValue):
            Day(0)
    
    def test_dia_mayor_a_31_tira_error(self):
        with self.assertRaises(InvalidDateValue):
            Day(35)

    def test_mes_mayor_a_12_tira_error(self):
        with self.assertRaises(InvalidDateValue):
            Month(15)
        
    def test_mes_menor_a_1_tira_error(self):
        with self.assertRaises(InvalidDateValue):
            Month(-1)

    def test_minuto_menor_a_1_tira_error(self):
        with self.assertRaises(InvalidDateValue):
            Minute(-1)

    def test_minuto_mayor_a_59_tira_error(self):
        with self.assertRaises(InvalidDateValue):
            Minute(66)

    def test_hora_mayor_a_23_tira_error(self):
        with self.assertRaises(InvalidDateValue):
            Hour(66)

    def test_hora_menor_a_0_tira_error(self):
        with self.assertRaises(InvalidDateValue):
            Hour(-5)

    def test_fecha_invalida_levanta_error(self):
        with self.assertRaises(InvalidDateValue):
            newdate = Date(Day(33), Month(13), Year(2023))

            

if __name__ == "__main__":
    unittest.main()
