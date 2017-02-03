#!/usr/bin/python3
def append_write(filename="", text=""):
    i = 0
    with open(filename, mode="a") as fhandle:
        fhandle.write(text)
        for line in text:
            i += 1
        return i
