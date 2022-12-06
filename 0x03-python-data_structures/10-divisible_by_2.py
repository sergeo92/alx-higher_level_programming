#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    list_ = []
    for n in my_list:
        if n % 2 == 0:
            list_.append(True)
        else:
            list_.append(False)
    return list_


if __name__ == '__main__':
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    st = "{:d} {:s} divisible by 2"
    while i < len(list_result):
        print(st.format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1

