#!/usr/bin/python3

def roman_to_int(roman_string):
    result = 0
    pre_value = 0
    if roman_string is None or roman_string == "" or roman_string is str:
        return (0)
    roman_dictionary = {
                            'I' : 1,
                            'V': 5,
                            'X': 10,
                            'L': 50,
                            'C': 100,
                            'D': 500,
                            'M': 1000
                        }
    for i in range(0, len(roman_string)):
        for j in roman_dictionary:
            if roman_string[i] == j:
                result += roman_dictionary[j]
                if i != 0 and pre_value < roman_dictionary[j]:
                    result -= (2 * pre_value)
                pre_value = roman_dictionary[j]
    return (result)
