#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) < 1:
        print("0 argument.")
    else:
        for arg in sys.argv[1:]:
            print("{:d}: {}".format(len(sys.argv[1:]), sys.argv[1:]))
