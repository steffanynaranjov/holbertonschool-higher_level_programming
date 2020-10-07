#!/usr/bin/python3
def add_attribute(ob, name, value):
    """add attribute and  method"""
    if hasattr(ob, "__dict__"):
        setattr(ob, name, value)
    else:
        raise TypeError("can't add new attribute")
