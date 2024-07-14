import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtraction(0, 0), 0)
        self.assertEqual(self.calc.subtraction(-1, 1), -2)
        
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(0, 6), 0)
        
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(0, 1),0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)
            
            
