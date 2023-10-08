#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_len = len(my_list)
    list_copy = []

    for el in my_list:
        list_copy.append(el)

    if idx < 0:
        return list_copy

    if idx >= list_len:
        return list_copy

    list_copy[idx] = element
    return list_copy
