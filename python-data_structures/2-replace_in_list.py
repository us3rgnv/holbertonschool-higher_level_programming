#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace element at a specific index of a list.

    Args:
        my_list (list): The original list
        idx (int): The index to replace
        element (any): The new element

    Returns:
        list: The modified list, or original if idx is invalid
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
