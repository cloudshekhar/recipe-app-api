"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test substracting numbers together"""
        res = calc.substract(2, 7)

        self.assertEqual(res, 5)
