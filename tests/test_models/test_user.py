#!/usr/bin/env python3
"""unittests for user.py"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import unittest


class TestUser(unittest.TestCase):

    def test_class(self):
        """Tests class name and inheritance"""
        use = User()
        self.assertEqual(use.__class__.__name__, "User")
        self.assertTrue(issubclass(use.__class__, BaseModel))
