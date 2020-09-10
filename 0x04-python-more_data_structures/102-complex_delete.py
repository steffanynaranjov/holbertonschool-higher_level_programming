#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        t = list(a_dictionary.keys())[list(a_dictionary.values()).index(value)]
        if a_dictionary[t]:
            del a_dictionary[t]
    return a_dictionary
