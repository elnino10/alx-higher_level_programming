#!/usr/bin/python3

def max_integer(my_list=[]):
    list_len = len(my_list)
    i = 0

    if list_len == 0:
        return None
    max_num = my_list[0]
    while i < list_len:
        if my_list[i] >= max_num:
            max_num = my_list[i]
        i += 1
    return max_num
