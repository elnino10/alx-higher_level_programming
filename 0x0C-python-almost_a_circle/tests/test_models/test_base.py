#!/usr/bin/python3
"""test_base module
"""
import unittest
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

    # def test_to_json_string_non_empty_list(self):
    #     """test for to_json_string with non-empty list"""
    #     result = Base.to_json_string(
    #         [
    #             {"width": 2, "heigth": 4, "id": 1, "x": 3, "y": 2},
    #             {"size": 4, "id": 1, "x": 3, "y": 2},
    #         ]
    #     )
    #     self.assertEqual(
    #         result,
    #         [
    #             {"width": 2, "heigth": 4, "id": 1, "x": 3, "y": 2},
    #             {"size": 4, "id": 1, "x": 3, "y": 2},
    #         ],
    #     )
