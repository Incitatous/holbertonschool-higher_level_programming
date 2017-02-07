#!/usr/bin/python3
def number_of_lines(filename=""):
    i = 0
    with open(filename) as fhandle:
        for line in fhandle:
            i += 1
    return i
