#!/usr/bin/python3
def multiply_by_2(my_dict):
    copy_dict = dict(my_dict)
    for k in copy_dict:
        copy_dict[k] *= 2
    return copy_dict
