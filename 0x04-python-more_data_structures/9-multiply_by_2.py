#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for item in a_dictionary.items():
        new_dictionary.update({item[0]: item[1] * 2})
    return new_dictionary
