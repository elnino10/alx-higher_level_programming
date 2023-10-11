#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for ind in range(len(my_list)):
        if my_list[ind] == search:
            my_list[ind] = replace
    return my_list
