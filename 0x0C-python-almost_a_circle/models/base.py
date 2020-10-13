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
        """
        just return the json
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

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
        new file load
        """
        filename = "{}.json".format(cls.__name__)
        ins_list = []
        if os.path.isfile(filename):
            with open(filename) as f:
                ins_object = cls.from_json_string(f.read())
                for ins_dict in ins_object:
                    ins_list.append(cls.create(**ins_dict))
                return ins_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        f = "{}.csv".format(cls.__name__)
        list_dict = []
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fieldnames = ["id", "size", "x", "y"]
        with open(f, mode="w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            [writer.writerow(obj.to_dictionary())for obj in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """
        Load CSV files
        """
        list_t = []
        if os.path.isfile(cls.__name__ + ".csv"):
            with open(cls.__name__ + ".csv",
                      encoding="utf-8") as csv_file:
                csv_write = csv.DictReader(csv_file)
                for dic in csv_write:
                    for k, value in dic.items():
                        dic[k] = int(value)
                    list_t.append(cls.create(**dic))
                return list_t
