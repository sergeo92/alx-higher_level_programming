#!/usr/bin/python3

def hex_98():
    for i in range(0, 99):
        print("{:d} = {}".format(i, hex(i)))


def main():
    hex_98()


if __name__ == "__main__":
    main()
