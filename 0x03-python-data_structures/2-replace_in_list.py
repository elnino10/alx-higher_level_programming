#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    list_len = len(my_list)
    new_list = my_list

    if idx < 0:
        return new_list

    if idx >= list_len:
        return new_list

    my_list[idx] = element
    return new_list
