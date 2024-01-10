#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_set = set()

    # Add unique integers to the set
    for i in my_list:
        if i in unique_set:
            continue
        unique_set.add(i)

    # Calculate and return the sum of unique integers
    return sum(unique_set)
