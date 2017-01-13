#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_set = []
    if len(set_1) > len(set_2):
        for i in set_1:
            if i in set_2:
                my_set.append(i)
    else:
        for i in set_2:
            if i in set_1:
                my_set.append(i)
    return my_set
