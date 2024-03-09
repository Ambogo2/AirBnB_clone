#!/usr/bin/python3
"""unittest for BaseModel class."""

import unittest
from datetime import datetime
import os
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unittest for BaseModel
    """

    def setUp(self):
        """
        Setup for temporary file path
        """
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """
        Tear down for temporary file path
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            if os.path.exists("tmp.json"):
                os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """
        Test for init
        """
        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save(self):
        """
        Test for save method
        """
        model = BaseModel()

        initial_updated_at = model.updated_at

        current_updated_at = model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        model = BaseModel()

        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)

        self.assertEqual(model_dict["__class__"], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())

    def test_str(self):
        """
        Test for string representation
        """
        model = BaseModel()

        self.assertTrue(str(model).startswith('[BaseModel]'))
        self.assertIn(model.id, str(model))
        self.assertIn(type(model).__name__, str(model))

if __name__ == "__main__":
    unittest.main()
