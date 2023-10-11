#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_row = 0
    for row in my_list:
        mul = 1
        for num in range(2):
            mul *= row[num]
        sum_row += mul

    sum_weight = 0
    for row in my_list:
        for num in range(2):
            if num == 1:
                sum_weight += row[num]

    return (sum_row / sum_weight)
