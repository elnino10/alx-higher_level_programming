#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        calc = add(a, b)
        for i in range(4, 6):
            calc = add(calc, i)
        return (calc)
    else:
        return(sub(a, b))