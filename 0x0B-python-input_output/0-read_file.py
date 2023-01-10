#!/usr/bin/python3

def read_file(filename=""):
    """Read file and print lines
    Args:
        filename (str): string

    """

    with open(filename,"r", encoding="utf-8") as my_file:
        for line in my_file:
            print(line, end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
