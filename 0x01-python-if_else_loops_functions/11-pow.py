#!/usr/bin/python3

def pow(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / (a**(-b))
    else:
        return a**b


def main():
    pass


if __name__ == "__main__":
    main()