#!/usr/bin/python3
def simple_delete(a_dictionary, keys=None):
    if keys:
        for key in keys:
            if key in a_dictionary:
                del a_dictionary[key]
    return a_dictionary
