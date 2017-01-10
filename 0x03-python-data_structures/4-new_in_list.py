#!/usr/bin/python3
def new_in_list(list, idx, element):
    # Colon necessary because of the pointer
    myList = list[:]
    if idx in myList:
        myList[idx] = element
    return myList
