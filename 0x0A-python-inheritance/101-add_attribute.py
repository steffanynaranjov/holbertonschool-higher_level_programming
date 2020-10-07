#!/usr/bin/python3
def add_attribute(obj, name, value):
    """add_attribute method"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
