#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for ind in range(len(new_list)):
        if new_list[ind] == search:
            new_list[ind] = replace
    return new_list
