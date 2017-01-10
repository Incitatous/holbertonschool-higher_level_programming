#!/usr/bin/python3
def no_c(str):
    myStr = ""
    for i in str:
        if i != 'c' and i != 'C':
            myStr += i
    return myStr
