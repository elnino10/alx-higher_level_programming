#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = []
    union_set = set_1.union(set_2)
    intersection_set = set_1.intersection(set_2)
    new_set.extend(union_set.difference(intersection_set))
    return (new_set)
