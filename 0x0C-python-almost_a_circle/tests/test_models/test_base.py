#!/usr/bin/python3
"""test_base module
"""
import os
import unittest
from io import StringIO
from unittest.mock import patch

from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the base module

    Args:
        unittest (obj): testing framework
    """

    def test_nb_objects_non_empty(self):
        """tests for an integer argument passed when object created"""
        b3 = Base(3)
        self.assertEqual(b3.id, 3)

    def test_nb_objects_empty(self):
        """tests for no argument passed when object created"""
        b1 = Base()
        self.assertEqual(b1.id, b1.id)

    def test_to_json_string_empty_list(self):
        """test for to_json_string with an empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        """test for to_json_string with non-empty list"""
        result = Base.to_json_string(
            [
                {"width": 2, "heigth": 4, "id": 1, "x": 3, "y": 2},
                {"size": 4, "id": 1, "x": 3, "y": 2},
            ]
        )
        self.assertEqual(
            result,
            '[{"width": 2, "heigth": 4, "id": 1, "x": 3, "y": 2}, \
{"size": 4, "id": 1, "x": 3, "y": 2}]',
        )

    def test_to_json_string_none(self):
        """test for to_json_string with an empty list"""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_dict(self):
        """test for to_json_string with an empty list"""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_empty_stringed_list(self):
        """test for to_json_string with an empty list string"""
        result = Base.to_json_string("[]")
        self.assertEqual(result, '"[]"')

    def test_to_json_string_list_dict(self):
        """test for to_json_string with a list of dictionaries"""
        result = Base.to_json_string('[{"width": 5}]')
        self.assertEqual(result, '"[{\\"width\\": 5}]"')

    @patch("sys.stdout", new_callable=StringIO)
    def test_save_to_file(self, mock_output):
        """test save_to_file"""
        from models.rectangle import Rectangle

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            print(f.read())

            res = mock_output.getvalue().strip()

        self.assertEqual(
            res,
            '[{"id": 2, "width": 10, "height": 7, "x": 2, "y": 8}, \
{"id": 3, "width": 2, "height": 4, "x": 0, "y": 0}]',
        )

    @patch("sys.stdout", new_callable=StringIO)
    def test_save_to_file_none(self, mock_output):
        """test save_to_file"""
        from models.rectangle import Rectangle

        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            print(f.read())

            res = mock_output.getvalue().strip()

        self.assertEqual(res, "[]")

    @patch("sys.stdout", new_callable=StringIO)
    def test_save_to_file_empty_list(self, mock_output):
        """test save_to_file"""
        from models.rectangle import Rectangle

        Rectangle.save_to_file([])

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            print(f.read())

            res = mock_output.getvalue().strip()

        self.assertEqual(res, "[]")

    @patch("sys.stdout", new_callable=StringIO)
    def test_save_to_file_one_item_list(self, mock_output):
        """test save_to_file"""
        from models.rectangle import Rectangle

        r = Rectangle(1, 2, 0, 0, 3)
        Rectangle.save_to_file([r])

        with open("Rectangle.json", "r", encoding="utf-8") as f:
            print(f.read())

            res = mock_output.getvalue().strip()

        self.assertEqual(res, '[{"id": 3, "width": 1, "height": 2, "x": 0, "y": 0}]')
