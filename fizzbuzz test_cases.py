# __author__ = 'Scott Businge'

import unittest
from fizzbuzz_lab import fizz_buzz


class TestFizzbuz(unittest.TestCase):
    def setup(self):
        self.fizzbuzz = fizz_buzz(105)

    def test_return1(self):
        self.assertEqual(self.fizzbuzz, 'Fizz')

    def test_return2(self):
        self.assertEqual(self.fizzbuzz, 'Buzz')

    def test_return3(self):
        self.assertEqual(self.fizzbuzz, 'FizzBuzz')

    def test_2(self):
        if 105 % 3 == 0 and 105 % 5 == 0:
            self.assertEqual(self.fizzbuzz, 'FizzBuzz')
        else:
            pass

    def test_3(self):
        if 105 % 3 == 0:
            self.assertEqual(self.fizzbuzz, 'Fizz')
        else:
            pass

    def test_5(self):
        if 105 % 5 == 0:
            self.assertEqual(self.fizzbuzz, 'Fizz')
        else:
            pass
