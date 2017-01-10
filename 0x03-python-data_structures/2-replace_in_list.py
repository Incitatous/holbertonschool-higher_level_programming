#!/usr/bin/python3
def replace_in_list(list, idx, element):
    if idx >= 0 and idx <= len(list):
        list[idx] = element
    return list
