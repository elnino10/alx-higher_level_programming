#!/usr/bin/python3
from sys import argv

argv_size = len(argv)

if argv_size < 2:
    print("0 arguments.")
elif argv_size == 2:
    print("{} argument:".format(argv_size - 1))
    print("{}: {}".format(argv_size - 1, argv[1]))
else:
    print("{} arguments:".format(argv_size - 1))
    i = 0
    while (i < argv_size - 1):
        print("{}: {}".format(i + 1, argv[i + 1]))
        i += 1
