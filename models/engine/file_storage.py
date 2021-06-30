#!/usr/bin/env python3
"""Defines Class FileStorage"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                cp_dict[key] = value.to_dict()
            json.dump(cp_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                my_dict = json.load(f)
                for key in my_dict:
                    cls_d = {"BaseModel": BaseModel, "User": User, "State":
                             State, "City": City, "Amenity": Amenity,
                             "Place": Place, "Review": Review}
                    self.__objects[key] = \
                        cls_d[my_dict[key]["__class__"]](**my_dict[key])
        except FileNotFoundError:
            pass
