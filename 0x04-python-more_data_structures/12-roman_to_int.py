#!/usr/bin/python3
def roman_to_int(roman_string):
    numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    pre, sum = 0, 0

    for i in roman_string:
        sum += numbers[i] if numbers[i] <= pre else numbers[i] - pre * 2
        pre = numbers[i]
    return sum
