from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """ test case 1 """
        self.assertEqual(add(5, 15), 20)

    def test_subtract_number(self):
        """ test case 2 """
        self.assertEqual(subtract(8, 2), 6)
