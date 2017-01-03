#!/usr/bin/python3
def uppercase(str):
    for item in str:
        if ord('a') <= ord(item) <= ord('z'):
            print(chr(ord(item) - 32), end="")
        else:
            print(item, end="")
    print("{}".format(""))
