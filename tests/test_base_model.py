#!/usr/bin/env python3
"""Unittests for base_model.py"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from uuid import uuid4
import models


class TestBaseModel(unittest.TestCase):

    bm1 = BaseModel()
    bm2 = BaseModel()

    def test_uuid(self):
        """Tests if uuid was assigned to instance."""

        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_datetime_created_at(self):
        """Tests to see if datetime was correctly assigned"""

        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertTrue(hasattr(bm1, "created_at"))

    def test_datetime_updated_at(self):
        """Tests to see if datetime was correctly assigned"""

        bm1 = BaseModel()
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertTrue(hasattr(bm1, "updated_at"))

    def test_BaseModel_methods(self):
        """Tests if Class BaseModel has listed methods"""

        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_method(self):
        """Tests __init__ functionality"""

        bm1 = BaseModel()
        self.assertTrue(isinstance(self.bm1, BaseModel))

    def test_save_method(self):
        """Tests save method functionality"""

        bm1 = BaseModel()
        self.bm1.save()
        self.assertNotEqual(bm1.created_at, bm1.updated_at)

    def test_to_dict_method(self):
        """Tests to_dict method functionality"""
