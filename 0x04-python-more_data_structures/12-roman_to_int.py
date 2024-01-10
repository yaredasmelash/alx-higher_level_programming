#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    integer = 0
    i = 0
    while i < len(roman_string):
        if i+1 < len(roman_string) and roman_dict[roman_string[i:i+2]] > roman_dict[roman_string[i]]:
            integer += roman_dict[roman_string[i:i+2]]
            i += 2
        else:
            integer += roman_dict[roman_string[i]]
            i += 1
    return integer
