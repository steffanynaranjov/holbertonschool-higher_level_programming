#!/usr/bin/python3
"""
Writes an Object to a text file, using a JSON
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON
    """
    with open(filename, mode="w") as m_json:
        json.dump(my_obj, m_json)
