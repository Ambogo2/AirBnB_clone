#!/usr/bin/python3
"""unittest for user class."""

import unittest
import os
from models.base_model import BaseModel
from models.user import User

class Test_User(unittest.TestCase):
    """Test cases for user class"""
    def setUp(self):
        """creates a temporary test file for saving data"""
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """Removes the temporary test file after the test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        user_test = User()
        self.assertEqual(user_test.email, "")
        self.assertEqual(user_test.password, "")
        self.assertEqual(user_test.first_name, "")
        self.assertEqual(user_test.last_name, "")

    def test_user_inheritance(self):
        user_test = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_representation(self):
        user_test = User()
        user_test.email = "ruthambogo.ra@gmail.com"
        user_test.first_name = "ruth"
        user_test.last_name = "ambogo"
        user_test.password = "home254"
        user_str = str(user_test)
        self.assertIn("User", user_str)
        self.assertIn("ruthambogo.ra@gmail.com", user_str)
        self.assertIn("ruth", user_str)
        self.assertIn("ambogo", user_str)
        self.assertIn("home254", user_str)

    def test_user_to_dict(self):
        user_test = User()
        user_test.email = "ruthambogo.ra@gmail.com"
        user_test.first_name = "ruth"
        user_test.last_name = "ambogo"
        user_test.password = "home254"
        user_test.save()
        user_dict = user_test.to_dict()
        self.assertEqual(user_dict['email'], "ruthambogo.ra@gmail.com")
        self.assertEqual(user_dict['first_name'], "ruth")
        self.assertEqual(user_dict['last_name'], "ambogo")
        self.assertEqual(user_dict['password'], "home254")

    def test_user_instantiation(self):
        user_test = User(email="ruthambogo.ra@gmail.com",
                        password="home254", first_name="ruth", last_name="ambogo")
        self.assertEqual(user_test.email, "ruthambogo.ra@gmail.com")
        self.assertEqual(user_test.first_name, "ruth")
        self.assertEqual(user_test.last_name, "ambogo")
        self.assertEqual(user_test.password, "home254")

    def test_user_instantiation_to_dict(self):
        user_test = User(email="ruthambogo.ra@gmail.com",
                        password="home254", first_name="ruth", last_name="ambogo")
        user_dict = user_test.to_dict()
        self.assertEqual(user_dict['email'], "ruthambogo.ra@gmail.com")
        self.assertEqual(user_test['first_name'], "ruth")
        self.assertEqual(user_test['last_name'], "ambogo")
        self.assertEqual(user_test['password'], "home254")

    def test_user_id_generation(self):
        user1 = User()
        user1 = User()
        self.assertEqual(user1.id, user2.id)

if__name__="__main__":
    unittest.main()
