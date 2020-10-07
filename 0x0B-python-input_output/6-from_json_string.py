#!/usr/bin/python3
"""
Returns an object represented by a JSON
"""


import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON
    """
    rep = json.loads(my_str)
    return rep
