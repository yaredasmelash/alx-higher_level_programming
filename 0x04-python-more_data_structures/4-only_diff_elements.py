#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Get the difference between the two sets
    diff_set = set_1.symmetric_difference(set_2)

    return diff_set

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
