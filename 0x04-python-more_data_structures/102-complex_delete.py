#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value not in a_dictionary:
        return a_dictionary

    for key in a_dictionary:
        if key == value:
            del a_dictionary[value]

    return a_dictionary


if __name__ == "__main__":
    pass
