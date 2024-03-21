#!/usr/bin/python3


def roman_to_int(roman_string):

    numbers = dict()
    numbers = {'I' : 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500,'M': 1000}
    if type(roman_string) != 'str' or roman_string == NONE:
        return 0
    for i in roman_string:
        if i not in numbers:
            return (0)
    last_num = 0
    value = 0
    for i in reversed(roman_string):
        i = int(i)
        if i < last_num:
            value -= i
        elif i > last_num:
            value += i
        last_num = i
    return (int(value))
