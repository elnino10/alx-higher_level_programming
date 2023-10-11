#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = 0
    for key, val in a_dictionary.items():
        if val > max_score:
            max_score = val
        else:
            continue
    for key, val in a_dictionary.items():
        if val == max_score:
            return key
