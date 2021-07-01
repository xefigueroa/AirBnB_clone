#!/usr/bin/env python3
"""unittests for state.py"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class TestState(unittest.TestCase):

    def test_class(self):
        """Tests class name and inheritance"""
        stt = State()
        self.assertEqual(stt.__class__.__name__, "State")
        self.assertTrue(issubclass(stt.__class__, BaseModel))
