#!/usr/bin/python3
def print_reversed_list_integer(list=[]):
    if list != None:
        for i in list[::-1]:
            print("{:d}".format(i))
            # print(str.format(str(i)))
