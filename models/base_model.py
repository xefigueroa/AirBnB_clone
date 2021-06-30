#!/usr/bin/env python3
"""Defines class BaseModel"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Defines class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance

        Args:
            *args (tuple): Tuple that contains all arguments
            **kwargs (dict): dict that contains all arguments by key/value
        """
        if (kwargs):  # re-creates an instance/object from to_dict()
            del kwargs["__class__"]
            for key, val in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(val,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, value)
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()  # Datetime instance is created.
            self.updated_at = datetime.now()  # Updates every time obj changes.
            models.storage.new(self)  # call to new() from file_storage.py

    def __str__(self):
        """Prints BaseModel object/instance as a string"""
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()  # storage var from __init__.py

    def to_dict(self):  # dictionary representation of an instance/object
        """returns dict with all keys/values of __dict__ of the instance/obj"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
