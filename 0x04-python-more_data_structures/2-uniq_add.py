#!/usr/bin/python3
def uniq_add(my_list=[]):
    checker = []
    for i in my_list:
        if i not in checker:
            checker.append(i)
    return sum(checker)
