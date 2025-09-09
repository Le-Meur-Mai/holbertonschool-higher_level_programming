#!/usr/bin/python3

def roman_to_int(roman_string):
    result = 0

    if roman_string is None or roman_string == "" or type(roman_string) != str:
        return (0)
 
    roman_letter_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman_number_list = [1, 5, 10, 50, 100, 500, 1000]

    for i in range(0, len(roman_string)):
        for j in range(0, len(roman_letter_list)):
            if roman_string[i] == roman_letter_list[j]:
                if i != 0 and roman_string[i - 1] == roman_letter_list[j - 1]:
                    result += (roman_number_list[j] - roman_number_list[j - 1])
                else:
                    result += roman_number_list[j]
    return (result)
