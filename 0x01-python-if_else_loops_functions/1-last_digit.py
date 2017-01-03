#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
pos = (number % 10)
if number >= 0:
    print("Last digit of ", end="")
    if pos > 5:
        print("{:d} is {:d}".format(number, pos), end="")
        print(" and is greater than 5")
    elif pos == 0:
        ("{:d} is 0 and is 0".format(number))
    elif pos < 6 and not 0:
        print("{:d} is {:d} and is less than 6 and not 0".format(number, pos))

neg = (((number * -1) % 10) * -1)
if number < 0:
    print("Last digit of ", end="")
    if neg > 5:
        print("{:d} is {:d} and is greater than 5".format(number, neg))
    elif neg == 0:
        print("{:d} is 0 and is 0".format(number))
    elif neg < 6 and not 0:
        print("{:d} is {:d} and is less than 6 and not 0".format(number, neg))
