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
        self.assertEqual(b1.id, 1)

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

    # @patch("sys.stdout", new_callable=StringIO)
    # def test_save_to_file(self, mock_stdout):
    #     """test save_to_file"""
    #     from models.rectangle import Rectangle

    #     r1 = Rectangle(2, 3, 4, 5, 12)
    #     r2 = Rectangle(3, 4, 5, 6, 10)

    #     result = Base.save_to_file([r1, r2])
    #     print(result)
    #     print_out = mock_stdout.getvalue().strip()

    #     # if os.path.exists("Rectangle.json"):
    #     #     with open("Rectangle.json", "r", encoding="utf-8") as f:
    #     #         print(f.read())
    #     self.assertEqual(
    #         print_out,
    #         "[{'width': 2, 'height': 3, 'x': 4, 'y': 5, 'id': 12}, {'width': 3, 'height': 4, 'x': 5, 'y': 6, 'id': 10}]",
    #     )
