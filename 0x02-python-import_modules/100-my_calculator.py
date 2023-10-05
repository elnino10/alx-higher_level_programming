#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    arg_size = len(argv)
    if arg_size != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if operator == "+":
        res = add(a, b)
    elif operator == "-":
        res = sub(a, b)
    elif operator == "*":
        res = mul(a, b)
    elif operator == "/":
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, res))
