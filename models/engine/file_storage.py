#!/usr/bin/env python3
"""Defines Class FileStorage"""
import json
import models


class FileStorage:
    """serializes/deserializes instances to/from JSON file.

    Atributes:
        __file_path (str): string-path to json file
        __objects (dict): Empty but will store objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        # will return the __object dict. Since its a class attr
        # we can return it like so
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <objClassName>.id"""
        # key is className.id, value is obj
        keyNew = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[keyNew] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        cp_dict = {}
        for key, value in self.__objects.items():
            cp_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(cp_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                cp_dict = json.load(f)
                self.__objects = cp_dict
        except FileNotFoundError:
            pass
