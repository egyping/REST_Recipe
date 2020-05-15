from django.test import TestCase
from app.calc import add


class CalcCase(TestCase):
    
    def test_add_number(self):
        
        self.assertEqual(add(5 , 15), 20)