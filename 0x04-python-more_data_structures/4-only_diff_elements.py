#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create a set that is the union of set_1 and set_2
    union_set = set_1 | set_2

    # Create a set that the intersection of set_1 and set_2
    inter_set = set_1 & set_2

    # Subtract the intersection set from the union set to get the set of elements
    # that are present in only one of the two sets
    only_diff_set = union_set - inter_set

    return only_diff_set
