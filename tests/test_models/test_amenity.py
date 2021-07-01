#!/usr/bin/env python3
"""unittests for amenity.py"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class TestAmenity(unittest.TestCase):

    def test_class(self):
        """Tests class name and inheritance"""
        amen = Amenity()
        self.assertEqual(amen.__class__.__name__, "Amenity")
        self.assertTrue(issubclass(amen.__class__, BaseModel))
