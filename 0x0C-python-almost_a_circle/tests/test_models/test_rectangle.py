#!/usr/bin/python3
"""test_rectangle module
"""
import sys
import unittest
from io import StringIO
from unittest.mock import patch

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test for rectangle

    Args:
        unittest (obj): testing framework
    """

    def test_width_non_empty(self):
        """tests for a non empty width with integer"""
        rect = Rectangle(2, 4)
        self.assertEqual(rect.width, 2)

    def test_width_empty(self):
        """tests for an empty width"""
        with self.assertRaises(TypeError):
            Rectangle(None, 4)

    def test_width_float(self):
        """tests width with a floating number"""
        with self.assertRaises(TypeError):
            Rectangle(2.4, 5)

    def test_width_string(self):
        """width as a string"""
        with self.assertRaises(TypeError):
            Rectangle("3", 5)

    def test_width_empty_string(self):
        """width as an empty string"""
        with self.assertRaises(TypeError):
            Rectangle("", 5)

    def test_width_equal_zero(self):
        """width equals zero"""
        with self.assertRaises(ValueError):
            Rectangle(0, 4)

    def test_width_negative_num(self):
        """width as a negative number"""
        with self.assertRaises(ValueError):
            Rectangle(-2, 4)

    def test_width_negative_float(self):
        """width as a negative floating number"""
        with self.assertRaises(TypeError):
            Rectangle(-2.5, 4)

    def test_width_complex_num(self):
        """width as a complex number"""
        with self.assertRaises(TypeError):
            Rectangle(1 + 2j, 4)

    def test_width_list(self):
        """width as a list"""
        with self.assertRaises(TypeError):
            Rectangle([1, 2], 3)

    def test_width_tuple(self):
        """width as a tuple"""
        with self.assertRaises(TypeError):
            Rectangle((1, 2), 3)

    def test_width_dict(self):
        """width as a dictionary"""
        with self.assertRaises(TypeError):
            Rectangle({"a": 1, "b": 2}, 3)

    def test_width_set(self):
        """width as a set"""
        with self.assertRaises(TypeError):
            Rectangle({"a", 2}, 3)

    def test_height_non_empty(self):
        """tests for a non empty height with integer"""
        rect = Rectangle(2, 4)
        self.assertEqual(rect.height, 4)

    def test_height_empty(self):
        """tests for an empty height"""
        with self.assertRaises(TypeError):
            Rectangle(2, None)

    def test_height_float(self):
        """tests height with a floating number"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4.2)

    def test_height_string(self):
        """height as a string"""
        with self.assertRaises(TypeError):
            Rectangle(3, "5")

    def test_height_empty_string(self):
        """height as an empty string"""
        with self.assertRaises(TypeError):
            Rectangle(3, "")

    def test_height_equal_zero(self):
        """height equals zero"""
        with self.assertRaises(ValueError):
            Rectangle(3, 0)

    def test_height_negative_num(self):
        """height as a negative number"""
        with self.assertRaises(ValueError):
            Rectangle(2, -4)

    def test_height_negative_float(self):
        """height as a negative floating number"""
        with self.assertRaises(TypeError):
            Rectangle(2, -4.3)

    def test_height_complex_num(self):
        """width as a complex number"""
        with self.assertRaises(TypeError):
            Rectangle(2, 1 + 2j)

    def test_height_list(self):
        """height as a list"""
        with self.assertRaises(TypeError):
            Rectangle(3, [1, 2])

    def test_height_tuple(self):
        """height as a tuple"""
        with self.assertRaises(TypeError):
            Rectangle(3, (1, 2))

    def test_height_dict(self):
        """height as a dictionary"""
        with self.assertRaises(TypeError):
            Rectangle(3, {"a": 1, "b": 2})

    def test_height_set(self):
        """height as a set"""
        with self.assertRaises(TypeError):
            Rectangle(3, {"a", 2})

    def test_both_complex_num(self):
        """both as complex numbers"""
        with self.assertRaises(TypeError):
            Rectangle(2 + 1j, 1 + 2j)

    def test_both_negative_num(self):
        """both as negative numbers"""
        with self.assertRaises(ValueError):
            Rectangle(-2, -4)

    def test_both_equal_zero(self):
        """both equals zero"""
        with self.assertRaises(ValueError):
            Rectangle(0, 0)

    def test_both_string(self):
        """both as strings"""
        with self.assertRaises(TypeError):
            Rectangle("3", "5")

    def test_both_empty_string(self):
        """both as empty strings"""
        with self.assertRaises(TypeError):
            Rectangle("", "")

    def test_both_float(self):
        """tests both as floating numbers"""
        with self.assertRaises(TypeError):
            Rectangle(2.3, 4.2)

    def test_both_negative_float(self):
        """tests both as negative floating numbers"""
        with self.assertRaises(TypeError):
            Rectangle(-2.3, -4.2)

    def test_both_empty(self):
        """tests for empty arguments"""
        with self.assertRaises(TypeError):
            Rectangle(None, None)

    def test_x_empty(self):
        """test when x not passed"""
        rect = Rectangle(2, 4)
        self.assertEqual(rect.x, 0)

    def test_x_none(self):
        """test when x is none"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, None)

    def test_x_non_empty(self):
        """x non-empty argument"""
        rect = Rectangle(2, 4, 5)
        self.assertEqual(rect.x, 5)

    def test_x_float(self):
        """x is a floating number"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 3.1)

    def test_x_negative_num(self):
        """x is a negative number"""
        with self.assertRaises(ValueError):
            Rectangle(2, 4, -4)

    def test_x_negative_float(self):
        """x is a negative floating number"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, -4.7)

    def test_x_string(self):
        """x is a string"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, "4")

    def test_x_empty_string(self):
        """x is an empty string"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, "")

    def test_x_complex_num(self):
        """x is a complex number"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 2 + 1j)

    def test_x_list(self):
        """x as a list"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2, [1, 2])

    def test_x_tuple(self):
        """x as a tuple"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2, (1, 2))

    def test_x_dict(self):
        """x as a dictionary"""
        with self.assertRaises(TypeError):
            Rectangle(3, 4, {"a": 1, "b": 2})

    def test_x_set(self):
        """x as a set"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2, {"a", 2})

    def test_y_empty(self):
        """test when y not passed"""
        rect = Rectangle(2, 4, 3)
        self.assertEqual(rect.y, 0)

    def test_y_none(self):
        """test when y is none"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 3, None)

    def test_y_non_empty(self):
        """y non-empty argument"""
        rect = Rectangle(2, 4, 5, 3)
        self.assertEqual(rect.y, 3)

    def test_y_float(self):
        """y is a floating number"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 3, 5.6)

    def test_y_negative_num(self):
        """y is a negative number"""
        with self.assertRaises(ValueError):
            Rectangle(2, 4, 4, -3)

    def test_y_negative_float(self):
        """x is a negative floating number"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 4, -3.6)

    def test_y_string(self):
        """y is a string"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 4, "3")

    def test_y_empty_string(self):
        """y is an empty string"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 7, "")

    def test_y_complex_num(self):
        """y is a complex number"""
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 5, 2 + 1j)

    def test_y_list(self):
        """y as a list"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2, 1, [1, 2])

    def test_y_tuple(self):
        """y as a tuple"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2, 5, (1, 2))

    def test_y_dict(self):
        """y as a dictionary"""
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 2, {"a": 1, "b": 2})

    def test_y_set(self):
        """y as a set"""
        with self.assertRaises(TypeError):
            Rectangle(3, 2, 1, {"a", 2})

    def test_all_none(self):
        """test when all arguments are none"""
        with self.assertRaises(TypeError):
            Rectangle(None, None, None, None)

    def test_all_non_empty(self):
        """all are non-empty arguments"""
        rect = Rectangle(2, 4, 5, 3)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 3)

    def test_all_float(self):
        """all arguments are floating numbers"""
        with self.assertRaises(TypeError):
            Rectangle(2.3, 4.7, 3.8, 5.6)

    def test_all_negative_num(self):
        """all arguments are negative numbers"""
        with self.assertRaises(ValueError):
            Rectangle(-2, -4, -5, -3)

    def test_all_negative_float(self):
        """all arguments are negative floating numbers"""
        with self.assertRaises(TypeError):
            Rectangle(-2.5, -4.2, -7.4, -3.6)

    def test_all_string(self):
        """all arguments are strings"""
        with self.assertRaises(TypeError):
            Rectangle("2", "4", "4", "3")

    def test_all_empty_string(self):
        """all arguments are empty strings"""
        with self.assertRaises(TypeError):
            Rectangle("", "", "", "")

    def test_all_complex_num(self):
        """all arguments are complex numbers"""
        with self.assertRaises(TypeError):
            Rectangle(2 + 5j, 4 + 2j, 5 + 1j, 2 + 1j)

    def test_area(self):
        """tests for area width and height passed"""
        rect1 = Rectangle(2, 5)
        rect2 = Rectangle(3, 2, 0, 0, 10)
        self.assertEqual(rect1.area(), 10)
        self.assertEqual(rect2.area(), 6)

    def test_display(self):
        """test display method"""
        rect1 = Rectangle(2, 2)
        rect2 = Rectangle(2, 4)
        rect3 = Rectangle(2, 4, 3, 4)

        with StringIO() as my_output:
            sys.stdout = my_output

            rect1.display()
            displayed_content_1 = my_output.getvalue()
            expected_char_print_1 = "##\n##\n"
            expected_char_num_1 = 6
            self.assertEqual(displayed_content_1, expected_char_print_1)
            self.assertEqual(len(displayed_content_1), expected_char_num_1)
        sys.stdout = sys.__stdout__

        # second test case
        with StringIO() as my_output:
            sys.stdout = my_output

            rect2.display()
            displayed_content_2 = my_output.getvalue()
            expected_char_print_2 = "##\n##\n##\n##\n"
            expected_char_num_2 = 12
            self.assertEqual(displayed_content_2, expected_char_print_2)
            self.assertEqual(len(displayed_content_2), expected_char_num_2)
        sys.stdout = sys.__stdout__

        # third test case
        with StringIO() as my_output:
            sys.stdout = my_output

            rect3.display()
            displayed_content_3 = my_output.getvalue()
            expected_char_print_3 = "\n\n\n\n   ##\n   ##\n   ##\n   ##\n"
            expected_char_num_3 = 28
            self.assertEqual(displayed_content_3, expected_char_print_3)
            self.assertEqual(len(displayed_content_3), expected_char_num_3)
        sys.stdout = sys.__stdout__

    @patch("sys.stdout", new_callable=StringIO)
    def test_str_with_id(self, mock_stdout):
        """test __str__ method"""
        rect = Rectangle(5, 5, 1, 0, 1)
        print(rect)
        print_res = mock_stdout.getvalue().strip()
        self.assertEqual(
            print_res,
            "[Rectangle] (1) 1/0 - 5/5",
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_str_without_id(self, mock_stdout):
        """test __str__ method"""
        rect = Rectangle(5, 5, 1, 0)
        print(rect)
        print_res = mock_stdout.getvalue().strip()
        self.assertEqual(print_res, f"[Rectangle] ({rect.id}) 1/0 - 5/5")

    @patch("sys.stdout", new_callable=StringIO)
    def test_update(self, mock_stdout):
        """test update method"""
        rect = Rectangle(5, 5, 1, 0, 1)
        rect.update(y=2)
        rect.update(width=2)
        rect.update(height=3)
        rect.update(x=7)
        rect.update(id=52)
        print(rect)
        print_res = mock_stdout.getvalue().strip()
        self.assertEqual(print_res, "[Rectangle] (52) 7/2 - 2/3")

    @patch("sys.stdout", new_callable=StringIO)
    def test_update_without_id(self, mock_stdout):
        """update id"""
        rect = Rectangle(5, 5, 1, 0)
        rect.update(2, 2, 2, 2, 2)
        rect.update(x=7)
        print(rect)
        print_res = mock_stdout.getvalue().strip()
        self.assertEqual(print_res, "[Rectangle] (2) 7/2 - 2/2")

    @patch("sys.stdout", new_callable=StringIO)
    def test_to_dictionary(self, mock_stdout):
        """test to_dictionary method"""
        rect = Rectangle(2, 4, 5, 7, 1)
        print(rect.to_dictionary())
        print_res = mock_stdout.getvalue().strip()
        self.assertEqual(
            print_res, "{'id': 1, 'width': 2, 'height': 4, 'x': 5, 'y': 7}"
        )
