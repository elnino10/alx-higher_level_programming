#!/usr/bin/python3
"""test_square module
"""
import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """test for square

    Args:
        unittest (obj): testing framework
    """

    def test_size_non_empty(self):
        """tests for a non empty width with integer"""
        sqr = Square(2, 4, 3)
        self.assertEqual(sqr.size, 2)

    def test_size_empty(self):
        """tests for an empty width"""
        with self.assertRaises(TypeError):
            Square(None, 4, 2)

    def test_size_float(self):
        """tests width with a floating number"""
        with self.assertRaises(TypeError):
            Square(2.4, 5, 3)

    def test_size_string(self):
        """width as a string"""
        with self.assertRaises(TypeError):
            Square("3", 5, 5)

    def test_size_empty_string(self):
        """width as an empty string"""
        with self.assertRaises(TypeError):
            Square("", 5, 3)

    def test_size_equal_zero(self):
        """width equals zero"""
        with self.assertRaises(ValueError):
            Square(0, 4, 5)

    def test_size_negative_num(self):
        """width as a negative number"""
        with self.assertRaises(ValueError):
            Square(-2, 4, 9)

    def test_size_negative_float(self):
        """width as a negative floating number"""
        with self.assertRaises(TypeError):
            Square(-2.5, 4, 3, 2)

    def test_size_complex_num(self):
        """width as a complex number"""
        with self.assertRaises(TypeError):
            Square(1 + 2j, 4, 10, 45)

    ###########################################

    def test_x_empty(self):
        """test when x not passed"""
        sqr = Square(2)
        self.assertEqual(sqr.x, 0)

    def test_x_none(self):
        """test when x is none"""
        with self.assertRaises(TypeError):
            Square(2, None)

    def test_x_non_empty(self):
        """x non-empty argument"""
        sqr = Square(2, 5, 1)
        self.assertEqual(sqr.x, 5)

    def test_x_float(self):
        """x is a floating number"""
        with self.assertRaises(TypeError):
            Square(2, 3.1)

    def test_x_negative_num(self):
        """x is a negative number"""
        with self.assertRaises(ValueError):
            Square(2, -4, -4)

    def test_x_negative_float(self):
        """x is a negative floating number"""
        with self.assertRaises(TypeError):
            Square(2, -4.7, 4)

    def test_x_string(self):
        """x is a string"""
        with self.assertRaises(TypeError):
            Square(2, "4", "4")

    def test_x_empty_string(self):
        """x is an empty string"""
        with self.assertRaises(TypeError):
            Square(2, "")

    def test_x_complex_num(self):
        """x is a complex number"""
        with self.assertRaises(TypeError):
            Square(2, 2 + 1j, 3)

    def test_y_empty(self):
        """test when y not passed"""
        sqr = Square(2, 3)
        self.assertEqual(sqr.y, 0)

    def test_y_none(self):
        """test when y is none"""
        with self.assertRaises(TypeError):
            Square(2, 4, None)

    def test_y_non_empty(self):
        """y non-empty argument"""
        rect = Square(2, 4, 5, 3)
        self.assertEqual(rect.y, 5)

    def test_y_float(self):
        """y is a floating number"""
        with self.assertRaises(TypeError):
            Square(2, 4, 5.6)

    def test_y_negative_num(self):
        """y is a negative number"""
        with self.assertRaises(ValueError):
            Square(2, 4, -4, 3)

    def test_y_negative_float(self):
        """x is a negative floating number"""
        with self.assertRaises(TypeError):
            Square(2, 4, -4.7, 3.6)

    def test_y_string(self):
        """y is a string"""
        with self.assertRaises(TypeError):
            Square(2, 4, "4", "3")

    def test_y_empty_string(self):
        """y is an empty string"""
        with self.assertRaises(TypeError):
            Square(2, 4, "")

    def test_y_complex_num(self):
        """y is a complex number"""
        with self.assertRaises(TypeError):
            Square(2, 4, 2 + 1j, 5)
