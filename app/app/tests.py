from django.test import TestCase

from app.calc import add,sub


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that values are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """THis test checks subtraction of the sub function"""
        self.assertEqual(sub(11, 5), 6)
