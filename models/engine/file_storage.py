#!/usr/bin/env python3
"""Defines Class FileStorage"""
import json
from models.base_model import BaseModel


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
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <objClassName>.id"""
        # key is className.id, value is obj
        keyNew = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[keyNew] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        cp_dict = FileStorage.__objects
        for key, value in FileStorage.__objects.items():
            cp_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(cp_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        with open(FileStorage.__file_path) as f:
            cp_dict = json.load(f)
            FileStorage.__objects = cp_dict
