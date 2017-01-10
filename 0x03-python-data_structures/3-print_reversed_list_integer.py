#!/usr/bin/python3
def print_reversed_list_integer(list=[]):
    if list is not None and len(list) > 0:
        for i in list[::-1]:
            print("{:d}".format(i))
    return None
