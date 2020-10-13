#!/usr/bin/python3
"""
New class base
"""
import json
import os
import csv


class Base:
    """
    New class base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        new var
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries and len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write json in a new  file
        """
        new_file = "{}.json".format(cls.__name__)
        list_wri = []
        if list_objs is not None:
            list_wri = [l.to_dictionary()for l in list_objs]
        with open(new_file, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_wri))

    @staticmethod
    def from_json_string(json_string):
        """
        return a string of json
        """
        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        new instance
        """
        new_ins = None
        if cls.__name__ == "Rectangle":
            new_ins = cls(1, 1)
        elif cls.__name__ == "Square":
            new_ins = cls(1)
        new_ins.update(**dictionary)
        return new_ins

    @classmethod
    def load_from_file(cls):
        """
        load a new class
        """
        filename = "{}.json".format(cls.__name__)
        l_d = []
        if os.path.exists(filename):
            with open(filename, mode="r", encoding="utf-8") as f:
                l_d = [cls.create(**d)for d in cls.from_json_string(f.read())]
        return l_d

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filen = "{}.csv".format(cls.__name__)
        list_dic = []
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fieldnames = ["id", "size", "x", "y"]
        with open(filen, mode="w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            [writer.writerow(obj.to_dictionary())for obj in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        filen = "{}.csv".format(cls.__name__)
        list_dic = []
        if os.path.exists(filen):
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            with open(filen, newline='') as csvfile:
                list_dic = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dic = [dict([k, int(v)]for k, v in obj.items())
                             for obj in list_dic]
                list_dic = [cls.create(**dict)for dict in list_dic]
        return list_dic
