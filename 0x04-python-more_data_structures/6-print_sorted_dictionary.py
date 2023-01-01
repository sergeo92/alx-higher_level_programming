#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")


if __name__ == "__main__":
    a = {'le': "C", 'Num': 89, 'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a)
