#!/usr/bin/python3
def element_at(my_list, idx):

    index_last = len(my_list)-1
    if idx < 0 or idx > index_last:
        return None
    else:
        return  my_list[idx]
