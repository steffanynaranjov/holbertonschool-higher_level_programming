#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or len(roman_string) == 0:
        return 0
    r_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    len_str = len(roman_string)
    for n in range(len_str):
        if not r_num.get(roman_string[n], 0):
            return 0
        if (len_str != (n + 1) and
                r_num[roman_string[n + 1]] > r_num[roman_string[n]]):
            i += -r_num[roman_string[n]]
        else:
            i += r_num[roman_string[n]]
    return i
