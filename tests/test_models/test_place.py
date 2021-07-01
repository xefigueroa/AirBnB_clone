#!/usr/bin/env python3
"""unittests for place.py"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class TestPlace(unittest.TestCase):

    def test_class(self):
        """Tests class name and inheritance"""
        pl = Place()
        self.assertEqual(pl.__class__.__name__, "Place")
        self.assertTrue(issubclass(pl.__class__, BaseModel))
