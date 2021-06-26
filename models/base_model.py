#!/usr/bin/env python3
"""Defines class BaseModel"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Defines class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance

        Args:
            *args (tuple): Tuple that contains all arguments
            **kwargs (dict): dictionary that contains all arguments by key/value
        """
        self.id = str(uuid4())
        self.created_at = datetime.now() #Datetime when instance is created. Doesnt change.
        self.updated_at = datetime.now() #It will be updated every time you change your object.

    def __str__(self):
        """Prints BaseModel object/instance as a string"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute with current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance/object"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
