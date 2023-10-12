#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    del_val = []
    for key, val in a_dictionary.items():
        if val != value:
            continue
        else:
            del_val.append(key)

    for el in del_val:
        del a_dictionary[el]
    return a_dictionary
