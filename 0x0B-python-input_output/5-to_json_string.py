#!/usr/bin/python3
"""
Returns the JSON representation of an object
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object
    """
    rep = json.dumps(my_obj)
    return rep
