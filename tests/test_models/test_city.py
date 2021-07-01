#!/usr/bin/env python3
"""unittests for city.py"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class TestCity(unittest.TestCase):

    def test_class(self):
        """Tests class name and inheritance"""
        cit = City()
        self.assertEqual(cit.__class__.__name__, "City")
        self.assertTrue(issubclass(cit.__class__, BaseModel))
