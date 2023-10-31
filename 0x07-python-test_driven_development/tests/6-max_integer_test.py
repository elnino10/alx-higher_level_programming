#!/usr/bin/python3
"""The test module for max_integer function
It returns the maximum integer in a list or None if list
is empty
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test for max_integer in list of integers"""
    def setUp(self):
        self.result1 = max_integer([])
        self.result2 = max_integer([1, 2, 3, 5, 7, 4])
        self.result3 = max_integer([4])

    def test_max_integer(self):
        self.assertEqual(self.result1, None, 'list is empty')
        self.assertEqual(self.result2, 7, 'incorrect result')
        self.assertEqual(self.result3, 4, 'incorrect result')
