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

    match operator:
        case "+":
            res = add(a, b)
        case "-":
            res = sub(a, b)
        case "*":
            res = mul(a, b)
        case "/":
            res = div(a, b)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

    print("{} {} {} = {}".format(a, operator, b, res))
