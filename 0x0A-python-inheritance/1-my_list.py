#!/usr/bin/python3
"""my_list module that has a MyList class"""


class MyList(list):
    """my_list module that has a MyList class"""
    def print_sorted(self):
        sort = sorted(self)
        print(sort)
