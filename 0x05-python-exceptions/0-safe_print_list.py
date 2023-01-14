#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for n in range(0, x):
        try:
            my_list[n]
        except IndexError:
            break

        counter += 1
        print(my_list[n])

    return counter


if __name__ == '__main__':
    list_ = [1, 2, 3, 4]
    number = safe_print_list(list_, 7)
    print(number)
