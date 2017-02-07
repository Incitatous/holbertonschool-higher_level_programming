#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    i = 1
    with open(filename) as fhandle:
            if nb_lines <= 0:
                print(fhandle.read(), end="")
            else:
                for line in fhandle:
                    if i <= nb_lines:
                        print(line, end="")
                        i += 1
