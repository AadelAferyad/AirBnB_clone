#!/usr/bin/python3
""" this file is for unittesting """

import unittest
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.base_model import BaseModel
import datetime


class PlaceTest(unittest.TestCase):
    """ test cases for Place class """

    def test_basic(self):
        """ basic test """
        pl = Place()
        self.assertIsInstance(pl, Place)
        self.assertIsInstance(pl.id, str)
        self.assertIsInstance(pl.created_at, datetime.datetime)
        self.assertIsInstance(pl.updated_at, datetime.datetime)
        self.assertIsInstance(pl.city_id, str)
        self.assertIsInstance(pl.user_id, str)
        self.assertIsInstance(pl.name, str)
        self.assertIsInstance(pl.description, str)
        self.assertIsInstance(pl.number_rooms, int)
        self.assertIsInstance(pl.number_bathrooms, int)
        self.assertIsInstance(pl.max_guest, int)
        self.assertIsInstance(pl.price_by_night, int)
        self.assertIsInstance(pl.latitude, float)
        self.assertIsInstance(pl.longitude, float)
        self.assertIsInstance(pl.amenity_ids, list)

    def test_type(self):
        """ test tyoe """
        pl = Place()
        self.assertEqual(pl.city_id, "")
        self.assertEqual(pl.user_id, "")
        self.assertEqual(pl.description, "")
        self.assertEqual(pl.name, "")
        self.assertEqual(pl.number_rooms, 0)
        self.assertEqual(pl.number_bathrooms, 0)
        self.assertEqual(pl.max_guest, 0)
        self.assertEqual(pl.price_by_night, 0)
        self.assertEqual(pl.longitude, 0.0)
        self.assertEqual(pl.latitude, 0.0)
        self.assertEqual(pl.amenity_ids, [])

    def test_attributes(self):
        """ test attributes """
        pl = Place()
        am = Amenity()
        ur = User()
        cy = City()
        ds = "kbira 3amra bri7tha ri7t lward o lyasmin"

        pl.city_id = cy.id
        pl.user_id = ur.id
        pl.name = "dar houda"
        pl.description = ds
        pl.number_rooms = 2
        pl.number_bathrooms = 1
        pl.max_guest = 5
        pl.price_by_night = 0
        pl.latitude = 8.2
        pl.longitude = 10.22
        pl.amenity_ids = [am.id]

        self.assertEqual(pl.city_id, cy.id)
        self.assertEqual(pl.user_id, ur.id)
        self.assertEqual(pl.description, ds)
        self.assertEqual(pl.name, "dar houda")
        self.assertEqual(pl.number_rooms, 2)
        self.assertEqual(pl.number_bathrooms, 1)
        self.assertEqual(pl.max_guest, 5)
        self.assertEqual(pl.price_by_night, 0)
        self.assertEqual(pl.latitude, 8.2)
        self.assertEqual(pl.longitude, 10.22)
        self.assertEqual(pl.amenity_ids, [am.id])

    def test_inheritance(self):
        """test_inheritance"""
        self.assertTrue(issubclass(Place, BaseModel)
                        and Place is not BaseModel)


if __name__ == "__main__":
    unittest.main()
