#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_size = len(argv)
    i = 1
    arg_sum = 0
    while i < arg_size:
        arg_sum += int(argv[i])
        i += 1
    print("{}".format(arg_sum))
