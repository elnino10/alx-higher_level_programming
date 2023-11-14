#!/usr/bin/python3
"""test_square module
"""
import unittest
from io import StringIO
from unittest.mock import patch

from models.square import Square


class TestSquare(unittest.TestCase):
    """test for square

    Args:
        unittest (obj): testing framework
    """

    @patch("sys.stdout", new_callable=StringIO)
    def test_square_args(self, mock_output):
        """test for square"""
        sqr = Square(2, 3, 5, 6)
        print(sqr)
        res = mock_output.getvalue().strip()
        self.assertEqual(res, "[Square] (6) 3/5 - 2")

    def test_square_negative_x(self):
        """test for square"""
        with self.assertRaises(ValueError):
            Square(2, -6)

    @patch("sys.stdout", new_callable=StringIO)
    def test_str_with_id(self, mock_stdout):
        """test __str__ method"""
        rect = Square(5, 5, 1, 1)
        print(rect)
        print_res = mock_stdout.getvalue().strip()
        self.assertEqual(
            print_res,
            "[Square] (1) 5/1 - 5",
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_to_dictionary(self, mock_stdout):
        """test to_dictionary method"""
        rect = Square(2, 4, 5, 1)
        print(rect.to_dictionary())
        print_res = mock_stdout.getvalue().strip()
        self.assertEqual(print_res, "{'id': 1, 'size': 2, 'x': 4, 'y': 5}")

    @patch("sys.stdout", new_callable=StringIO)
    def test_update(self, mock_stdout):
        """test update method"""
        rect = Square(5, 5, 1, 1)
        rect.update(y=2)
        rect.update(size=3)
        rect.update(x=7)
        rect.update(id=52)
        print(rect)
        print_res = mock_stdout.getvalue().strip()
        self.assertEqual(print_res, "[Square] (52) 7/2 - 3")

    @patch("sys.stdout", new_callable=StringIO)
    def test_update_without_id(self, mock_stdout):
        """update id"""
        rect = Square(5, 5, 1, 0)
        rect.update(2, 2, 2, 2)
        rect.update(x=7)
        print(rect)
        print_res = mock_stdout.getvalue().strip()
        self.assertEqual(print_res, "[Square] (2) 7/2 - 2")

    @patch("sys.stdout", new_callable=StringIO)
    def test_create_dict_x(self, mock_output):
        """test create"""
        r = Square(1, 5)
        print(r.create(**{"id": 89, "size": 1, "x": 3}))
        res = mock_output.getvalue().strip()
        self.assertEqual(res, "[Square] (89) 3/0 - 1")

    @patch("sys.stdout", new_callable=StringIO)
    def test_create_dict_y(self, mock_output):
        """test create"""
        r = Square(1, 5)
        print(r.create(**{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}))
        res = mock_output.getvalue().strip()
        self.assertEqual(res, "[Square] (89) 3/4 - 1")

    @patch("sys.stdout", new_callable=StringIO)
    def test_create_dict(self, mock_output):
        """test create"""
        r1 = Square(2, 4)
        print(r1.create(**{"id": 89}))
        res = mock_output.getvalue().strip()
        self.assertEqual(res, "[Square] (89) 0/0 - 2")

    @patch("sys.stdout", new_callable=StringIO)
    def test_create_dict_width(self, mock_output):
        """test create"""
        r2 = Square(1, 5)
        print(r2.create(**{"id": 89, "width": 1}))
        res2 = mock_output.getvalue().strip()
        self.assertEqual(res2, "[Square] (89) 0/0 - 1")

    @patch("sys.stdout", new_callable=StringIO)
    def test_create_dict_height(self, mock_output):
        """test create"""
        r = Square(1, 5)
        print(r.create(**{"id": 89, "width": 1, "height": 2}))
        res = mock_output.getvalue().strip()
        self.assertEqual(res, "[Square] (89) 0/0 - 1")

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

    def test_size_list(self):
        """width as a list"""
        with self.assertRaises(TypeError):
            Square([1, 2], 3)

    def test_size_tuple(self):
        """width as a tuple"""
        with self.assertRaises(TypeError):
            Square((1, 2), 3)

    def test_size_dict(self):
        """width as a dictionary"""
        with self.assertRaises(TypeError):
            Square({"a": 1, "b": 2}, 3)

    def test_size_set(self):
        """width as a set"""
        with self.assertRaises(TypeError):
            Square({"a", 2}, 3)

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

    def test_x_list(self):
        """x as a list"""
        with self.assertRaises(TypeError):
            Square(3, [1, 2])

    def test_x_tuple(self):
        """x as a tuple"""
        with self.assertRaises(TypeError):
            Square(3, (1, 2))

    def test_x_dict(self):
        """x as a dictionary"""
        with self.assertRaises(TypeError):
            Square(3, {"a": 1, "b": 2})

    def test_x_set(self):
        """x as a set"""
        with self.assertRaises(TypeError):
            Square(3, {"a", 2})

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

    def test_y_list(self):
        """y as a list"""
        with self.assertRaises(TypeError):
            Square(3, 2, [1, 2])

    def test_y_tuple(self):
        """y as a tuple"""
        with self.assertRaises(TypeError):
            Square(3, 2, (1, 2))

    def test_y_dict(self):
        """y as a dictionary"""
        with self.assertRaises(TypeError):
            Square(3, 4, {"a": 1, "b": 2})

    def test_y_set(self):
        """y as a set"""
        with self.assertRaises(TypeError):
            Square(3, 2, {"a", 2})
