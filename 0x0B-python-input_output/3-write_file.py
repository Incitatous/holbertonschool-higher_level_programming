#!/usr/bin/python3
def write_file(filename="", text=""):
    i = 0
    with open(filename, mode="w") as fhandle:
        fhandle.write(text)
        for line in text:
            i += 1
        return i
