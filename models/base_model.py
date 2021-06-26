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

    def to_dict(self):
