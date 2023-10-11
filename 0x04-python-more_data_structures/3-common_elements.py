#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = []
    for el1 in set_1:
        for el2 in set_2:
            if el1 == el2:
                new_set.append(el1)
    return new_set
