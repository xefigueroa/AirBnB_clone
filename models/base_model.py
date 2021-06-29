#!/usr/bin/env python3
"""Defines class BaseModel"""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """Defines class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance

        Args:
            *args (tuple): Tuple that contains all arguments
            **kwargs (dict): dict that contains all arguments by key/value
        """
        tStrFormat = "%Y-%m-%dT%H:%M:%S.%f"  # pep8 said lines too long
        if len(kwargs) != 0:  # re-creates an instance/object from to_dict()
            for key, val in kwargs:
                if key == "created_at":
                    self.__dict__[key] = datetime.strptime(val, tStrFormat)
                elif key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, tStrFormat)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()  # Datetime instance is created.
            self.updated_at = datetime.now()  # Updates every time obj changes.
            storage.new(self)  # call to new() from file_storage.py

    def __str__(self):
        """Prints BaseModel object/instance as a string"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute with current datetime"""
        self.update_at = datetime.now()
        storage.save()  # storage var from __init__.py

    def to_dict(self):  # dictionary representation of an instance/object
        """returns dict with all keys/values of __dict__ of the instance/obj"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
