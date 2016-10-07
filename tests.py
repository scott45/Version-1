# TDD
__author__ = 'Scott Businge'

import unittest
import calculator


class TestOperation(unittest.TestCase):

    def test_sum(self):
        return self.assertEqual(calculator(5, 5) )

    def test_subtract(self):
        pass

    def test_multiply(self):
        pass

    def test_divide(self):
        pass
