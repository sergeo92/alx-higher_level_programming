#!/usr/bin/python3


c = 0
for i in range(122, 96, -1):
    if i % 2 == 0:
        c = i
    else:
        c = i - 32
    print("{}".format(chr(c)), end='')
