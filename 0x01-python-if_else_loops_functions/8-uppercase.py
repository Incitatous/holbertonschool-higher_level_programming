#!/usr/bin/python3
def uppercase(str):
    for item in str:
        if ord('a') <= ord(item) <= ord('z'):
            var1 = (chr(ord(item) - 32))
        else:
            var1 = (item)
        print("{}".format(var1), end="")
    print("{}".format(""))
