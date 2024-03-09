#!/usr/bin/python3
"""unittest for amenity class."""

import unittest
import models
from models.amenity import Amenity
from datetime import datetime
import os


class TestAmenityInstantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Amenity class.
    """
    def setUp(self):
        """Setup for temporary file path"""
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Tear down for temporary file path"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_no_args_instantiates(self):
        """Test instantiation with no arguments"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance is stored in the objects"""
        self.assertIn(Amenity(), models.storage.all().values())


class TestAmenitySave(unittest.TestCase):
    """
    Unittests for save method of the Amenity class.
    """


    def test_one_save(self):
        """Test if save method updates the updated_at attribute"""
        amenity = Amenity()
        first_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)


class TestAmenityToDict(unittest.TestCase):
    """
    Unittests for to_dict method of the Amenity class.
    """
 

    def test_to_dict_type(self):
        """Test if the to_dict method returns a dictionary"""
        self.assertTrue(dict, type(Amenity().to_dict()))


if __name__ == "__main__":
    unittest.main()