#!/usr/bin/python3
""" this file is for test cases of user class """

import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """
    test cases for user class
    """

    def test_type(self):
        """
        test type
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attribute(self):
        """
        test attributes
        """
        user = User()
        user.first_name = "Betty"
        user.last_name = "Bar"
        user.email = "airbnb@mail.com"
        user.password = "root"

        self.assertEqual(user.email, "airbnb@mail.com")
        self.assertEqual(user.first_name, "Betty")
        self.assertEqual(user.last_name, "Bar")
        self.assertEqual(user.password, "root")


if __name__ == '__main__':
    unittest.main()
