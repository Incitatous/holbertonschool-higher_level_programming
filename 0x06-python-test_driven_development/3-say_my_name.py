#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    try:
        print("My name is {:s} ".format(first_name), end="")
    except Exception as err:
        print(err)
    try:
        print("{:s}".format(last_name))
    except Exception as err:
        print(err)
