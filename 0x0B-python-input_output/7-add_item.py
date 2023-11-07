#!/usr/bin/python3
"""
module has a script that adds all arguments to a Python list,
and then save them to a file
"""
import os
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


FILENAME = "add_item.json"
my_list = []
for index, arg in enumerate(sys.argv):
    if index > 0:
        my_list.append(arg)

if os.path.exists(FILENAME):
    my_file = load_from_json_file(FILENAME)
    my_file.extend(my_list)
    save_to_json_file(my_file, FILENAME)
else:
    save_to_json_file(my_list, FILENAME)
