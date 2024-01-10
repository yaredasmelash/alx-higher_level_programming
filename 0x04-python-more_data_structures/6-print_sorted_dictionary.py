#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get a list of the dictionary's keys, sorted in alphabetic order
    keys = sorted(a_dictionary.keys())

    # Iterate over the sorted list of keys
    for key in keys:
        # Print the key and its corresponding value
        print("{:s}: {:s}".format(key, str(a_dictionary[key])))
