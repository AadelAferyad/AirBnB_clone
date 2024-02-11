#!usr/bin/python3
""" this file is for unittesting """


from models.amenity import Amenity
import unittest


class AmenityTest(unittest.TestCase):
    """ test cases for Amenity class """

    def test_basic(self):
        """ basic test """
        am = Amenity()
        self.assertEqual(type(am), Amenity)

    def test_user_type(self):
        am = Amenity()
        self.assertEqual(am.name, "")

    def test_attributes(self):
        """ test attributes """
        am = Amenity()
        am.name = "haruma"

        self.assertEqual(am.name, "haruma")


if __name__ == '__main__':
    unittest.main()
