#!/usr/bin/python3
def inherits_from(obj, a_class):
    if issublclass(obj,  a_class) or isinstance(obj, a_class):
        return True
    return False
