#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (roman_string) or roman_string is None:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

    numerical_value = 0
    prev_value = 0

    for char in reversed(roman_string):
        if char in roman_numerals:
            value = roman_numerals[char]
            if value > prev_value:
                numerical_value += value
            else:
                numerical_value -= value
            prev_value = value
        else:
            return 0

    return numerical_value
