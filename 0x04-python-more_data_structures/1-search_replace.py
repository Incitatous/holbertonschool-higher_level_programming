#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for idx, val in enumerate(new_list):
        if val is search:
            new_list.pop(search)
            new_list.insert(idx, replace)
    return new_list
