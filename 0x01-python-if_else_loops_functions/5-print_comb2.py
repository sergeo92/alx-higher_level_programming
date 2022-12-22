#!/usr/bin/python3

def print_number():
    for i in range(0, 100):
        if i != 99:
            print("{:02d}".format(i), end=", ")
        else:
            print("{:02d}".format(i), end="")


def main():
    print_number()


if __name__ == "__main__":
    main()
