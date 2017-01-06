#!/usr/bin/python3
import sys
if __name__ == '__main__':
    i = 1
    if len(sys.argv[1:]) < 1:
        print("0 argument.")
    elif len(sys.argv[1:]) == 1:
            print("1 argument:")
    elif len(sys.argv[1:]) > 1:
        print("{:d} arguments:".format(len(sys.argv[1:])))
    for arg in sys.argv[1:]:
        print("{:d}: {}".format(i, arg))
        i += 1
