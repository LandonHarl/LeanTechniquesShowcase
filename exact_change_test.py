import unittest
from change_calculator import *


class MyTestCase(unittest.TestCase):
    def test_input(self):
        calc = ChangeCalculator(123.45)
        self.assertEqual(calc.verify_input(), "Valid option.")

    def test_calcs(self):
        calc = ChangeCalculator(894.16)
        calc.verify_input()
        self.assertEqual(calc.calc_change(), [8, 1, 2, 0, 0, 4, 0, 1, 1, 1])
