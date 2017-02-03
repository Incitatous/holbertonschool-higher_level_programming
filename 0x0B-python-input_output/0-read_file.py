#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as fhandle:
        for line in fhandle:
            print(line, end="")
