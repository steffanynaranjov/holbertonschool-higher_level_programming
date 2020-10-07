#!/usr/bin/python3
"""
Class Student that defines a student
"""


class Student:
    """
    Class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Variables and instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the attribute of a object
        """
        if not isinstance(attrs, list):
            return self.__dict__

        for x in attrs:
            if not isinstance(x, str):
                return self.__dict__

        m_dict = self.__dict__
        n_dict = {
            attr: m_dict for attr in attrs if attr in self.__dict__.keys()
        }
        return n_dict
