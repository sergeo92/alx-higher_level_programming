#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="UTF8") as my_file:
        for line in my_file:
            line = line.replace("\n", "")
            print(line)
