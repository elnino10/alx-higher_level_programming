#!/usr/bin/python3
for rev in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(rev if rev % 2 == 0 else rev - 32), end='')
