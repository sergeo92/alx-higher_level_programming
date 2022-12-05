def element_at(my_list, idx):
    """Function that retrieve an element in list

    Args:
        my_list: integer list
        idx    : integer

    Returns:
        None or integer
    """

    index_last = len(my_list)-1
    if idx < 0 or idx > index_last:
        return None
    else:
        return  my_list[idx]
