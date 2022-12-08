#!/usr/bin/python3
def roman_to_int(roman_string):
    # always check user input
    if roman_string is not None and type(roman_string) == str:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev = 1001

        for c in roman_string:
            if roman_dict[c] > prev:
                total += roman_dict[c] - (prev * 2)
            else:
                total += roman_dict[c]
            prev = roman_dict[c]
        return total
    return 0
