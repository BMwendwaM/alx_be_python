import unittest
from simple_calculator.py import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, 5), 10)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(6, 3), 3)
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6, 3), 18)
        self.assertEqual(self.calc.subtract(3, 3), 9)

    def test_division(self):
        if b == 0:
            return None
        else:
            self.assertEqual(self.calc.divide(8, 2), 4)
            self.assertEqual(self.calc.divide(10, 5), 2)