#!usr/bin/python3
""" this file is for unittesting """


from models.amenity import Amenity
import unittest
import datetime
from models.base_model import BaseModel


class AmenityTest(unittest.TestCase):
    """ test cases for Amenity class """

    def test_basic(self):
        """ basic test """
        am = Amenity()
        self.assertIsInstance(am, Amenity)
        self.assertIsInstance(am.id, str)
        self.assertIsInstance(am.created_at, datetime.datetime)
        self.assertIsInstance(am.updated_at, datetime.datetime)
        self.assertIsInstance(am.name, str)

    def test_user_type(self):
        """
        test type
        """
        am = Amenity()
        self.assertEqual(am.name, "")

    def test_attributes(self):
        """ test attributes """
        am = Amenity()
        am.name = "haruma"

        self.assertEqual(am.name, "haruma")

    def test_inheritance(self):
        """test_inheritance"""
        self.assertTrue(issubclass(Amenity, BaseModel)
                        and Amenity is not BaseModel)


if __name__ == "__main__":
    unittest.main()
