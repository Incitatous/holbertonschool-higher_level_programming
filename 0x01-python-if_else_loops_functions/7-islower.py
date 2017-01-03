#!/usr/bin/python3
def islower(c):
    #if c.islower():
    if ord(c) in range(ord('a'), ord('z') + 1):
    #if ord('a') >= c <= ord('z')
        return True
    return False
