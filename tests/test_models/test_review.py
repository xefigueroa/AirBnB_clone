#!/usr/bin/env python3
"""unittests for review.py"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import unittest


class TestReview(unittest.TestCase):

    def test_class(self):
        """Tests class name and inheritance"""
        rev = Review()
        self.assertEqual(rev.__class__.__name__, "Review")
        self.assertTrue(issubclass(rev.__class__, BaseModel))
