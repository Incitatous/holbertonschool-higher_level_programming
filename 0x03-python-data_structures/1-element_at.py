#!/usr/bin/python3
def element_at(list, idx):
    if idx >= 0 and idx in list:
        return list[idx]
    else:
        return None
