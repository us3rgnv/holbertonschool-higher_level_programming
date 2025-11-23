#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete an item at a specific index in a list without using pop."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
    return new_list
